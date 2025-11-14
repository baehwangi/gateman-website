
jQuery(function($){
	/* scroll */
	$(document).ready(function(){  
		$(".kso-scroll").click(function(event){  
			//prevent the default action for the click event  
			event.preventDefault();  
			//get the full url - like mysitecom/index.htm#home  
			var full_url = this.href;  			  
			//split the url by # and get the anchor target name - home in mysitecom/index.htm#home  
			var parts = full_url.split("#");  
			var trgt = parts[1];  			   
			//get the top offset of the target anchor  
			var target_offset = $("#"+trgt).offset();  
			var target_top = target_offset.top;  			  
			//goto that anchor by setting the body scroll top to anchor top  
			$('html, body').animate({scrollTop:target_top}, 1000);  
		});  	
	}); 

	// nav hover
	$('.navbar ul.nav>li.dropdown').hover(
		function(){$(this).children('ul').stop(true,true).hide().fadeIn(100);},
		function(){$(this).children('ul').stop(true,true).fadeOut(100);}
	);
	$('.navbar ul.nav>li.dropdown li.dropdown').hover(
		function(){$(this).children('ul').stop(true,true).hide().fadeIn(100);},
		function(){$(this).children('ul').stop(true,true).fadeOut(100);}
	);

	$(document).ready(function($) {
		$('nav#xs-menu').mmenu({
			slidingSubmenus: false,
			extensions	: [ 'effect-slide-menu','pageshadow','theme-dark' ]
		});
	});

});

(function($){

	// Sticky header one
	$(function(){
		var shrinkHeaders = 700;
		$(window).scroll(function() {
			var scroll = getCurrentScroll();
			if ( scroll >= shrinkHeaders ) {
				$('.nav-mini').addClass('show');
			}
			else {
				$('.nav-mini').removeClass('show');
			}
		});
		function getCurrentScroll() {
			return window.pageYOffset || document.documentElement.scrollTop;
		}
	});

	$(document).ready(function(){  
		$(".inner-link").click(function(event){  
			event.preventDefault();  
			var full_url = this.href;  			  
			var parts = full_url.split("#");  
			var trgt = parts[1];  			   
			var target_offset = $("#"+trgt).offset();  
			var target_top = target_offset.top;  			  
			$('html, body').animate({scrollTop:target_top}, 1000, 'easeInOutCirc');  
		});  
	}); 
	
})(jQuery);

// float menu
(function($){
	$(function(){
	  var menu_head = $('ul.float-menu h2.title').height();
	  var item_height = $('ul.float-menu li a').height();
	  // Untoggle menu on click outside of it
	    $(document).mouseup(function (e) {
	      var container = $('ul.float-menu');
	      if ((!container.is(e.target) && container.has(e.target).length === 0) && 
	         (!($('a.kso-opener').is(e.target)) && $('a.kso-opener').has(e.target).length === 0)) {
	        container.removeClass("in");
	        $('body, ul.float-menu').removeClass("open");
			$('a.kso-opener').removeClass('navtoggleon'); //
	      	$('ul.float-menu li').css("top", "100%");
		      $('ul.float-menu h2').css("top", "-60px");
	      }
	    });
	    
	    $("a.kso-opener").click(function(e) {	
	      e.preventDefault();
	      if ($('ul.float-menu, body').hasClass('open')) {
	      	$('ul.float-menu').removeClass('open');
	      	$('body').removeClass('open');
		$('a.kso-opener').removeClass('navtoggleon');

	      	// Reset menu on close
	      	$('ul.float-menu li').css("top", "100%");
		    $('ul.float-menu h2').css("top", "-60px");
	      } else {
			$("a.kso-opener").addClass("navtoggleon"); //
		      $('ul.float-menu').addClass('open');
		      $('body').addClass('open');

		      $('ul.float-menu h2').css("top", 0);
		      $('ul.float-menu li').each(function() {
		      	// Traditional Effect
		      	if ($(this).hasClass('float-link')) {
		      		var i = ($(this).index() - 1)
			      	var fromTop = menu_head + (i * item_height);
			      	var delayTime = 100 * i;
			      	$(this).delay(delayTime).queue(function(){
				        $(this).css("top", fromTop);
				        $(this).dequeue();
				    	});
		      	}
		      	// Metro Effect
		      	else if ($(this).hasClass('metro')) {
		      		var row_i = ($(this).parent().parent().index() - 1); // Vertical Index
		      		var col_i = $(this).index(); // Horizontal Index
		      		var fromTop = menu_head + (row_i * 125);
							var fromLeft = col_i * 125;
							var delayTime = (row_i * 200) + Math.floor((Math.random() * 200) + 1);
							console.log(delayTime);
				      $(this).css("left", fromLeft);
							$(this).delay(delayTime).queue(function(){
				      	$(this).css("top", fromTop);
				        $(this).dequeue();
				    	});
		      	}
		      });
	      }

	    })
	}); 
})(jQuery); 