class CarInfo{
    brand
    model
    year

    constructor(brand, model, year){
        const currentYear = new Date().getFullYear()
        if (year > currentYear) throw new Error("Year shouldn't cross the current year")

        this.brand = brand
        this.model = model
        this.year = year
    }

    carInfo(){
        return `car name is ${this.brand}, model ${this.model} and published year ${this.year}`
    }
}

const car1 = new CarInfo("Tata", "Tiago", 2026)
console.log(car1.carInfo());
