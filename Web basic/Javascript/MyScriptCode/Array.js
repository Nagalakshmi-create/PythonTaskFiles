let s1="Neosoft Technologies";
let s2=new String("Squad Infotech");

const len=s1.length;
console.log(len);
console.log(s1.charAt(4));
console.log(s1.indexOf('o'));  //lastIndexOf
let up=s1.toUpperCase();  //changes stored in new object
console.log(up);
console.log(s1);   //immutable
console.log(s1.toLowerCase());
console.log((s1));

//substring, substr, slice

console.log(s1.substring(2,8));
console.log(s1.substring(2));
console.log(s1.substring(-5)); //replace -ve value to 0
console.log(s1.substring(-5,9)); //replace -ve value to 0
console.log(s1.substring(-5,-9)); //replace -ve value to 0
console.log("--------------------");

console.log(s1.slice(2,8));
console.log(s1.slice(2));
console.log(s1.slice(-5)); 
console.log(s1.slice(-5,9)); 
console.log(s1.slice(-9,-5)); 
console.log(s1.slice(12,2));  //empty
console.log("--------------------");
console.log(s1.substr(2,8));  //setInterval, length
console.log(s1.substr(-10,3));  //si, length


let array1=[56000,12345,78000,90000,670000,890000,560000];
console.log(array1);
array1.push(45999);
console.log(array1);
let array2=['dffg',56688,true];
console.log(array2);
let array4=new Array();
console.log(array4.length);
array4.push('pune');
console.log(array4.length);
let array5=new Array(3);
console.log(array5);
console.log(array5.length);
array5[0]='solapur';
array5[1]='Thane';
array5[2]='Satara';
array5.push('Mumbai');   //extra element added
console.log(array5);
let array6=new Array(3,5,67,34,11,23);
console.log(array6);
console.log(array6.length);
array6.push(10);  //adds the element from back of array
console.log(array6);
let num=array6.pop();  //removes the element from back of the array
console.log(num+" popped from array");
console.log(array6);
array6.unshift(34);  //adds the element from start of the array
console.log(array6);
array6.shift(34);  //removes the element from start of the array
console.log(array6);
let no=array6.find(ele=>ele>10);  //first matching element
console.log(no);
let array3=new Array('vina','pooja','hari','kalpesh','vipin','varun');
console.log(array3);
let element=array3.find(el=>el.startsWith('v'));
console.log(element);
let newArray=array3.filter(el=>el.startsWith('v'));
console.log(newArray);
let myarr=[];
for(let i=0;i<array3.length;i++) {
    if(array3[i].startsWith('v'))
        myarr.push(array3[i])
}
console.log(myarr);
myarr=[];
for(let elem of array3) {
    if(elem.startsWith('v'))
        myarr.push(elem)
}
console.log(myarr);



//spread operator 
let emparr=['kumar','poonam','shali'];
let copyarr=[...emparr];
console.log(copyarr);

function sumFun(...arr) {
    let sum=0;
    for(let ele of arr) 
        sum=sum+ele;
    return sum;
}
console.log(sumFun(2,3));
console.log(sumFun(2,2,1));
console.log(sumFun(12));
console.log(sumFun(2,3,2));
console.log(sumFun(5,3,7,2,5));

function sumFun1(...arr) {
    let sum=arr.reduce((acc,elem)=>acc+elem);  //initially acc=1st ele of array, elem=2nd ele of array
    return sum;
}

console.log(sumFun1(2,3));
console.log(sumFun1(2,2,1));
console.log(sumFun1(12));
console.log(sumFun1(2,3,2));
console.log(sumFun1(5,3,7,2,5));

function sumFun2(...arr) {
    let sum=arr.reduce((acc,elem)=>acc+elem, 100);  //initially acc=100, elem=1st ele of an array
    return sum;
}

console.log(sumFun2(2,3));
console.log(sumFun2(2,2,1));
console.log(sumFun2(12));
console.log(sumFun2(2,3,2));
console.log(sumFun2(5,3,7,2,5));



let items=["steel","copper","bronze"];
items.forEach(display);
function display(item) {
    console.log(item);
}


const numbers = [4, 9, 16, 25];
const dummy=[];
numbers.map(cube);
function cube(nums) {
    dummy.push(nums**3);
}
console.log(dummy);