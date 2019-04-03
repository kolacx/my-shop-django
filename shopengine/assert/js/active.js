(function ($) {
    'use strict';

    setTimeout(function() { 
      $('body').removeClass('pre') 
    }, 500);

    var $window = $(window);

    // :: Nav Active Code
    if ($.fn.classyNav) {
        $('#essenceNav').classyNav();
    }

    // :: Sliders Active Code
    if ($.fn.owlCarousel) {
        $('.popular-products-slides').owlCarousel({
            items: 4,
            margin: 30,
            loop: true,
            nav: false,
            dots: false,
            autoplay: true,
            autoplayTimeout: 5000,
            smartSpeed: 1000,
            responsive: {
                0: {
                    items: 1
                },
                576: {
                    items: 2
                },
                768: {
                    items: 3
                },
                992: {
                    items: 4
                }
            }
        });
        $('.product_thumbnail_slides').owlCarousel({
            items: 1,
            margin: 0,
            loop: true,
            nav: true,
            navText: ["<img src='/static/img/core-img/long-arrow-left.svg' alt=''>", "<img src='/static/img/core-img/long-arrow-right.svg' alt=''>"],
            dots: false,
            autoplay: true,
            autoplayTimeout: 5000,
            smartSpeed: 1000
        });
    }

    // :: Header Cart Active Code
    var cartbtn1 = $('#essenceCartBtn');
    var cartOverlay = $(".cart-bg-overlay");
    var cartWrapper = $(".right-side-cart-area");
    var cartbtn2 = $("#rightSideCart");
    var cartOverlayOn = "cart-bg-overlay-on";
    var cartOn = "cart-on";

    cartbtn1.on('click', function () {
        cartOverlay.toggleClass(cartOverlayOn);
        cartWrapper.toggleClass(cartOn);
    });
    cartOverlay.on('click', function () {
        $(this).removeClass(cartOverlayOn);
        cartWrapper.removeClass(cartOn);
    });
    cartbtn2.on('click', function () {
        cartOverlay.removeClass(cartOverlayOn);
        cartWrapper.removeClass(cartOn);
    });

    // :: ScrollUp Active Code
    if ($.fn.scrollUp) {
        $.scrollUp({
            scrollSpeed: 1000,
            easingType: 'easeInOutQuart',
            scrollText: '<i class="fa fa-angle-up" aria-hidden="true"></i>'
        });
    }

    // :: Sticky Active Code
    $window.on('scroll', function () {
        if ($window.scrollTop() > 0) {
            $('.header_area').addClass('sticky');
        } else {
            $('.header_area').removeClass('sticky');
        }
    });

    // :: Nice Select Active Code
    if ($.fn.niceSelect) {
        $('select').niceSelect();
    }

    // :: Slider Range Price Active Code
    $('.slider-range-price').each(function () {
        var min = jQuery(this).data('min');
        var max = jQuery(this).data('max');
        var unit = jQuery(this).data('unit');
        var value_min = jQuery(this).data('value-min');
        var value_max = jQuery(this).data('value-max');
        var label_result = jQuery(this).data('label-result');
        var t = $(this);
        $(this).slider({
            range: true,
            min: min,
            max: max,
            values: [value_min, value_max],
            slide: function (event, ui) {
                var result = label_result + " " + ui.values[0] + ' - ' + ui.values[1] + ' ' + unit;
                console.log(t);
                t.closest('.slider-range').find('.range-price').html(result);
                t.closest('.slider-range').find('#price_min').html(ui.values[0])
                t.closest('.slider-range').find('#price_max').html(ui.values[1])
            }
        });
    });

    // :: Favorite Button Active Code
    var favme = $(".favme");

    favme.on('click', function () {
        $(this).toggleClass('active');
    });

    favme.on('click touchstart', function () {
        $(this).toggleClass('is_animating');
    });

    favme.on('animationend', function () {
        $(this).toggleClass('is_animating');
    });

    // :: Nicescroll Active Code
    if ($.fn.niceScroll) {
        $(".cart-list, .cart-content").niceScroll();
    }

    // :: wow Active Code
    if ($window.width() > 767) {
        new WOW().init();
    }

    // :: Tooltip Active Code
    if ($.fn.tooltip) {
        $('[data-toggle="tooltip"]').tooltip();
    }

    // :: PreventDefault a Click
    $("a[href='#']").on('click', function ($) {
        $.preventDefault();
    });

    console.log('MY JS READY!!!!')

    var warning_ico = '<svg version="1.1" class="warning_ico" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 292.805 292.805" xml:space="preserve"><g><path style="fill:#ff0000" d="M137.583,18.265L1.709,259.709c-4.933,8.767,1.402,19.601,11.462,19.599c57.413-0.01,208.901-0.037,266.469-0.047c10.059-0.002,16.388-10.833,11.454-19.598c-44.565-79.158-135.89-241.399-135.89-241.399C151.62,11.907,141.167,11.907,137.583,18.265z M145.761,248.714c-10.028,0-18.162-8.136-18.162-18.163c0-10.029,8.134-18.165,18.162-18.165c10.03,0,18.165,8.136,18.165,18.165C163.926,240.578,155.791,248.714,145.761,248.714zM160.925,98.708c0.023,0.487,0.02,0.992,0,1.471l-5.05,104.048c-3.149-1.214-6.539-1.948-10.114-1.948c-3.572,0-6.963,0.734-10.112,1.948l-5.05-104.048c-0.402-8.376,6.051-15.493,14.428-15.898C153.403,83.876,160.52,90.332,160.925,98.708z"/></g></svg>';
    var error_mess_1 = '<div class="allert"><span>Заполните это поле</span>' + warning_ico + '</div>'; 
    var error_mess_2 = '<div class="allert"><span>Введите корректный e-mail</span>' + warning_ico + '</div>'; 
    var error_mess_3 = '<div class="allert"><span>Введите корректный номер телефона</span>' + warning_ico + '</div>';

    var timerErrorForm;

    function clearErrorMesForm() {
        clearTimeout(timerErrorForm);
        timerErrorForm = setTimeout(function() {
            jQuery(".field.error").removeClass('error');
            jQuery("input.error").removeClass('error');
            jQuery(".allert").remove();
        }, 5000);
    }

    function scroll_to_element(){
      $([document.documentElement, document.body]).animate({
          scrollTop: $("#shop_scrol").offset().top-80
      }, 2000);
    }

    $('.add_to_b').on('click', function(e){
        var id = $(this).attr("data-id");

        var data = {
            'poduct_id' : id
        };

        $.ajax({
            type: 'GET',
            url: '/add_to_cart/',
            data: data,
            success: function(data){
                $('.cart_total').text(data.cart_total)
                $('.price_all').text(data.total_price + ' грн')
                $('.cart-list').html(data.html)
                console.log(data)
            }
        })

    })

    $( "body" ).delegate( ".product-remove", "click", function(e) {
      e.preventDefault();
      console.log('click remove');
      var id = $(this).attr("data-id");

      var data = {
          'poduct_id' : id
      };

      $.ajax({
          type: 'GET',
          url: '/remove_from_cart/',
          data: data,
          success: function(data){
              $('.cart_total').text(data.cart_total)
              $('.price_all').text(data.total_price + ' грн')
              $('.cart-list').html(data.html)
              console.log(data)
          }
      })
    });

    $('#buy').on('click', function(e){
        e.preventDefault();
        var form = $('#buy_form');
        var error;

        var data = form.serialize();

        var checkedValue = form.find('[required]');

        jQuery(checkedValue).each(function() {
          if (jQuery(this).val() == '') {
            var errorfield = jQuery(this);
            jQuery(this).parent('.field').addClass('error').append(error_mess_1);
            error = 1;
            jQuery(":input.error:first").focus();
            return;
          } else {
            var pattern = /^([a-z0-9_\.-])+@[a-z0-9-]+\.([a-z]{2,4}\.)?[a-z]{2,4}$/i;
            if (jQuery(this).attr("type") == 'email') {
              if (!pattern.test(jQuery(this).val())) {
                jQuery("[name=email]").val('');
                jQuery(this).parent('.field').addClass('error').append(error_mess_2);
                error = 1;
                jQuery(":input.error:first").focus();
              }
            }
            var patterntel = /^([0-9_+\.-]{10,18})/i;
            if (jQuery(this).attr("type") == 'tel') {
              if (!patterntel.test(jQuery(this).val())) {
                jQuery("[name=tel]").val('');
                jQuery(this).parent('.field').addClass('error').append(error_mess_3);
                error = 1;
                jQuery(":input.error:first").focus();
              }
            }
          }
        });
        if (!(error == 1)) {
                $.ajax({
                    type: 'POST',
                    url: '/buy/',
                    data: data,
                    success: function(data){
                        if(data.status =='200'){
                          $('#by_one_click').modal("hide");
                          $('#by_one_click_modal').modal("hide");
                          $('#modal_ok').modal();
                        }
                    }
                })
        } else {
                clearErrorMesForm();
            }
    });
    
    $('#buy_one_click').on('click', function(e){
        e.preventDefault();
        console.log('start');
        var form = $('#buy_one_click_form');
        var error;
        

        var data = form.serialize();

        var checkedValue = form.find('[required]');

        jQuery(checkedValue).each(function() {
          if (jQuery(this).val() == '') {
            var errorfield = jQuery(this);
            jQuery(this).parent('.field').addClass('error').append(error_mess_1);
            error = 1;
            jQuery(":input.error:first").focus();
            return;
          } else {
            var pattern = /^([a-z0-9_\.-])+@[a-z0-9-]+\.([a-z]{2,4}\.)?[a-z]{2,4}$/i;
            if (jQuery(this).attr("type") == 'email') {
              if (!pattern.test(jQuery(this).val())) {
                jQuery("[name=email]").val('');
                jQuery(this).parent('.field').addClass('error').append(error_mess_2);
                error = 1;
                jQuery(":input.error:first").focus();
              }
            }
            var patterntel = /^([0-9_+\.-]{10,18})/i;
            if (jQuery(this).attr("type") == 'tel') {
              if (!patterntel.test(jQuery(this).val())) {
                jQuery("[name=tel]").val('');
                jQuery(this).parent('.field').addClass('error').append(error_mess_3);
                error = 1;
                jQuery(":input.error:first").focus();
              }
            }
          }
        });

        if (!(error == 1)) {
          $.ajax({
              type: 'POST',
              url: '/buy_one_click/',
              data: data,
              success: function(data){
                  if(data.status =='200'){
                    $('#by_one_click').modal("hide");
                    $('#by_one_click_modal').modal("hide");
                    $('#modal_ok').modal();
                  }
              }
          })
        } else {
          clearErrorMesForm();
        }
    });

    $('#by_one_click_one').on('click', function(e){
        e.preventDefault();
        console.log('start');
        var form = $('#by_one_click_one_form');
        var error;

        var data = form.serialize();

        var checkedValue = form.find('[required]');

        jQuery(checkedValue).each(function() {
          console.log('oopa');
          if (jQuery(this).val() == '') {
            var errorfield = jQuery(this);
            jQuery(this).parent('.field').addClass('error').append(error_mess_1);
            error = 1;
            jQuery(":input.error:first").focus();
            return;
          } else {
            var pattern = /^([a-z0-9_\.-])+@[a-z0-9-]+\.([a-z]{2,4}\.)?[a-z]{2,4}$/i;
            if (jQuery(this).attr("type") == 'email') {
              if (!pattern.test(jQuery(this).val())) {
                jQuery("[name=email]").val('');
                jQuery(this).parent('.field').addClass('error').append(error_mess_2);
                error = 1;
                jQuery(":input.error:first").focus();
              }
            }
            var patterntel = /^([0-9_+\.-]{10,18})/i;
            if (jQuery(this).attr("type") == 'tel') {
              if (!patterntel.test(jQuery(this).val())) {
                jQuery("[name=tel]").val('');
                jQuery(this).parent('.field').addClass('error').append(error_mess_3);
                error = 1;
                jQuery(":input.error:first").focus();
              }
            }
          }
        });

        if (!(error == 1)) {
          $.ajax({
              type: 'POST',
              url: '/buy_one_click_one/',
              data: data,
              success: function(data){
                  if(data.status =='200'){
                    $('#by_one_click').modal("hide");
                    $('#by_one_click_modal').modal("hide");
                    $('#modal_ok').modal();
                  }
              }
          })
        } else {
          clearErrorMesForm();
        }
    });

    $('.nice-select li, #filter_go').on('click', function(){

      var data_value = $(this).attr('data-value');
      $('#filter_go').attr('data-value', data_value)

      var a = $('.page-link').href;

      var p_min = $('#price_min').text();      
      var p_max = $('#price_max').text();   

      p_min = +p_min - 1;
      p_max = +p_max + 1;

      console.log(p_min);   
      console.log(p_max);   

      var urlParams = new URLSearchParams(window.location.search);
      var myParam = urlParams.get('page');

      console.log(myParam)

      if (myParam == null){
        myParam = '1'
      }

      var data = {
        'order_by': data_value,
        'ajax': 'True',
        'page': myParam,
        'p_min' : p_min,
        'p_max' : p_max
      }

      $.ajax({
        type: 'GET',
        url: window.location,
        data: data,
        success: function(data){
          // console.log(data.html);
          $('.items_shop').html(data.html);

          if (window.innerWidth < 500) {
            scroll_to_element();
          }
          

        }
      })
    })

})(jQuery);

$(document).ready(function() {


  // window.addEventListener('beforeunload', function (e) {
  //   e.preventDefault();
  //   $('body').addClass('pre')
  // });

        /* =============================================================================
       AJAX
       ========================================================================== */

      $("body").on("click", ".add_product_js", function(){

    /* -----------------------Add animation cart----------------------- */
    var carousel;
        
        if( $(this).hasClass('package_btn') ){
          carousel = $(this).closest(".item");
        }else if( !$(this).hasClass('btn_order') ){
          carousel = $(this).closest(".carousel__item");
        }else{
          carousel = $(".owl-item.active");
        }

           var img = carousel.find('img');
           var position = $(carousel).offset();  
           var widthWindow = $(window).width();
           var wWrap = carousel.width();
           var hWrap = carousel.height();
           if( $(this).hasClass("btn_add_sales_js") ){
              hWrap = false;  
           }
           var posTop = $(carousel).offset().top - $(window).scrollTop();
           var posRight = widthWindow - $(carousel).offset().left - wWrap;
           var idItem = carousel.attr("data-product-id");
         
           $(this).addClass("is-fav");     
           $("body").append('<div class="floating-cart"></div>');      
           var cart = $('div.floating-cart');     
           $(carousel).clone().appendTo(cart);
           $(cart).find('.anim').removeClass('anim').removeClass('fadeInUp');
           $(cart).css({
              'top'       : posTop + 'px', 
              'right'     : posRight + 'px',
              'width'     : wWrap + 'px',
              'height'    : hWrap + 'px',          
           }).fadeIn("slow")
           .addClass('moveToCart');   
           setTimeout(function(){$("body").addClass("MakeFloatingCart").addClass("adding-cart");}, 800);         
           setTimeout(function(){
              $('div.floating-cart').remove();
              $("body").removeClass("MakeFloatingCart").removeClass("adding-cart");
           }, 1000);
           })
});