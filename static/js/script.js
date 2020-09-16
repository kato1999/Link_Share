//スマホの時だけ電話番号有効化
//スムーススクロール

$(function(){
	$('a[href^="#"]').click(function(){
		var speed = 500;
		var href= $(this).attr("href");
		var target = $(href == "#" || href == "" ? 'html' : href);
		var position = target.offset().top;
		$("html, body").animate({scrollTop:position}, speed, "swing");
		return false;
	});
});

/***************** MENU ******************/

$(function() {
  $(".navbar-toggle").click(function() {
    $("#gnavi").slideToggle(200);
    $(".icon-bar").toggleClass("closeup");
    return false;
  });
});

//スマホのメニューをタップしたら閉じる

$(document).ready(function () {
 $(".navbar-nav li a").click(function(event) {
 $(".navbar-collapse").removeClass('show');
 });
});