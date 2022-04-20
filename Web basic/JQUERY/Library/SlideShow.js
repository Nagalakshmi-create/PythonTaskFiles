$(document).ready(function() {
    $('#btn').click(function() {
        if($('#btn').text()=='SLIDE UP') {
            $('.image').slideUp(4000, function() {         
                $('#btn').text("SLIDE DOWN");
                
            }); 
        }
        else {
            $('.image').slideDown(4000, function() {         
                $('#btn').text("SLIDE UP");
                
            }); 
        }       
    });

    $('#btn2').click(function() {
        $('.image').slideToggle(3000);
    });
});