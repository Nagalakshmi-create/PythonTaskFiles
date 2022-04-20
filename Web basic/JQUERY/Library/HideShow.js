$(document).ready(function() {
    $('#btn').click(function() {
        if($('#btn').text()=='HIDE') {
            $('.myimage').hide(6000, function() {         //hide: decrease dimensions and then remove elemnet
                $('#btn').text("SHOW");
                
            }); 
        }
        else {
            $('.myimage').show(4000, function() {         //show: add the element along with increase dimensions
                $('#btn').text("HIDE");
                
            }); 
        }       
    });

    $('#btn2').click(function() {
        $('.myimage').toggle(1000);
    });
});