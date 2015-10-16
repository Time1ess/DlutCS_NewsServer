$('.news-link').hover(function(){
	$(this).find('#news-container').css('background-color','rgba(0,0,0,0.1)');
},
function(){
	$(this).find('#news-container').css('background-color','rgba(0,0,0,0)');
});
var current_page=1;
var COMMENTS_PER_PAGE=5;// shoudl be odd,but do not change this value 
var MAX_PAGE_PER_LINE=3;// should be odd
var comments_list=$('#comments_list');
var comments_count=comments_list.attr('data-count');
var PAGE_NUM=Math.ceil(comments_count/COMMENTS_PER_PAGE);

$(function(){
	$('.comment_content').hide();
	var next_page=$('#comments_page_next');

	next_page.before('<li id="page'+1+'" class="active"><a onclick="comments_page_change(1)"><strong>1</strong></a></li>');
	for(var i=2;i<=PAGE_NUM;i++)
	{
		next_page.before('<li id="page'+i+'"><a onclick="comments_page_change('+i+')"><strong>'+i+'</strong></a></li>');
		if(i>MAX_PAGE_PER_LINE)
			$('#page'+i).hide();
	}

})

function comments_page_change(page)
{
	if(page==current_page)
		return false;
	if(page=='previous')
	{
		if(current_page==1)
			return false;
		page=current_page-1;
	}
	else if(page=='next')
	{
		if(current_page==PAGE_NUM)
			return false;
		page=current_page+1;
	}
	else if(page=='first')
	{
		page=1;
	}
	else if(page=='last')
	{
		page=PAGE_NUM;
	}
	$('#page'+current_page).removeClass('active');
	$('#page'+current_page).addClass('disable');
	$('#page'+page).removeClass('disable');
	$('#page'+page).addClass('active');
	var startPage=current_page-Math.floor(MAX_PAGE_PER_LINE/2);
	startPage=startPage>0?startPage:1;
	var endPage=startPage+MAX_PAGE_PER_LINE-1;
	endPage=endPage>PAGE_NUM?PAGE_NUM:endPage;
	for(var i=startPage;i<=endPage;i++)
		$('#page'+i).hide();

	startPage=page-Math.floor(MAX_PAGE_PER_LINE/2); 
	endPage=page+Math.floor(MAX_PAGE_PER_LINE/2);  
	if(endPage>PAGE_NUM&&startPage>=1)
	{
		//alert('cut tail')
		var tmpStartPage=startPage-(endPage-PAGE_NUM);
		startPage=tmpStartPage>0?tmpStartPage:1;
	}
	else if(endPage<=PAGE_NUM&&startPage<1)
	{
		//alert('cut head');
		var tmpEndPage=endPage+(1-startPage);
		endPage=tmpEndPage<=PAGE_NUM?tmpEndPage:PAGE_NUM;
	}
	else if(endPage>PAGE_NUM&&startPage<1)
	{
		//alert('both cut');
		endPage=PAGE_NUM;
		startPage=1;
	}
	for(var i=startPage;i<=endPage;i++)
		$('#page'+i).show();
	// for(var i=max_message_per_page*(current_page-1)+1,j=max_message_per_page*(page-1)+1;i<=current_page*max_message_per_page;i++,j++)
	// {
	// 	var no='#messageNo'+i;
	// 	$(no).hide();
	// 	no='#messageNo'+j;
	// 	$(no).show();
	// }
	current_page=page;
	return true;
}

function comment(id)
{	
	var comment=$('#comment_content_'+id);
	var isshow=comment.is(':visible');
	$('.comment_content').hide();
	var no_comments=$('#no_comments');
	if(isshow)
	{
		comment.hide();
		no_comments.fadeIn(250);
		$('#create_a_comment_'+id).html(id==0?'发表评论':'<span class="glyphicon glyphicon-share"></span> 回复');
	}
	else
	{
		no_comments.hide();
		comment.fadeIn(250);
		$('#create_a_comment_'+id).html(id==0?'取消评论':'<span class="glyphicon glyphicon-remove"></span> 取消');
	}
}
function GetCharLength(str) 
{ 
	var iLength = 0; 
	for(var i = 0;i<str.length;i++) 
	{ 
		if(str.charCodeAt(i) >255) 
		{ 
			iLength += 2; 
		} 
		else 
		{ 
			iLength += 1; 
		} 
	} 
	return iLength; 
}
function checkReplyContent(id)
{
	var content_length=GetCharLength($('#comment_input_'+id).val());
	$('#charslabel_'+id).show();
	var counts=120-content_length;
	if(counts>=0)
		$('#charslabel_'+id).html("还可以输入<span style=\"color:green\">"+counts+"</span>字符");
	else
		$('#charslabel_'+id).html("<span style=\"color:red;\">输入字数超过限制！</span>");
}

function submitComment(id)
{
	var content=$("#comment_input_"+id).val();
	alert(content);
	//first to check the content is legal
}

function voteup(id)
{
	alert(id);
}