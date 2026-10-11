(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Header: shadow on scroll, active link, burger
  var header = $("#header"), nav = $("#nav"), burger = $(".burger");
  var links = $$("#nav a"), secs = links.map(function (a) { return $(a.getAttribute("href")); });
  var tick = false;
  function onScroll() {
    var y = window.scrollY, hero = $(".hero-bg"), idx = 0;
    header.classList.toggle("scrolled", y > 30);
    secs.forEach(function (s, k) { if (s && s.getBoundingClientRect().top < 140) idx = k; });
    links.forEach(function (a, k) { a.classList.toggle("active", k === idx); });
    if (hero && !reduce && y < window.innerHeight) hero.style.transform = "translate3d(0," + y * 0.25 + "px,0)";
    tick = false;
  }
  window.addEventListener("scroll", function () { if (!tick) { tick = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();

  function setMenu(open) {
    nav.classList.toggle("open", open);
    burger.classList.toggle("open", open);
    burger.setAttribute("aria-expanded", open);
    burger.setAttribute("aria-label", open ? "Закрити меню" : "Відкрити меню");
  }
  burger.addEventListener("click", function () { setMenu(!nav.classList.contains("open")); });
  $$('a[href^="#"]').forEach(function (a) {
    a.addEventListener("click", function (e) {
      var t = $(a.getAttribute("href"));
      if (!t) return;
      e.preventDefault(); setMenu(false);
      t.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });

  // Reveal on scroll
  var rev = $$(".reveal");
  if (reduce || !("IntersectionObserver" in window)) {
    rev.forEach(function (el) { el.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    rev.forEach(function (el) { io.observe(el); });
  }

  // Lightbox
  var lb = $("#lightbox"), img = $("img", lb), cap = $("figcaption", lb);
  var shots = $$("[data-lb]"), cur = null;
  function show(i) {
    cur = (i + shots.length) % shots.length;
    var im = $("img", shots[cur]);
    img.src = im.getAttribute("src"); img.alt = im.alt; cap.textContent = im.alt;
  }
  function open(i) { show(i); lb.classList.add("open"); lb.setAttribute("aria-hidden", "false"); document.body.style.overflow = "hidden"; }
  function close() { cur = null; lb.classList.remove("open"); lb.setAttribute("aria-hidden", "true"); document.body.style.overflow = ""; }
  shots.forEach(function (b, i) { b.addEventListener("click", function () { open(i); }); });
  $(".lb-x", lb).addEventListener("click", close);
  $(".lb-p", lb).addEventListener("click", function () { show(cur - 1); });
  $(".lb-nx", lb).addEventListener("click", function () { show(cur + 1); });
  lb.addEventListener("click", function (e) { if (e.target === lb) close(); });
  window.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { setMenu(false); if (cur !== null) close(); }
    if (cur === null) return;
    if (e.key === "ArrowLeft") show(cur - 1);
    if (e.key === "ArrowRight") show(cur + 1);
  });
})();
