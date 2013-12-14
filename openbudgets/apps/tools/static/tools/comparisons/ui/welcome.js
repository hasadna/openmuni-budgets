define([
	'jquery'
],function ($) { 
    $(".galleryItem").mouseenter(function() {
      var thisoverlay = $(this).find('.galleryOverlay');
      
      thisoverlay.stop(true, true).animate({
        height: '200',
        marginTop: '-220px'
      });
    });

    $(".galleryItem").mouseleave(function() {
      var thisoverlay = $(this).find('.galleryOverlay');
      
      thisoverlay.stop(true, true).animate({
        height: '30',
        marginTop: '-50px'
      });
    });
});