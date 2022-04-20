let text = "Welcome Naga";
let newText = text.replace("Naga", "Sandhya");  //replaces only the first match
console.log("Replace:  "+newText);

let text1="Hell";
let text2="World"
let newText1=text1.concat("o", " ", text2);
console.log("Concat:  "+newText1);

let a="           Hi All          ";
let b=a.trim();
console.log("Trim:  "+b);

let text3 = "Na";
let padded = text3.padStart(3,1);
console.log("padStart:  "+padded);

let text4 = "Na";
let padded1 = text4.padEnd(3,1);
console.log("padEnd:  "+padded1);

let text5="Hello Vamsi you are very great Vamsi";
let result=text5.lastIndexOf("s");
console.log("lastIndexOf:  "+result);

let text6 = "Hello world, welcome to the universe.";
let result1=text6.startsWith("world", 6);
console.log("startsWith:  "+result1);

let text7="Good Morning";
let result2=text7.endsWith("ing");
console.log("endsWith:  "+result2);


const vehicles=["car","bus","van","bike","cycle"];
vehicles.splice(2, 1, "tractor","truck");
console.log(vehicles);

const flowers=["jasmine","rose","lily","Hibiscus","sunflower","lotus"];
flowers.splice(3,2);
console.log(flowers);

const fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
const citrus = fruits.slice(1, 3);
console.log(citrus);