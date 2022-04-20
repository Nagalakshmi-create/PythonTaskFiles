let invalidBorder="4px double red";
let validBorder="4px double green";

let fnameNode;
let spanNode1;

$(document).ready(function() {
    fnameNode=$('#fname');
    spanNode1=$('#error1');
    fnameNode.blur(()=>validate1());
    lnameNode=$('#lname');
    spanNode2=$('#error2');
    lnameNode.blur(()=>validate2());
    ageNode=$('#age');
    spanNode3=$('#error3');
    ageNode.blur(()=>validate3());
    telNode=$('#telph');
    spanNode4=$('#error4');
    telNode.blur(()=>validate4());
    emailNode=$('#emails');
    spanNode5=$('#error5');
    emailNode.blur(()=>validate5());
    pwd1Node=$('#pwd1');
    spanNode6=$('#error6');
    tdNode=$('#passtd');
    pwd1Node.blur(()=>validate6());
    pwd2Node=$('#pwd2');
    spanNode7=$('#error7');
    pwd2Node.blur(()=>validate7());
    $('#rForm').submit(()=>formValidate());
    checkn=$("#showp");
    $('#showp').change(()=> {
        if($('#showp').prop('checked'))
            $('#pwd1, #pwd2').attr('type','text');
        else 
            $('#pwd1, #pwd2').attr('type','password');
    });
    
});

function validate1() {
    let firstName=fnameNode.val();
    spanNode1.text("");
    if (firstName==='') {
        spanNode1.text("First Name is required") ;
        fnameNode.css({'border':invalidBorder});
        return false;
    }
    else {
        fnameNode.css({'border':validBorder});
        return true;
    }
}

let lnameNode;
let spanNode2;
function validate2() {
    let lastName=lnameNode.val();
    spanNode2.text("");
    if (lastName==='') {
        spanNode2.text("Last Name is required") ;
        lnameNode.css({'border':invalidBorder});
        return false;
    }
    else {
        lnameNode.css({'border':validBorder});
        return true;
    }
}

let ageNode;
let spanNode3;
function validate3() {
    let age=ageNode.val();
    spanNode3.text("");
    if (age==='') {
        spanNode3.text("Age is required")  ;
        ageNode.css({'border':invalidBorder});
        return false;
    }
    else if(age<0 || age>70) {
        spanNode3.text("Age should be in the range of 1-70")  ;
        ageNode.css({'border':invalidBorder});
        return false;
    }
    else {
        ageNode.css({'border':validBorder});
        return true;
    }
}


let telNode;
let spanNode4;
function validate4() {
    let telp=telNode.val();
    spanNode4.text("");
    let regexp=RegExp("^[0-9]{10}$");
    let result=regexp.test(telp);  // true: mobile number matching with pattern , false: not
    if (telp==='') {
        spanNode4.text("Telephone Number is required")  ;
        telNode.css({'border':invalidBorder});
        return false;
    }
    else if(result==false) {
        spanNode4.text("Please enter valid mobile number")  ;
        telNode.css({'border':invalidBorder});
        return false;
    }
    else {
        telNode.css({'border':validBorder});
        return true;
    }
}

let emailNode;
let spanNode5;
function validate5() {
    let emailId=emailNode.val();
    spanNode5.text("");
    if (emailId==='') {
        spanNode5.text("Email Id is required")  ;
        emailNode.css({'border':invalidBorder});
        return false;
    }
    else if (!emailId.includes('@') || emailId.substring(emailId.indexOf('@')+1)==='') {
        spanNode5.text("Please put valid Email Id")  ;
        emailNode.css({'border':invalidBorder});
        return false;
    }
    else {
        emailNode.css({'border':validBorder});
        return true;
    }
}

let pwd1Node;
let spanNode6;
let tdNode;
function validate6() {
    let pwds1=pwd1Node.val();
    spanNode6.text("");
    let regexp2=RegExp("^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{5,12}$");
    let result2=regexp2.test(pwds1); // true: password matching with pattern, false: not
    spanNode6.text("");
    tdNode.html("");  //all inner elements of tdNode gets removed
    tdNode.append(spanNode6);   //but we need one span inside td so we are appending again
    if (pwds1==='') {
        spanNode6.text("Password is required")  ;
        pwd1Node.css({'border':invalidBorder});
        return false;
    }
    else if (result2==false) {
        spanNode6.text("Password should contain atleast")  ;
        let olNode=$('<ol></ol>');
        let array=['small letter','capital letter','digit','special symbol'];
        for(let ele of array) {
            let liNode=$('<li></li>');
            liNode.text(ele);
            olNode.append(liNode);  // <ol> <li></li><li></li><li></li><li></li></ol>
        }
        let boldNode=$('<b></b>');
        boldNode.text('and it should be 5 to `12 characters long');
        tdNode.append(spanNode6,olNode,boldNode); // <td><ol>   </ol></td>
        pwd1Node.css({'border':invalidBorder});
        return false;
    }
    else {
        pwd1Node.css({'border':validBorder});
        return true;
    }
}

let pwd2Node;
let spanNode7;
function validate7() {
    let pwds2=pwd2Node.val();
    let pwds1=pwd1Node.val();
    spanNode7.text("");
    if (pwds2==='') {
        spanNode7.text("Confirm Password is required")  ;
        pwd2Node.css({'border':invalidBorder});
        return false;
    }
    else if (pwds1!=pwds2) {
        spanNode7.text("Both Passwords should be matched")  ;
        pwd2Node.css({'border':invalidBorder});
        return false;
    }
    else {
        pwd2Node.css({'border':validBorder});
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
let checkn;
