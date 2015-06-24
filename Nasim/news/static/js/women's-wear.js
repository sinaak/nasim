$('.navigation_02 li:has("ul") > a').on('click', function (e) {
    var $this = $(this);
    $('.navigation_02 a.active').not($this).removeClass('active').next().stop(true, true).slideUp('slow');
    $this.addClass('active').next().stop(true, true).slideToggle('slow');
});