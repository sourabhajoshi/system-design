class Calculator{
    a
    b

    constructor(a, b){
        this.a = a
        this.b = b
    }

    addTwoNum(){
        return (this.a + this.b)
    }

    subTwoNum(){
        return (this.a - this.b)
    }

    mulTwoNum(){
        return (this.a * this.b)
    }
}

const cal1 = new Calculator(5, 10)
console.log("Add : ", cal1.addTwoNum());
console.log("Sub : ", cal1.subTwoNum());
console.log("Sub : ", cal1.mulTwoNum());
