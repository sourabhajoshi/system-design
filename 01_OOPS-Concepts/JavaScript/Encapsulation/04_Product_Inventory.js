// Create a `Product` class:
// - Private variables:
//   - `price`
//   - `quantity`
// - Methods:
//   - `buy(count)`
//   - `restock(count)`
//   - `getProductInfo()`

// **Rules**
// - Price cannot be negative
// - Quantity cannot go below 0

class Product{
    #price
    #quantity

    constructor(price, quantity){
        if(price < 0){
            throw new Error("Price cannot be negative")
        }

        if(quantity < 0){
            throw new Error("Quantity cannot go below 0")
        }
        this.#price = price
        this.#quantity = quantity
    }

    buy(count){

    }

    restock(count){

    }

    getProductInfo(){
        return
    }
}