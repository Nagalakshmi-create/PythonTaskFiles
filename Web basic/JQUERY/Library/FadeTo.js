$(document).ready(function() {
    $('button').click(function() {         //event method
        $('p,img').fadeTo(5000,0.5);       //timer, opacity
    });
    $('#animate').click(function() {
        $('p,img').animate({'width':'500px', 'opacity':'0.1', 'background-color':'yellow'},3000, function() {
            $('#animate').val('ANIMATE DONE');     //let node=document.getElementById('#animate) node.value="jhjh"
        });
    });
});

//animate applies the animation on numeric css properties/ js properties with effect
//css applies the style using any css property(numeric/non numeric)