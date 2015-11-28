
$('.navbar-toggle').click(function(){
    /*$('#navbar').slideToggle();*/
    $('.main-content').toggleClass('sidebar-menu-is-open');
    $('header').toggleClass('sidebar-menu-is-open');
    $('#sidebar-nav').toggleClass('sidebar-menu-is-open');
});


<!-- Scrolled header -->
$(window).scroll(function () {
    if ($(window).scrollTop() >= 300) {
        $('header').addClass('header-is-scrolled');
        $('.header-bars-wrapper').addClass('is-scrolled');
    }
    else {
        $('header').removeClass('header-is-scrolled');
        $('.header-bars-wrapper').removeClass('is-scrolled');
    }
});

<!-- Custom ADF Widget JS  =============================-->
$(document).ready(function () {
    $(".adf-blackbox ").hide();
    $(".adf-mbox .collect").hide();
    $(".adf-modalbox").hover(
        function () {
            $(".adf-main").fadeToggle("slow", "swing");
            $(".adf-blackbox").fadeToggle("slow", "swing", function () {
                $(".adf-mbox .collect").slideToggle("fast", "swing");

            });
        }, function () {
            $(".adf-mbox .collect").slideToggle("fast", "swing", function () {
                $(".adf-blackbox").fadeToggle("slow", "swing");
                $(".adf-main").fadeToggle("slow", "swing");

            });

        });


    $(".adf-modalbox").click(function () {
        // add js code for for when user clicks on widget here
    });
});


<!-- Jquery mask for phone input -->
$(document).ready(function () {
    $('#id_phone').mask('000-000-0000');
});
