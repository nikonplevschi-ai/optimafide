const ALLOWED_ORIGINS = new Set([
  "https://recovery.optimafide.md",
  "https://nikonplevschi-ai.github.io",
  "https://optimafide.pages.dev"
]);

function isAllowedOrigin(origin) {
  return ALLOWED_ORIGINS.has(origin);
}

function corsHeaders(origin) {
  const headers = {
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Content-Type": "application/json; charset=utf-8",
    "Vary": "Origin"
  };
  if (isAllowedOrigin(origin)) headers["Access-Control-Allow-Origin"] = origin;
  return headers;
}

function json(origin, data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: corsHeaders(origin)
  });
}

function clean(value, max = 1500) {
  return String(value || "")
    .replace(/[<>]/g, "")
    .trim()
    .slice(0, max);
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || "";

    if (request.method === "GET") {
      return json(origin, { ok: true, service: "optima-fide-telegram-requests" });
    }

    if (!isAllowedOrigin(origin)) {
      return json(origin, { ok: false, error: "Origin not allowed" }, 403);
    }

    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: corsHeaders(origin) });
    }

    if (request.method !== "POST") {
      return json(origin, { ok: false, error: "Method not allowed" }, 405);
    }

    const contentLength = Number(request.headers.get("Content-Length") || 0);
    if (contentLength > 20_000) {
      return json(origin, { ok: false, error: "Request too large" }, 413);
    }

    let data;
    try {
      data = await request.json();
    } catch {
      return json(origin, { ok: false, error: "Invalid JSON" }, 400);
    }

    if (data.website) {
      return json(origin, { ok: true });
    }

    const name = clean(data.name, 120) || "Не указано";
    const contact = clean(data.contact, 160) || "Не указан";
    const message = clean(data.message, 1500);
    const lang = clean(data.lang, 10) || "unknown";
    const page = clean(data.page, 300);
    const userAgent = clean(data.userAgent, 300);
    const createdAt = clean(data.createdAt, 80) || new Date().toISOString();

    if (message.length < 5) {
      return json(origin, { ok: false, error: "Message too short" }, 400);
    }

    if (!env.TELEGRAM_BOT_TOKEN || !env.TELEGRAM_CHAT_ID) {
      return json(origin, { ok: false, error: "Worker is not configured" }, 500);
    }

    const text =
`Новая заявка с сайта Optima Fide

Имя: ${name}
Контакт: ${contact}
Язык: ${lang}
Время: ${createdAt}

Сообщение:
${message}

Страница: ${page}
Browser: ${userAgent}`;

    const telegramUrl = `https://api.telegram.org/bot${env.TELEGRAM_BOT_TOKEN}/sendMessage`;
    const telegramResponse = await fetch(telegramUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        chat_id: env.TELEGRAM_CHAT_ID,
        text,
        disable_web_page_preview: true
      })
    });

    if (!telegramResponse.ok) {
      console.error(JSON.stringify({ event: "telegram_send_failed", status: telegramResponse.status }));
      return json(origin, { ok: false, error: "Telegram failed" }, 502);
    }

    return json(origin, { ok: true });
  }
};

// Configure secrets in Cloudflare; never commit their values:
// npx wrangler secret put TELEGRAM_BOT_TOKEN
// npx wrangler secret put TELEGRAM_CHAT_ID
