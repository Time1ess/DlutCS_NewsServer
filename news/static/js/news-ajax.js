$('.news-link').hover(function(){
	$(this).find('#news-container').css('background-color','rgba(0,0,0,0.1)');
},
function(){
	$(this).find('#news-container').css('background-color','rgba(0,0,0,0)');
});