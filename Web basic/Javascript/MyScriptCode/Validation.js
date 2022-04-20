let invalidBorder="4px double red";
let validBorder="4px double green";

let fnameNode=document.getElementById('fname');
let spanNode1=document.getElementById('error1');
function validate1() {
    let firstName=fnameNode.value;
    spanNode1.textContent="";
    if (firstName==='') {
        spanNode1.textContent="First Name is required"  ;
        fnameNode.style.border=invalidBorder;
        return false;
    }
    else {
        fnameNode.style.border=validBorder;
        return true;
    }
}

let lnameNode=document.getElementById('lname');
let spanNode2=document.getElementById('error2');
function validate2() {
    let lastName=lnameNode.value;
    spanNode2.textContent="";
    if (lastName==='') {
        spanNode2.textContent="Last Name is required"  ;
        lnameNode.style.border=invalidBorder;
        return false;
    }
    else {
        lnameNode.style.border=validBorder;
        return true;
    }
}

let ageNode=document.getElementById('age');
let spanNode3=document.getElementById('error3');
function validate3() {
    let age=ageNode.value;
    spanNode3.textContent="";
    if (age==='') {
        spanNode3.textContent="Age is required"  ;
        ageNode.style.border=invalidBorder;
        return false;
    }
    else if(age<0 || age>70) {
        spanNode3.textContent="Age should be in the range of 1-70"  ;
        ageNode.style.border=invalidBorder;
        return false;
    }
    else {
        ageNode.style.border=validBorder;
        return true;
    }
}


let telNode=document.getElementById('telph');
let spanNode4=document.getElementById('error4');
function validate4() {
    let telp=telNode.value;
    spanNode4.textContent="";
    let regexp=RegExp("^[0-9]{10}$");
    let result=regexp.test(telp);  // true: mobile number matching with pattern , false: not
    if (telp==='') {
        spanNode4.textContent="Telephone Number is required"  ;
        telNode.style.border=invalidBorder;
        return false;
    }
    else if(result==false) {
        spanNode4.textContent="Please enter valid mobile number"  ;
        telNode.style.border=invalidBorder;
        return false;
    }
    else {
        telNode.style.border=validBorder;
        return true;
    }
}

let emailNode=document.getElementById('emails');
let spanNode5=document.getElementById('error5');
function validate5() {
    let emailId=emailNode.value;
    spanNode5.textContent="";
    if (emailId==='') {
        spanNode5.textContent="Email Id is required"  ;
        emailNode.style.border=invalidBorder;
        return false;
    }
    else if (!emailId.includes('@') || emailId.substring(emailId.indexOf('@')+1)==='') {
        spanNode5.textContent="Please put valid Email Id"  ;
        emailNode.style.border=invalidBorder;
        return false;
    }
    else {
        emailNode.style.border=validBorder;
        return true;
    }
}

let pwd1Node=document.getElementById('pwd1');
let spanNode6=document.getElementById('error6');
let tdNode=document.getElementById("passtd");
function validate6() {
    let pwds1=pwd1Node.value;
    spanNode6.textContent="";
    let regexp2=RegExp("^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{5,12}$");
    let result2=regexp2.test(pwds1); // true: password matching with pattern, false: not
    spanNode6.textContent="";
    tdNode.innerHTML="";  //all inner elements of tdNode gets removed
    
    if (pwds1==='') {
        spanNode6.textContent="Password is required"  ;
        pwd1Node.style.border=invalidBorder;
        return false;
    }
    else if (result2==false) {
        spanNode6.textContent="Password should contain atleast"  ;
        let olNode=document.createElement('ol');
        let array=['small letter','capital letter','digit','special symbol'];
        for(let ele of array) {
            let liNode=document.createElement('li');
            liNode.textContent=ele;
            olNode.append(liNode);  // <ol> <li></li><li></li><li></li><li></li></ol>
        }
        let boldNode=document.createElement('b');
        boldNode.textContent='and it should be 5 to `12 characters long';
        tdNode.append(spanNode6,olNode,boldNode); // <td><ol>   </ol></td>
        pwd1Node.style.border=invalidBorder;
        return false;
    }
    else {
        pwd1Node.style.border=validBorder;
        return true;
    }
}

let pwd2Node=document.getElementById('pwd2');
let spanNode7=document.getElementById('error7');
function validate7() {
    let pwds2=pwd2Node.value;
    let pwds1=pwd1Node.value;
    spanNode7.textContent="";
    if (pwds2==='') {
        spanNode7.textContent=" Confirm Password is required"  ;
        pwd2Node.style.border=invalidBorder;
        return false;
    }
    else if (pwds1!=pwds2) {
        spanNode7.textContent=" Both Passwords should be matched"  ;
        pwd2Node.style.border=invalidBorder;
        return false;
    }
    else {
        pwd2Node.style.border=validBorder;
        return true;
    }
}

function formValidate() {
    let st1=validate1()
    let st2=validate2()
    let st3=validate3()
    let st4=validate4()
    let st5=validate5()
    let st6=validate6()
    let st7=validate7()
    return (st1 && st2 && st3 && st4 && st5 && st6 && st7);
}
let checkn=document.getElementById("showp");
checkn.addEventListener('change', ()=>showPassword());

function showPassword() {
    let pass=document.getElementById("pwd1");
    let c_pass=document.getElementById("pwd2");
    if (checkn.checked) {
        pass.type="text";
        c_pass.type="text";
    }
        
    else {
        pass.type="password";
        c_pass.type="password";
    }
}
