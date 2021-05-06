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
        
})(jQuery);