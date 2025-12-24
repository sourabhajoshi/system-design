// Create a BankAccount class:

// Properties: accountHolder, balance

// Methods: deposit(amount), withdraw(amount), showBalance()

// Rules : Balance should not go negative

class BankAccount{
    accountHolder
    balance

    constructor(accountHolder, balance){
        if (balance < 0) throw new Error("Balance should not be negative")

        this.accountHolder = accountHolder
        this.balance = balance
    }

    deposit(amount){
        if (amount > 0){
            this.balance += amount
            console.log(`You successfully depositted ${amount}$. Avilable balance is ${this.balance}$`)
        }
    }

    withdraw(amount){
        if(amount > this.balance){
            console.log("Insufficient balance");
        }else{
            this.balance -= amount
            console.log(`You successfully withdrown ${amount}$. Avilable balance is ${this.balance}$`)
        }
    }

    showBalance(){
        console.log(`your avilable balance is ${this.balance}$`);
        
    }
}

const acc1 = new BankAccount("Joshi", 500)
acc1.showBalance()
acc1.deposit(200)
acc1.withdraw(300)

const acc2 = new BankAccount("Joshi", -200)
