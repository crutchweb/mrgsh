$( document ).ready(function() {
    //col width
    $('.col').hover(
        function() {
            $(this).addClass('active');
            $('.col').not(this).addClass('not-active');
            if ($(this).data('shadow') == 'active') {
                $('.sidebar__centerline').addClass('shadow');
            }
        }, function() {
            $(this).removeClass('active');
            $('.col').not(this).removeClass('not-active');
            $('.sidebar__centerline').removeClass('shadow');
    });

    //nav
    $('.navigation li.sub__menu > a').on('click', function (e) {
        e.preventDefault();
        $('.navigation li a').not(this).closest('li').find('.menu__children').slideUp();
        $(this).toggleClass('active');
        $(this).closest('li').find('.menu__children').slideToggle();
        $('.navigation li a').not(this).removeClass('active');
    })

    // owl
    $('.news__carousel').owlCarousel({
        loop:true,
        margin:10,
        nav:false,
        items:1,
        autoplay:true,
        autoplayTimeout:4000,
        autoplayHoverPause:true
    });

    var owl = $('.news__carousel');

    //owl custom prev/next btn
    $('.widget__href .owl__next').click(function() {
        owl.trigger('next.owl.carousel');
    });
    // Go to the previous item
    $('.widget__href .owl__prev').click(function() {
        owl.trigger('prev.owl.carousel');
    });

    if ($('.img__carousel a').length >= 4){
        var loop = true
    }else{
        var loop = false
        $('.additional__img').css('padding', '0 10px')
        $('.additional__img .owl__prev').hide();
        $('.additional__img .owl__next').hide();
    }

    $('.img__carousel').owlCarousel({
        loop:loop,
        margin:10,
        nav:false,
        items:4,
        dots:false
    });

    var owl2 = $('.img__carousel');

    //owl custom prev/next btn
    $('.additional__img .owl__next').click(function() {
        owl2.trigger('next.owl.carousel');
    });
    // Go to the previous item
    $('.additional__img .owl__prev').click(function() {
        owl2.trigger('prev.owl.carousel');
    });

    //height left side
    var h = $('.content__breadcrumbs').height() + $('.content__title').height();
    var h = 'calc(100vh - ' + h + 'px)';
    $('.left__side').css('min-height', h)

});