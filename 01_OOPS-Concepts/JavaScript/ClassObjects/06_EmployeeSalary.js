// Create an Employee class:
// Properties: name, salary
// Method: calculateAnnualSalary()
// Create multiple employees and print annual salary.

class Employee{
    name
    salary

    constructor(name, salary){
        this.name = name
        this.salary = salary
    }

    calculateAnnualSalary(){
        console.log(`Employee name is ${this.name} and salary ${this.salary}`);
        
    }
}

const emp1 = new Employee("hece", 125125);
const emp2 = new Employee("hgecyed", 254215);
const emp3 = new Employee("kdjdfh", 125223);


emp1.calculateAnnualSalary()
emp2.calculateAnnualSalary()
emp3.calculateAnnualSalary()