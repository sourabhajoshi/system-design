// Create a `BankAccount` class:
// - Private variable: `balance`
// - Methods:
//   - `deposit(amount)`
//   - `withdraw(amount)`
//   - `getBalance()`

// **Rules**
// - Balance cannot be modified directly
// - Withdrawal only if sufficient balance

class BankAccount{
    #balance

    constructor(balance){
        if(balance < 0){
            throw new Error("Balance should not be negetive.")
        }
        this.#balance = balance
    }

    deposit(amount){
        if(amount <= 0){
            console.log("Please deposite atleast 1$");
        }else{
            this.#balance += amount
        }
    }

    withdraw(amount){
        if(amount > this.#balance){
            console.log(`Insufficient balance. You can withdraw maximum ${this.#balance}`);
        }else{
            this.#balance -= amount
        }
    }

    getBalance(){
        return this.#balance;
    }
}

// const acc1 = new BankAccount(-5) //Error: Balance should not be negetive.

const acc1 = new BankAccount(500)
acc1.deposit(200)
console.log(`Avilable balance is ${acc1.getBalance()}`);
acc1.withdraw(300)
console.log(`Avilable balance is ${acc1.getBalance()}`);
