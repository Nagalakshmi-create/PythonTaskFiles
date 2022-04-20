let array=document.getElementsByTagName('p');  // <p>
for (let ele of array) {
    console.log(ele);
    document.write(ele);
}
let array2=document.getElementsByClassName('heading');  // class 'heading'
for (let ele of array) {
    console.log(ele);
    document.write(ele);
}
let ele=document.getElementById('mypara1');  // id="mypara1"
console.log(ele);
document.write(ele);

let array3=document.getElementsByName('course');  //name="course"
for (let ele of array3) {
    console.log(ele);
    document.write(ele);
}
function showState() {
    console.log("---elements which are checked---");
    for (let ele of array3) {
        if(ele.checked) {    //checked:attribute
            console.log(ele);
        }
    }       
}

function extract() {
    console.log("Blur Event occured...");
    let passNode=document.getElementById("pass");
    let password=passNode.value;
    console.log(password);
}
let checkNode=document.getElementById("showp");
checkNode.addEventListener('change', ()=>showPassword());
let passNode=document.getElementById("pass");
passNode.style.backgroundColor="brown";  //it overrides CSS
function showPassword() {
    
    if (checkNode.checked)
        passNode.type="text";
    else 
        passNode.type="password";
}
function changeStyle() {
    passNode.style.backgroundColor="yellow";
    passNode.style.border='6px double purple'
}


let imgNode=document.getElementById("lataImage");
let changeImage=function() {
    imgNode.src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.amarujala.com%2Findia-news%2Fknow-how-lata-mangeshkar-political-journey-was-and-from-politicians-to-actors-paid-tribute&psig=AOvVaw0Tt2p4jDFgp4bgfCl5_4MC&ust=1644305146721000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi-uJOI7fUCFQAAAAAdAAAAABAD";
}
bwidth=3;
imgNode.style.borderWidth=bwidth+'px';
function zoomIn() {
    imgNode.height=imgNode.height+10;
    imgNode.width=imgNode.width+10;
    bwidth=bwidth+1;
    imgNode.style.borderWidth=bwidth+'px'
}
