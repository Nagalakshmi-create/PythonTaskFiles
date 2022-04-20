$(document).ready(function() {
    $('#btn').click(function() {
        if($('#btn').text()=='FADE OUT') {
            $('.image').fadeOut(6000, function() {         
                $('#btn').text("FADE IN");
                
            }); 
        }
        else {
            $('.image').fadeIn(4000, function() {         
                $('#btn').text("FADE OUT");
                
            }); 
        }       
    });

    $('#btn2').click(function() {
        $('.image').fadeToggle(3000);
    });
});