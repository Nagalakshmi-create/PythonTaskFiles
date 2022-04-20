function firstnum() {
    let fnum;
    let number=window.prompt("Enter first number : ");
    fnum=parseInt(number);
    document.getElementById("fn").textContent=fnum;
    document.getElementById("fn").value=fnum;
}

function secondnum() {
    let snum;
    let number=window.prompt("Enter fsecond number : ");
    fnum=parseInt(number);
    document.getElementById("sn").textContent=fnum;
    document.getElementById("sn").value=fnum;
}

function r() {
    let x;
    x=document.getElementById("fn").value+document.getElementById("sn").value;
    document.getElementById("result").textContent=x;
}


//salaries question

let r1=document.getElementById("salaries");
let salaryArray=[];
let results=[];
let salaries=()=> {
    for(var i=1;i<=5;i++) {
        let a=window.prompt("Enter salary_"+i);
        salaryArray.push(parseInt(a));
    }

    results=salaryArray.filter((each) => each>60000);
    document.write('<h3>['+ salaryArray +']');
    document.write('<h3>['+ results +']');
    console.log(salaryArray);
    console.log(results);
}