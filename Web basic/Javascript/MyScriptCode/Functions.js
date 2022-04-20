function makeAddition() {
    var num1=67;
    var num2=90.5;
    var result=num1+num2;
    console.log("Addition is : "+result);
}
makeAddition() ;
function multiply(num1, num2) {
    return num1*num2;
}

var res=multiply(56, 4);
console.log("Multiplication is: "+res);

var v1=56;
var v2=67;
var v1=7788;  //can redeclare
v2=343;  //cannot redeclare

function test() {
    for(var i=1;i<=5;i++) {
        console.log("i = "+i);
    }  //for ended
    console.log("outside of for i= "+i); //var type variable always have functional scope though we define then anywhere in the function

    for(let j=1;j<=5;j++) {
        console.log("j = "+j);
    } //for ended
    //console.log("ouside of for j= "+j);  // let type variable always have blockj scope where they are declared
}
//console.log("outside of function i= "+i);
test();
const divide=function(num1, num2) {
    return num1/num2;
}
console.log("Division is: "+divide(67, 3));

function setLoop() {
    let k=1;
    let interval=setInterval(function() {
        document.write("<b>"+k+" <b>");
        k++;
        if(k>5) {
            clearInterval(interval);
            document.write("DONE")
        }
    }, 3000);
}
setLoop();

const arrowfun1=()=> {
    var no1=67, no2=78;
    let res=no1+no2;
    console.log(res);
}
arrowfun1();

//if body of arrow function contains single stmt then {} are optional
const arrowfun2=(no1, no2)=>console.log(no1+no2);
arrowfun2(33,22);
//if body or arrow function contains single returns stmt then no {}, no return keyword
//if arrows function take single argument then () are optional
const cubeFun=num=> num*num*num   //num**3
res=cubeFun(3);
console.log(res);