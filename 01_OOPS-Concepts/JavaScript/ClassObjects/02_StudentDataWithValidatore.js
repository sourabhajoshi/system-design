class StudentData{
    name
    age
    marks

    constructor(name, age, marks){

        if(age <= 0) throw new Error("Age must be positive")
        if(marks < 0 || marks > 100) throw new Error("marks should be in b/w 1 to 100")

        this.name = name;
        this.age = age;
        this.marks = marks
    }

    getDetails(){
        return `Name is ${this.name}, age is ${this.age} and ${this.marks} marks scored`
    }
}

const std1 = new StudentData("Joshi", -5, 52)
console.log(std1.getDetails());
