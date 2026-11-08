// Frances Okeke — small, progressive enhancements. The site works without this file.
document.documentElement.classList.remove("no-js");

// Mobile menu: open/close with button, close on Escape (user control)
(function () {
  const btn = document.querySelector(".menu-btn");
  const nav = document.getElementById("site-nav");
  if (!btn || !nav) return;
  function set(open) {
    nav.classList.toggle("open", open);
    btn.setAttribute("aria-expanded", String(open));
    btn.querySelector("span").textContent = open ? "Close" : "Menu";
  }
  btn.addEventListener("click", () => set(btn.getAttribute("aria-expanded") !== "true"));
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && btn.getAttribute("aria-expanded") === "true") { set(false); btn.focus(); }
  });
})();

// Topic filters on list pages (flexibility; empty state that helps)
(function () {
  const chips = document.querySelectorAll(".chip");
  const items = document.querySelectorAll("[data-topics]");
  const count = document.querySelector(".result-count");
  const empty = document.querySelector(".empty");
  if (!chips.length) return;
  function apply(topic) {
    let shown = 0;
    items.forEach((it) => {
      const match = topic === "all" || it.dataset.topics.split(" ").includes(topic);
      it.hidden = !match;
      if (match) shown++;
    });
    chips.forEach((c) => c.setAttribute("aria-pressed", String(c.dataset.topic === topic)));
    const chip = [...chips].find((c) => c.dataset.topic === topic);
    const label = topic === "all" ? "all journeys" : chip.textContent.toLowerCase();
    if (count) count.textContent = `Showing ${shown} ${shown === 1 ? "piece" : "pieces"} on ${label}.`;
    if (empty) {
      empty.hidden = shown !== 0;
      const t = empty.querySelector(".empty-topic");
      if (t) t.textContent = label;
    }
    if (history.replaceState) history.replaceState(null, "", topic === "all" ? location.pathname : "#" + topic);
  }
  chips.forEach((c) => c.addEventListener("click", () => apply(c.dataset.topic)));
  const reset = document.querySelector(".empty button");
  if (reset) reset.addEventListener("click", () => { apply("all"); chips[0].focus(); });
  const start = location.hash.slice(1);
  apply([...chips].some((c) => c.dataset.topic === start) ? start : "all");
})();

// Reading progress bar on articles (visibility of system status)
(function () {
  const bar = document.querySelector(".progress");
  const article = document.querySelector(".article");
  if (!bar || !article) return;
  function update() {
    const rect = article.getBoundingClientRect();
    const total = rect.height - window.innerHeight;
    const done = Math.min(1, Math.max(0, -rect.top / (total > 0 ? total : 1)));
    bar.style.width = (done * 100).toFixed(1) + "%";
  }
  window.addEventListener("scroll", update, { passive: true });
  update();
})();

// Copy email: confirms what happened instead of a mailto link that may silently fail
(function () {
  const btn = document.querySelector("[data-copy]");
  const status = document.querySelector(".copy-status");
  if (!btn) return;
  btn.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(btn.dataset.copy);
      status.textContent = "Email address copied.";
    } catch (e) {
      status.textContent = "Couldn't copy automatically. The address is " + btn.dataset.copy;
    }
  });
})();
