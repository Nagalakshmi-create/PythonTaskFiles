$(document).ready(function() {
    $('.hidebtn').click(function() {           //click event on any button  
        $('p.india').hide();                         
    });
    $('#btn1').click(function() {
        $('#mypara').hide();
    });

    $('input[type]').css({'background-color':'yellow',
                          'color':'red',
                          'width':'200px'});
    $('[type="A"]').css({backgroundColor:'deeppink',
                         color:'green',
                         width:'100px'});
});

