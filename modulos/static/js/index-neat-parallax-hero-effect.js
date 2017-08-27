var heroShinker = function() {
    var hero = $('.hero-nav'),
        heroHeight = $('.hero-nav').outerHeight(true);
        $(hero).parent().css('padding-top', heroHeight);
    $(window).scroll(function() {
        var scrollOffset = $(window).scrollTop();
        if (scrollOffset < heroHeight) {
            $(hero).css('height', (heroHeight - scrollOffset));
            $('.hero-nav__inner .subtitle').css('display','block');
            $('.icon-scroll').css('display','block');
            $('.icon-scroll-text').css('display','block');
            $('.hero-nav__inner .title').css('margin-bottom','0');
            $('.hero-nav__inner .title').css('margin-top','0');
        }
        if (scrollOffset > (heroHeight - 215)) {
            hero.addClass('fixme');
            $('.hero-nav__inner .subtitle').css('display','none');
            $('.icon-scroll').css('display','none');
            $('.icon-scroll-text').css('display','none');
            $('.hero-nav__inner .title').css('margin-bottom','0.67em');
            $('.hero-nav__inner .title').css('margin-top','0.67em');
        }
        if (scrollOffset > (heroHeight - 300)) {
            hero.addClass('fixme');
            $('.icon-scroll').css('display','none');
            $('.icon-scroll-text').css('display','none');
        }
        else {
            hero.removeClass('fixme');
        };
    });
}
heroShinker();