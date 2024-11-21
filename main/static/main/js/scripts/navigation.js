var body = $("body"),
  _window = $(window);
// for menu
$(".btn-menu").on("click", function (e) {
  e.preventDefault();
  if (!body.hasClass("init-for-menu")) {
    body.addClass("overflow-hidden");
    body.css("width", body.width());
    body.removeClass("overflow-hidden");
    body.addClass("init-for-menu");
  }
  // else {
  //     body.removeClass('init-for-menu');
  //     body.css('width','');
  // }
  body.toggleClass("menu-active");
  $(this).toggleClass("active");
});

body.on("click", ".for-menu .has-children > a", function (e) {
  var _this = $(this);
  if (
    _this.attr("href") === undefined ||
    e.pageX >=
      _this.offset().left +
        _this.width() +
        parseFloat(_this.css("padding-left")) +
        parseFloat(_this.css("padding-right")) -
        45
  ) {
    e.preventDefault();
    _this.parent().toggleClass("active");
  }
});

var slick = $(".slick-slider");
if (slick.length > 0) {
  slick.each(function () {
    $(this).slick({
      dots: true,
    });
  });
}
// for header
      var header = $("header");
      _window.on("scroll", function () {
        var scrollTop = _window.scrollTop();
        if (scrollTop > 0) {
          header.addClass("with-bg");
        } else {
          header.removeClass("with-bg");
        }
      });
      $(this).scrollTop(0);