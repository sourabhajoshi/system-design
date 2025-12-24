// Create a `Student` class:
// - Private / protected property: `marks`
// - Public properties: `name`
// - Method:
//   - `getMarks()` → return marks

// - Marks should NOT be accessed directly
// - No setter yet

class Student{
    
    #marks

    constructor(name, marks){
        if(marks < 0 || marks > 100) throw new Error("Marks should be in b/w 0 to 100")
        this.name = name
        this.#marks = marks
    }

    getMarks(){
        return this.#marks
        // console.log(`Total marks for ${this.name} is ${this.#marks}`);
    }
}

const std1 = new Student("Joshi", 85)
console.log(`Total marks for ${std1.name} is ${std1.getMarks()}`)