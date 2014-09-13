$(document).keydown(function (key) {
    if (parseInt(key.which, 10) == 13) {
        if ($('#msg').val().length != 0) {
            var msg = $('#msg').val();
            var id = $('#userid').val();

            $.get("/send", {
                id: id,
                msg_data: msg
            }, function (data) {
            });

            $('#msg').val(null);
        }
    }
});