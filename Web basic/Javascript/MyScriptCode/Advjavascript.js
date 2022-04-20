class Employee {
    empId;
    empName;
    empSalary;
}
let emp=new Employee();  //default constructor
console.log(emp.empId);
console.log(emp.empName);
console.log(emp.empSalary);
emp.empId=112;
emp.empName="Naga";
emp.empSalary=70000;
console.log(emp.empId);
console.log(emp.empName);
console.log(emp.empSalary);


class Student {
    studId;
    studName;
    studPercentage;
    constructor(id, name, percent) {
        this.studId=id;
        this.studName=name;
        this.studPercentage=percent;
    }

    showDetails() {
        return "Id: "+this.studId+" Name: "+this.studName+" Percentage: "+this.studPercentage;
    }

    calculatePercent(m1,m2,m3) {
        this.studPercentage=(m1+m2+m3)/3;
    }
}

let stud=new Student(111,"poonam",78);
console.log(stud.studId);
console.log(stud.studName);
console.log(stud.studPercentage);
stud.calculatePercent(89,90,78);
console.log(stud.studPercentage);
let details=stud.showDetails();
console.log(details);

let stud1=new Student();   // no error in js  // in ts: no matching constructor found
console.log(stud1.studId);
console.log(stud1.studName);
console.log(stud1.studPercentage);