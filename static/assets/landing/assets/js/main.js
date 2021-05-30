(function($) {
	"use strict";

    $("#status").fadeOut(), $("#preloader").delay(350).fadeOut("slow"), $("body").delay(350).css({
        overflow: "visible"
    })

    /* ==================================================
            # Clients Carousel
         ===============================================*/
         $('.clients-items').owlCarousel({
            loop: false,
            nav: false,
            dots: true,
            autoplay: true,
            responsive: {
                0: {
                    items: 2
                },
                600: {
                    items: 3
                },
                1000: {
                    items: 7
                }
            }
        });

        /* ==================================================
            # Magnific Popup
         ===============================================*/
         $('.gallery').each(function() {
            $(this).magnificPopup({
                delegate: 'a',
                type: 'image',
                removalDelay: 300,
                mainClass: 'mfp-fade',
                gallery: {
                  enabled:true
                }
            });
        });
        
    /* ==================================================
            # init Isotope
     ===============================================*/
    var $grid = $('.project-items .row').isotope({
        // options
    });
    // filter items on button click
    $('.item-menu').on( 'click', 'li', function() {
        var filterValue = $(this).attr('data-filter');
        $grid.isotope({ filter: filterValue });
    });

    $('.item-menu').each( function( i, buttonGroup ) {
        var $buttonGroup = $( buttonGroup );
        $buttonGroup.on( 'click', 'li', function() {
          $buttonGroup.find('.active').removeClass('active');
          $( this ).addClass('active');
        });
      });

      /* ==================================================
            # WOW init
     ===============================================*/
      new WOW().init();

      /* ==================================================
            # slick
     ===============================================*/
     $(".news").slick({
        dots: true,
        infinite: true,
        variableWidth: true
      });

      /*================================
			ScrollUp JS
		==================================*/
        var offset = $(window).height();
        var duration = 500;
        $(window).scroll(function() {
            if (jQuery(this).scrollTop() > offset) {
                $('#scrollUp').fadeIn(duration);
            } else {
                $('#scrollUp').fadeOut(duration);
            }
        });

        $("body").on("click", "#scrollUp", function(e) {
            e.preventDefault();
            $("html,body").animate({ scrollTop: 0 }, "slow");
        });
})(jQuery);