function showAlert() {
    window.alert("Hurry up sale ends soon!!!");
}

let showConfirm=function() {
    let action=window.confirm("Do you really want to Finish the exam????");
    if(action==true)
        document.write("<h3>Exam submitted successfully....</h3>;")
    else 
        document.write("<h3>You can continue with exam....</h3>")
}

let showPrompt=() => {
    let name=window.prompt("Enter your name");
    document.write(name);
    document.write(typeof name);
}