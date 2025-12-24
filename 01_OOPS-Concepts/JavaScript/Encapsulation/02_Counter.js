// Create a `Counter` class:
// - Private variable: `count`
// - Methods:
//   - `increment()`
//   - `decrement()` (should not go below 0)
//   - `getCount()`

class Counter{
    #count

    constructor(count){
        this.#count = count
    }

    increment(){
        this.#count += 1;
    }

    decrement(){
        if(this.#count < 0) throw new Error("should not go below 0")
        this.#count -= 1;
    }

    getCount(){
        return this.#count
    }
}

// const cnt1 = new Counter(5)
// cnt1.decrement()
// cnt1.decrement()
// cnt1.decrement()
// cnt1.decrement()
// cnt1.decrement()
// cnt1.decrement()
// cnt1.decrement()
// cnt1.decrement()

const cnt2 = new Counter(10)
cnt2.increment()
console.log(cnt2.getCount());

cnt2.decrement()
console.log(cnt2.getCount());


