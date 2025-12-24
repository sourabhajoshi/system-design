class Student{
    name
    age
    marks

    constructor(name, age, marks){
        this.name = name;
        this.age = age;
        this.marks = marks
    }

    getDetails(){
        return `Name is ${this.name}, age is ${this.age} and ${this.marks} marks scored`
    }
}

const std = new Student("Joshi", 25, 85)
console.log(std.getDetails());
