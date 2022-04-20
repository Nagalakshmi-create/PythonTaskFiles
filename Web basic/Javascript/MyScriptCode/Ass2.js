const sentence="<b>All </b> is well";
const para1=document.getElementById("para1");
const para2=document.getElementById("para2");
console.log(para1.innerHTML=sentence);
console.log(para2.innerText=sentence);


const image=document.getElementById('image');
const heading=document.getElementById('heading');
let ele=document.createElement('p');
ele.textContent="The star is Red in color";
let ele1=document.createElement('p');
ele1.textContent="Sky is blue in color";
heading.after(ele);  //for after heading element       
image.parentNode.insertBefore(ele1,image);     //for before image element



const nodeList = document.body.children;
var elements=[...nodeList];
console.log(elements);


let image1=document.getElementById("image1");
let imageArray=["../HTML/My Images/Nature image.png", "../HTML/My Images/lataji.webp", "../HTML/My Images/sachin.jpg", "../HTML/My Images/submit-button-icon-png-1.jpg"];
function imgShow() {
    let a=0;
    let interval=setInterval(function() {
        image1.src=imageArray[a];
        image1.style.width="150px";
        image1.style.height="180px";
        a++;
        if(a>(imageArray.length)-1) {
            a=0;
        }
    }, 2000);
}

imgShow();
