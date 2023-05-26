$(document).ready(function() {

    $(".minimalist-vertical-menu").on("mouseleave", function() {
      $(".minimalist-tab-content").removeClass("active");
      $(".minimalist-tab-menu>.list-group>li").removeClass("active");
    });
                                                    
    $("li").on( "mouseleave", function() {
       if(!$(".minimalist-tab-content").hasClass("active")) {
        $(this).removeClass("active");
      }
      
    }).on( "mouseenter", function(e) {
      e.preventDefault();
      $(this)
        .siblings("li.active")
        .removeClass("active");
      $(this).addClass("active");
      var index = $(this).index();
      $(".minimalist-tab-content")
        .removeClass("active")
      $(".minimalist-tab>.minimalist-tab-content")
        .eq(index)
        .addClass("active");
    });
  });
  