$(document).ready(function() {
    function translateHello() {
        let langCode = $('#language_code').val();
        $.get('https://hellosalut.stefanbohacek.dev/?lang=' + langCode, function(data) {
            $('#hello').text(data.hello);
        });
    }

    $('#btn_translate').click(translateHello);
    
    $('#language_code').keypress(function(e) {
        if (e.which == 13) {
            translateHello();
        }
    });
});
