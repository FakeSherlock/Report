$(document).ready(function() {

	// 문서의 로딩이 끝나면, 이라는 뜻입니다. 잊지 않으셨죠?
    // 이곳에 코드를 작성하시면 됩니다.

    $('#shadow').dblclick(function(){
    	$(this).fadeOut('slow');
    	/*note1. this는 바로 위의 변수를 참조하는 것!*/
    });

     function rgb2hex(rgb) {
      if (  rgb.search("rgb") == -1 ) {
         return rgb;
      } else {
         rgb = rgb.match(/^rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*(\d+))?\)$/);
         function hex(x) {
            return ("0" + parseInt(x).toString(16)).slice(-2);
         }
         return "#" + hex(rgb[1]) + hex(rgb[2]) + hex(rgb[3]); 
      }
   }

    $('#car').dblclick(function(){

        var car_color = rgb2hex($('#top').css("backgroundColor"));

        if(car_color == "#ff4444"){
         $('#top').css("background","#99cc00");
         $('#bottom').css("background","#99cc00");
      }
      else if(car_color == "#99cc00"){
         $('#top').css("background","#ff4444");
         $('#bottom').css("background","#ff4444");
      }
        
    });

    //$('#car').mouseenter(function(){
    	//$('#shadow').fadeTo(/*옅어지게만드는 법*/'slow',0.25/*속도,최종값*/)
    //});

    //$('#car').mouseleave(function(){
    	//$('#shadow').fadeTo('slow',1)
    //});

    $('#button_right').click(function(){
    	$('#car').animate({left:"+=500px"},'slow'/*방향,속도*/);
    });

    $('#button_left').click(function(){
    	$('#car').animate({left:"-=500px"},'slow'/*방향,속도*/);
    });

    $('#button_up').click(function(){
    	$('#car').animate({top:"-=500px"},'slow'/*방향,속도*/);
    });

    $('#button_down').click(function(){
    	$('#car').animate({top:"+=500px"},'slow'/*방향,속도*/);
    });

    $(document/*문서 전체를 범위로 설정*/).keydown/*키를 눌렀을때*/(function(key/*크롬 브라우져로 전송되는 키를 의미*/) {
        switch(parseInt(key.which,10)) {
        	/*조건문(정수로 바꾼다(key.which,10)*/
			// 왼쪽 방향키
			case 37:
				$('#car').animate({left:"-=500px"},'slow'/*방향,속도*/);
				break;
				/*브레이크는 나머지를 무시하는 것*/
			// 위쪽 방향키
			case 38:
				// 코드를 입력하세요.
				$('#car').animate({top:"-=500px"},'slow');
				break;
			// 오른쪽 방향키
			case 39:
				// 코드를 입력하세요.
				$('#car').animate({left:"+=500px"},'slow');
				break;
			// 아래 방향키
			case 40:
				// 코드를 입력하세요.
				$('#car').animate({top:"+=500px"},'slow');
				break;
		}
	});
});