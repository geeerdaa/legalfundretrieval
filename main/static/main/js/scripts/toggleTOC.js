const tocHeader = document.querySelector(".wpj-jtoc--header-main")

tocHeader.addEventListener("click", function () {
    document.querySelector(".wpj-jtoc--body").classList.toggle("hide-toc");
    document.querySelector(".wpj-jtoc--toggle-box").classList.toggle("rotate-toc-box");
  });