(function () {
  function initRecoveryTree() {
    const section = document.querySelector(".recovery-tree-section");
    if (!section) return;

    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const branches = section.querySelectorAll(".tree-branch");

    branches.forEach((path) => {
      const length = typeof path.getTotalLength === "function" ? path.getTotalLength() : 520;
      path.style.setProperty("--path-length", `${Math.ceil(length)}`);
    });

    section.classList.add("is-ready");

    const showTree = () => {
      section.classList.add("is-visible");
    };

    if (reduceMotion || !("IntersectionObserver" in window)) {
      showTree();
      return;
    }

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        showTree();
        observer.unobserve(section);
      });
    }, {
      threshold: 0.35,
      rootMargin: "0px 0px -10% 0px"
    });

    observer.observe(section);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initRecoveryTree, { once: true });
  } else {
    initRecoveryTree();
  }
})();
