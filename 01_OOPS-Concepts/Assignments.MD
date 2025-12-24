# Class & Object – Practice Assignments (Beginner ➜ Advanced)

## LEVEL 1 – BEGINNER

### Assignment 1: Student Class
Create a `Student` class with:
- Properties: `name`, `age`, `marks`
- Method: `getDetails()` → prints all details

### Assignment 2: Student Class with validator
Create a `Student` class with:
- Properties: `name`, `age`, `marks`
- Method: `getDetails()` → prints all details

### Assignment 3: car Class
Create a `Car` class with:
- Properties: `brand`, `model`, `year`
- Method: `getCarInfo()` → prints all details

### Assignment 4: Calculator Class
Create a `Calculator` class with:
- Properties: `a`, `b`
- Method: `add(a, b), sub(a, b), mul(a, b)` 

## LEVEL 2 – INTERMEDIATE

### Assignment 5: Bank Account
Create a `Student` class with:
- Properties: `accountHolder`, `balance`
- Method: `deposit(amount), withdraw(amount) showBalance()` 
Balance should not go negative

### Assignment 6: Employee Salary
Create a `Employee Salary` class with:
- Properties: `name`, `salary`
- Method: `calculateAnnualSalary()` 
Create multiple employees and print annual salary.

## LEVEL 3 – ADVANCED

### Assignment 6: User Login System
Create a `user` class with:
- Properties: `username, password`
- Method: `login(inputPassword) and changePassword(oldPass, newPass)` 

Rules
- Login only if password matches
- Password should not be directly accessible

----

# Emcapsulation – Practice Assignments (Beginner ➜ Advanced)

## LEVEL 1 – BEGINNER (Encapsulation Basics)

### Assignment 1: Student Marks (Getter Only)
Create a `Student` class:
- Private / protected property: `marks`
- Public properties: `name`
- Method:
  - `getMarks()` → return marks

**Rules**
- Marks should NOT be accessed directly
- No setter yet

---

### Assignment 2: Counter with Control
Create a `Counter` class:
- Private variable: `count`
- Methods:
  - `increment()`
  - `decrement()` (should not go below 0)
  - `getCount()`

---

## LEVEL 2 – INTERMEDIATE (Getter + Setter)

### Assignment 3: BankAccount (Controlled Access)
Create a `BankAccount` class:
- Private variable: `balance`
- Methods:
  - `deposit(amount)`
  - `withdraw(amount)`
  - `getBalance()`

**Rules**
- Balance cannot be modified directly
- Withdrawal only if sufficient balance

---

### Assignment 4: User Password (Classic Encapsulation)
Create a `User` class:
- Private variable: `password`
- Methods:
  - `login(inputPassword)`
  - `changePassword(oldPass, newPass)`

**Rules**
- Password should NEVER be directly accessible
- Password length ≥ 5
- Old password must match before changing

---

## LEVEL 3 – ADVANCED (Validation + Protection)

### Assignment 5: Product Inventory
Create a `Product` class:
- Private variables:
  - `price`
  - `quantity`
- Methods:
  - `buy(count)`
  - `restock(count)`
  - `getProductInfo()`

**Rules**
- Price cannot be negative
- Quantity cannot go below 0

---

### Assignment 6: Employee Salary System
Create an `Employee` class:
- Protected variable: `salary`
- Methods:
  - `getSalary()`
  - `incrementSalary(percent)`

**Rules**
- Salary cannot be modified directly
- Increment must be positive

---

## LEVEL 4 – CHALLENGE (Think Like Senior Dev)

### Assignment 7: ATM Machine (Full Encapsulation)
Create an `ATM` class:
- Private variables:
  - `balance`
  - `pin`
- Methods:
  - `checkBalance(pin)`
  - `withdraw(pin, amount)`
  - `changePin(oldPin, newPin)`

**Rules**
- No direct access to balance or pin
- Wrong pin → deny operation

---

### Assignment 8: Login Attempt Limiter
Create a `SecureUser` class:
- Private variables:
  - `password`
  - `attempts`
- Methods:
  - `login(inputPassword)`

**Rules**
- Max 3 failed attempts
- After 3 failures → account locked
- Attempts should not be directly accessible

