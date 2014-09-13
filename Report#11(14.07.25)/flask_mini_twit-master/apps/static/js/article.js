$(document).ready(function () {
    $('#article').bind('input propertychange', function() {
        $('#article-length').text(100-this.value.length);

        if(this.value.length >100){
            $('.mytwit').addClass('disabled');
            $('#article-length').css('color','red');
        } else {
            $('.mytwit').removeClass('disabled');
            $('#article-length').css('color','black');
        }
    });
});