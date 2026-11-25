(function () {
  // 1. Cross-page Dark/Light Ink Theme Sync (shared key: plank_theme)
  var root = document.documentElement;
  var btn = document.getElementById("themeBtn");
  var saved = localStorage.getItem("plank_theme");
  if (saved === "dark") {
    root.setAttribute("data-theme", "dark");
    if (btn) btn.textContent = "素宣 · Paper";
  }
  if (btn) {
    btn.addEventListener("click", function () {
      var isDark = root.getAttribute("data-theme") === "dark";
      if (isDark) {
        root.removeAttribute("data-theme");
        localStorage.setItem("plank_theme", "light");
        btn.textContent = "夜砚 · Ink";
      } else {
        root.setAttribute("data-theme", "dark");
        localStorage.setItem("plank_theme", "dark");
        btn.textContent = "素宣 · Paper";
      }
    });
  }

  // 2. One-click Copy Buttons for Agent Prompts & CLI Commands
  var copyButtons = document.querySelectorAll("[data-copy-target]");
  copyButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      var targetId = button.getAttribute("data-copy-target");
      var pre = document.getElementById(targetId);
      if (!pre) return;
      var text = pre.innerText || pre.textContent || "";
      if (!navigator.clipboard) return;
      navigator.clipboard.writeText(text.trim()).then(function () {
        var orig = button.textContent;
        button.textContent = "已复制 ✓";
        button.classList.add("copied");
        setTimeout(function () {
          button.textContent = orig;
          button.classList.remove("copied");
        }, 1800);
      });
    });
  });

  // 3. Screenshot Lightbox Preview
  var galleryMats = document.querySelectorAll(".gallery-mat[data-full]");
  if (galleryMats.length > 0) {
    var lb = document.createElement("div");
    lb.className = "lightbox";
    lb.setAttribute("role", "dialog");
    lb.setAttribute("aria-modal", "true");
    lb.innerHTML = '<div class="lightbox-inner"><img alt="" /><p class="lightbox-caption"></p></div>';
    document.body.appendChild(lb);

    var lbImg = lb.querySelector("img");
    var lbCap = lb.querySelector(".lightbox-caption");

    function closeLb() {
      lb.classList.remove("open");
    }

    galleryMats.forEach(function (mat) {
      mat.addEventListener("click", function () {
        lbImg.src = mat.getAttribute("data-full");
        lbImg.alt = mat.getAttribute("data-caption") || "";
        lbCap.textContent = mat.getAttribute("data-caption") || "";
        lb.classList.add("open");
      });
    });

    lb.addEventListener("click", closeLb);
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeLb();
    });
  }
})();
