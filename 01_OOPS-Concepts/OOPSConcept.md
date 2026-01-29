# Object Orianted Programming language

At the heart of OOP lie two fundamental concepts: **classes** and **objects**.

They are the foundation on which every OOP-based language like Java, Python, C++, C#, or TypeScript is built.

###**What is a Class?**

A **class** is a _blueprint_, _template_, or _recipe_ for creating objects. It defines **what an object will contain** (its data) and **what it will be able to do** (its behavior).

A class is not an object itself, it’s a template used to create many objects with similar structure but independent state.

Think of a class like a **recipe for a cake**:

*   The _ingredients_ represent **fields or attributes** (flour, sugar, eggs → variables).
*   The _instructions_ represent **methods or functions** (mix, bake, decorate → operations).

The recipe itself doesn’t produce a cake, it just defines how to make one. When you follow the recipe and bake a cake, you’ve just created an **object**.

**Key Characteristics of a Class:**

*   It groups related data (attributes) and actions (methods) together.
*   Defines **attributes** to represent the state or data of an object.
*   Defines **methods** (functions inside a class) to represent the **behavior** or actions the object can perform.

**Example: Class Blueprint**

Let’s define a simple Car class with essential attributes and methods that any Car object will have.

The following diagram and code show the blueprint for a Car:

**Code:**

```
class Car:
    # Constructor
    def __init__(self, brand, model):
        # Attributes (private by convention with underscore)
        self._brand = brand
        self._model = model
        self._speed = 0

    # Method to accelerate
    def accelerate(self, increment):
        self._speed += increment

    # Method to display info
    def display_status(self):
        print(f"{self._brand} is running at {self._speed} km/h.")
```

This Car class defines what every car object should look like and what it can do.

---

###**What is an Object?**

An **object** is an instance of a class. It’s a _real-world manifestation_ of the class blueprint, something you can interact with, store data in, and invoke methods on.

When you create an object, you’re essentially saying:

“Take this blueprint (class) and build one actual thing (object) out of it.”

Each object:

*   Has its **own copy** of the data defined in the class.
*   Shares the same **structure** and **behavior** as defined by the class.
*   Operates **independently** of other objects.

**Creating Objects**

Let’s now create a few car objects using our Car class.

**Code:**
```
if __name__ == "__main__":
    # Creating objects of the Car class
    corolla = Car("Toyota", "Corolla")
    mustang = Car("Ford", "Mustang")

    corolla.accelerate(20)
    mustang.accelerate(40)

    # Displaying status of each car
    corolla.display_status()
    print("-----------------")
    mustang.display_status()
```

**Output:**

**Toyota Corolla is running at 20 km/h.**

**\-----------------**

**Ford Mustang is running at 40 km/h.**

**Here, corolla and mustang are objects of the Car class. They have their own brand , model , and speed fields and can use methods defined in the class.**

Classes and objects are powerful when you need to model complex structures or real-world entities. But what if you simply want to define a fixed set of constants, values that rarely change and for which you only ever need one instance of each?

That's where Enums come in. Lets explore them next.

Enums (short for **enumerations**) are a powerful yet underappreciated feature in object-oriented design. They allow you to define a **fixed set of named constants** that improve clarity, type safety, and maintainability in your system.

Used correctly, enums can make your code more **expressive**, **self-documenting**, and **resilient to errors**.

--

###**What is an Enum?**

An **enum** is a special data type that defines a collection of constant values under a single name. Unlike primitive constants or string literals, enums are **type-safe,** which means you can’t assign just any value to a variable declared as an enum type.

They ensure that a variable can only take **one out of a predefined set of valid options**.

**In short:** If a value can only be one of a predefined set of options, use an enum.

**Why Use Enums?**

Enums provide several key advantages over plain constants or strings:

*   **Avoid “magic values”:** No more scattered strings or integers like "PENDING" or 3 in your code.
*   **Improve readability:** Enums make your intent clear — OrderStatus.SHIPPED is far more descriptive than 3.
*   **Enable compiler checks:** The compiler validates enum usage, catching typos and invalid assignments early.
*   **Support IDE features:** Most IDEs provide auto-completion and refactoring tools for enum values.
*   **Reduce bugs:** You can’t accidentally assign a random string or number that doesn’t belong to enum.

**Example Enums:**

Enums are perfect for defining categories or states that rarely change.

*   Order States (e.g., PENDING, IN\_PROGRESS, COMPLETED)
*   User Roles (e.g., ADMIN, CUSTOMER, DRIVER)
*   Vehicle Types (e.g., CAR, BIKE, TRUCK)
*   Directions (e.g., NORTH, SOUTH, EAST, WEST)

By using enums instead of raw strings, you make your system easier to understand and harder to misuse.

**Code Examples**

**Simple Enum**

Let’s start with a simple example representing the status of an order in an e-commerce application.

```
from enum import Enum

# Simple Enum
class OrderStatus(Enum):
    PLACED = "PLACED"
    CONFIRMED = "CONFIRMED"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"
```

This enum defines a **finite set of valid states** an order can have. Nothing else is allowed.

**Using it in code:**
```
status = OrderStatus.SHIPPED

if status == OrderStatus.SHIPPED:
    print("Your package is on the way!")
```

**Enums with Properties and Methods**

Enums can have additional data and even behavior. This makes them even more powerful.

Let’s consider a Coin enum that represents U.S. coins and their denominations.

```
from enum import Enum

class Coin(Enum):
    PENNY = 1
    NICKEL = 5
    DIME = 10
    QUARTER = 25
    
    def __init__(self, value):
        self.coin_value = value
    
    def get_value(self):
        return self.coin_value
```

**Using It in Code:**

```
total = Coin.DIME.get_value() + Coin.QUARTER.get_value()  # 35
```

This is far more elegant and safe than using integers directly.

Enums help you define a fixed set of well-known values, giving structure and clarity to your data. But what if you want to define **a common set of behaviors** that different classes can implement in their own way?

That’s where **Interfaces** come in. In the next chapter, we'll dive into interfaces.

In object-oriented design, interfaces play a foundational role in building systems that are extensible, testable, and loosely coupled.

They define what a component should do, not how it should do it.

This separation of _definition_ and _implementation_ allows different parts of your system to work together through well-defined contracts, without needing to know each other’s internal details.

---

###**What is an Interface?**

At its core, an interface is a contract: a list of methods that any implementing class _must_ provide. It specifies a set of behaviors that a class agrees to implement but leaves the _details_ of those behaviors up to each implementation.

In other words:

An interface defines the "what", while classes provide the "how".

Real-World Analogy

Consider a remote control. It exposes a standard set of buttons:

*   `play()`
*   `pause()`
*   `volumeUp()`
*   `powerOff()`

The person using the remote doesn’t care if it controls a TV, a soundbar, or a projector, they all understand the same set of commands.

The remote is the interface. The devices (TV, soundbar, projector) are the implementations.

Each device behaves differently when you press `play()`, but the _contract_ remains consistent.

**Key Properties of Interfaces**

Interfaces are more than just method declarations, they are the foundation of flexible software design.

Here are their most important characteristics:

**a) Defines Behavior Without Dictating Implementation**

An interface only declares _what_ operations are expected. It doesn’t define _how_ they are carried out.

This gives freedom to implementers to provide their own version of the logic, while still honoring the same contract.

**b) Enables Polymorphism**

Different classes can implement the same interface in different ways.This allows your code to work with multiple implementations interchangeably.

**c) Promotes Decoupling**

Code that depends on interfaces is insulated from changes in the concrete classes that implement them.

This makes your code easier to:

*   Extend (add new implementations without modifying existing ones),
*   Test (mock interfaces in unit tests),
*   Maintain (fewer ripple effects from code changes).

**Example:**

As long as all payment providers implement the `PaymentGateway` interface, the `CheckoutService` can use any of them without changing its own code.

**Code Example: Payment Gateway Interface**

Let’s say you’re designing a payment processing module that supports multiple providers like Stripe, Razorpay, and PayPal.

You don’t want your business logic to depend on a specific provider. You just want a common way to initiate a payment.

You can define a generic interface:

```
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def initiate_payment(self, amount):
        pass
```

This interface defines the contract. Every payment gateway must provide a `initiatePayment()` method. But it doesn’t specify how each provider processes payments.

Now you can create multiple implementations:
```
class StripePayment(PaymentGateway):
    def initiate_payment(self, amount):
        print(f"Processing payment via Stripe: ${amount}")

class RazorpayPayment(PaymentGateway):
    def initiate_payment(self, amount):
        print(f"Processing payment via Razorpay: ₹{amount}")
```

Both `StripePayment` and `RazorpayPayment` implement the same interface, but the actual logic for processing the payment is different.

**Usage: Loose Coupling in Action**

Now let’s say you have a `CheckoutService` that processes payments. Instead of hardcoding a specific payment gateway, you inject the interface:

```
class CheckoutService:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway
    
    def set_payment_gateway(self, payment_gateway):
        self.payment_gateway = payment_gateway
    
    def checkout(self, amount):
        self.payment_gateway.initiate_payment(amount)
```

Notice that `CheckoutService` depends only on the interface, not the implementation. This makes it easy to swap or extend payment providers without changing the checkout logic.

Now you can plug in any payment gateway at runtime:
```
if __name__ == "__main__":
    stripe_gateway = StripePayment()
    checkout_service = CheckoutService(stripe_gateway)
    checkout_service.checkout(120.50)  # Output: Processing payment via Stripe: $120.5
    
    # Switch to Razorpay
    razorpay_gateway = RazorpayPayment()
    checkout_service.set_payment_gateway(razorpay_gateway)
    checkout_service.checkout(150.50)  # Output: Processing payment via Razorpay: ₹150.5
```

Here’s the beauty of it:

*   `CheckoutService` doesn’t care _which_ payment gateway is being used.
*   You can replace, extend, or test different gateways without touching its code.

Now that you understand how interfaces define contracts and enable flexibility between different components, it’s time to explore the core principles that make object-oriented programming truly powerful, starting with Encapsulation.

---

###**What is Encapsulation?**

Encapsulation is one of the four foundational principles of object-oriented design. It is the practice of **grouping data (variables) and behavior (methods)** that operate on that data into a single unit (typically a class) and **restricting direct access to the internal details** of that class.

In simple terms:

**Encapsulation = Data hiding + Controlled access**

**Real-World Analogy**

Think of a bank account as a **vault inside a bank**. You don't walk into the vault and change the numbers yourself.

Instead, you interact with it through a **well-defined interface,** the **ATM**.

The ATM provides limited but specific operations:

*   deposit()
*   withdraw()
*   checkBalance()

You can’t directly access or modify the bank’s internal data.

The bank might change how it stores information, applies interest, or validates transactions but none of that affects how you use the ATM.

That’s **encapsulation** in action — hiding internal complexity and exposing only what’s necessary.

In a well-encapsulated design, external code doesn’t need to know **how** something is done, it only needs to know **what** can be done.

**Why Encapsulation Matters**

Encapsulation isn’t just about data protection, it’s about designing systems that are **robust**, **secure**, and **easy to maintain**.

**1\. Data Hiding**

Sensitive data (like a bank balance or password) should not be exposed directly. Encapsulation keeps this data private and accessible only through controlled methods.

**2\. Controlled Access and Validation**

It ensures that data can only be modified in **controlled, predictable ways**.

For example, you can prevent invalid deposits or withdrawals by validating input inside methods.

**3\. Improved Maintainability**

Because internal details are hidden, you can change the implementation (e.g., how data is stored or validated) without affecting the code that depends on it.

**4. Security and Stability**

By preventing external tampering, encapsulation reduces the risk of inconsistent or invalid system states.

**How Encapsulation is Achieved**

Encapsulation is primarily implemented using two language features:

**1\. Access Modifiers**

Keywords like private, protected, and public are used to control the visibility of attributes and methods.

*   private: Accessible only within the same class. This is the primary tool for data hiding.
*   public: Accessible from anywhere. This creates the controlled public interface.

**2\. Getters and Setters**

These are public methods that provide controlled, indirect access to private attributes.

*   **Getter (e.g., getBalance()):** Provides read-only access to an attribute.
*   **Setter (e.g., setAmount()):** Allows modifying an attribute, often with validation logic built-in.

**Code Examples**

Let’s look at two practical examples that demonstrate how encapsulation helps you protect internal state, enforce business rules, and expose only what’s necessary.

**Example 1: BankAccount**

In a banking system, you want users to **deposit and withdraw funds**, but you must **prevent direct manipulation** of the account balance. Here’s how encapsulation helps:

```
class BankAccount:
   def __init__(self):
       self.__balance = 0.0  # Internal state is hidden

   def deposit(self, amount):
       if amount <= 0:
           raise ValueError("Deposit amount must be positive")
       self.__balance += amount

   def withdraw(self, amount):
       if amount <= 0:
           raise ValueError("Withdrawal amount must be positive")
       if amount > self.__balance:
           raise ValueError("Insufficient funds")
       self.__balance -= amount

   def get_balance(self):
       return self.__balance  # Controlled access
```

*   balance is marked private, so no external class can access or modify it directly.
*   deposit() and withdraw() are **public entry points** that validate user input before updating the state.
*   getBalance() allows **read-only access**, without revealing the underlying variable or letting external code change it.

This ensures the account remains in a valid state at all times and business rules are enforced through controlled interfaces.

**Example 2: PaymentProcessor**

Let’s take a more realistic example. You’re building a PaymentProcessor class that handles credit card transactions.

You don’t want raw card numbers to be stored or visible anywhere in the system.

```
class PaymentProcessor:
   def __init__(self, card_number, amount):
       self.__card_number = self.__mask_card_number(card_number)
       self.__amount = amount

   def __mask_card_number(self, card_number):
       return "****-****-****-" + card_number[-4:]

   def process_payment(self):
       print(f"Processing payment of {self.__amount} for card {self.__card_number}")


if __name__ == "__main__":
   payment = PaymentProcessor("1234567812345678", 250.00)
   payment.process_payment()
```

PaymentProcessor class accepts a card number and amount, but internally **masks the card number** to protect user privacy. Again, encapsulation allows us to hide implementation details while offering a clean interface.

**Output:**

```
Processing payment of 250.0 for card ****-****-****-5678
```

*   The raw card number is never stored or exposed directly.
*   Masking is handled **internally** via a private method.
*   The external caller doesn’t need to know how masking is done, they just call processPayment().

This design secures sensitive data and centralizes masking logic in one place, making the system safer and easier to maintain.

Encapsulation focuses on **how to protect and control access** to data within a class. But what if we extend that idea. Not just hiding data, but also **hiding complexity** itself?

That’s where **Abstraction** comes in.

In the next chapter, we’ll explore how **abstraction** helps you design systems that expose only the essential details while concealing unnecessary complexity, making your code cleaner, more intuitive, and easier to work with.

---

###**What is Abstraction?**

**Abstraction** is the process of hiding complex internal implementation details and exposing only the relevant, high-level functionality to the outside world. It allows developers to **focus on what an object does**, rather than **how it does it**.

It allows developers to focus on _what an object does_, rather than _how it does it_.

**In short:**

**Abstraction = Hiding Complexity + Showing Essentials**

By separating the **what** from the **how**, abstraction:

*   Reduces cognitive load
*   Improves modularity
*   Leads to cleaner, more intuitive APIs

**“Abstraction is about creating a simplified view of a system that highlights the essential features while suppressing the irrelevant details.”**

**Real-World Analogy: Driving a Car**

Think about how you drive a car:

You turn the **steering wheel**, press the **accelerator**, and shift the **gears**.

But you **don’t need to know**:

*   How the transmission works
*   How the fuel is injected
*   How torque or combustion is calculated

All of that mechanical complexity is abstracted away behind a **simple interface** — the steering wheel, pedals, and gear lever.

That’s exactly what **abstraction** does in software. It lets you use complex systems through simple, high-level interactions.

**Abstraction vs Encapsulation**

Although often discussed together, abstraction and encapsulation are distinct concepts.

*   **Abstraction** focuses on hiding **complexity**. It's about simplifying what the user sees. (The accelerate() pedal in a car).
*   **Encapsulation** focuses on hiding **data**. It's about bundling data and methods together to protect an object's internal state. (The engine is a self-contained unit).

Think of it this way: **Abstraction is the external view of an object, while Encapsulation is the internal view.**

|        Aspect |        Encapsulation |        Abstraction |
| --- | --- | --- |
| Focus | Protecting data within a class | Hiding implementation complexity |
| Goal | Restrict access to internal state | Simplify usage and expose only essentials |
| Level | Implementation-level | Design-level |
| Example | Private balance field in BankAccount | Exposing only deposit() and withdraw() without showing how they work |

Together, they make systems **secure**, **modular**, and **easy to reason about.** Encapsulation _protects_, abstraction _simplifies_.

**Why Abstraction Matters**

Abstraction is critical in designing systems that are **scalable**, **maintainable**, and **easy to use**.

**1. Reduces Complexity**

Users and developers don’t need to understand how a feature works internally — just how to use it.

**2. Improves Usability**

By exposing a minimal and intuitive interface, abstraction makes APIs easier to learn and harder to misuse.

**3. Enables Reusability and Substitutability**

Well-abstracted components can be replaced, extended, or reused without modifying the rest of the system.

**4. Decouples Design Decisions**

Internal implementations can evolve independently of the public interface, improving maintainability and flexibility.

**How Abstraction Is Achieved**

In **Object-Oriented Programming (OOP)**, abstraction is implemented using language features that allow developers to define **what an object should do** without specifying **how** it does it.

This is primarily achieved through:

**1. Abstract Classes**

Abstract classes define a common blueprint for a family of classes. It defines **what** must be done but lets subclasses decide **how** to do it.

It may contain:

*   **Abstract methods** (declared but not implemented)
*   **Concrete methods** (fully implemented)
*   **Fields and constructors** shared across subclasses

They are useful when:

*   Multiple classes share some behavior or state
*   You want to provide a default implementation but enforce subclasses to override specific behaviors

**Example:**
```
from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start(self):
        pass

    def display_brand(self):
        print("Brand:", self.brand)

# Subclass implementing the abstract method
class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

    def start(self):
        print("Car is starting...")
```

**Explanation**

*   The **abstract class Vehicle** defines the structure. Every vehicle must have a brand and a way to start.
*   The **Car** subclass provides its own implementation of start().
*   Users of Vehicle don’t care _how_ the vehicle starts, they just call start().

**2. Interfaces**

An interface is a **pure abstraction**. It defines a **contract** that a class must fulfill but doesn’t provide any implementation. Interfaces are ideal when you want to enforce a consistent API across unrelated classes.

**Example:**

```
class Document:
    def __init__(self, content):
        self.__content = content

    def get_content(self):
        return self.__content

class Printable(ABC):
    @abstractmethod
    def print(self, document):
        pass

# Concrete implementation of Printable
class PDFPrinter(Printable):
    def print(self, document):
        print("Printing PDF:", document.get_content())

class InkjetPrinter(Printable):
    def print(self, document):
        print("Printing via Inkjet:", document.get_content())
```

**Explanation**

*   The **Printable** interface defines _what_ printers must do — print(Document doc).
*   The **implementations** (PDFPrinter, InkjetPrinter) define _how_ the printing happens.
*   You can add new printers later without changing existing code.

**3. Public APIs**

Even when you're not using abstract classes or interfaces, **abstraction is achieved through clean, public APIs** that expose only what's necessary.

**Example: Database Client**

```
class DatabaseClient:
    def connect(self):
        # ...
        pass

    def query(self, sql):
        # ...
        pass

    def __open_socket(self):
        # internal logic
        pass

    def __authenticate(self):
        # internal logic
        pass
```
**Explanation**

*   Users only see connect() and query() — a simple, high-level API.
*   They don’t see or care about low-level socket handling or authentication logic.
*   The **interface remains clean**, while the internal implementation can evolve freely.

**Example: Abstracting a Printer**

Let’s say you’re using a Printer object in your application:

printer.print(document);

As a user of the print() method, you **don’t need to know**:

*   How the printer formats the document
*   How it communicates with the driver or firmware
*   Whether the connection is USB, Bluetooth, or Wi-Fi
*   How print jobs are queued and prioritized

All this complexity is **abstracted away**. The only thing you care about is:

"Can I send this document to the printer and get a physical copy?"

**More Examples:**

*   A **Task Scheduler** exposing scheduleTask(), while hiding threads and queues
*   A **Payment Gateway** offering pay(), abstracting card verification and fraud checks
*   A **DatabaseClient** providing query() and insert(), hiding connection pooling and transaction management

Abstraction helps you define **what** your objects should do but how do you **reuse and extend** that behavior across related classes?

That’s where **Inheritance** comes in.

In the next chapter, we’ll explore how inheritance enables **code reuse**, **shared behavior**, and **hierarchical design**, allowing classes to build upon and extend one another.

---

###**What is Inheritance?**

Inheritance allows one class (called the subclass or child class) to inherit the properties and behaviors of another class (called the superclass or parent class).

**In simpler terms:**

Inheritance enables code reuse by letting you define common logic once in a base class and then extend or specialize it in multiple derived classes.

This leads to cleaner, modular, and more maintainable software

**Real-World Analogy**

**Think of a User system in a web application:**

*   The base User class holds common attributes like username, email, and methods like login() or logout().
*   Specialized roles like Admin, Customer, and Vendor inherit from User but add role-specific behavior.

All specialized user types inherit common data and behaviors from the User class, but can extend functionality to suit their roles.

**Why Inheritance Matters**

Inheritance offers several benefits that make it a powerful design tool in OOP.

**1. Code Reusability**

It embodies the DRY (Don't Repeat Yourself) principle. Common logic is written once in the parent class and shared across all subclasses reducing redundancy.

**2. Logical Hierarchy**

It creates a clear and intuitive hierarchy that model real-world _“is-a”_ relationships like ElectricCar _is a_ Car or Admin _is a_ User.

**3. Ease of Maintenance**

If a bug is found or a change is needed in the shared logic, you only need to fix it in one place, the superclass. All subclasses automatically inherit the fix.

**4. Polymorphism**

Inheritance is a prerequisite for polymorphism, allowing objects of different subclasses to be treated as objects of the superclass.

**How Inheritance Works**

**When a class inherits from another:**

*   The subclass inherits all non-private fields and methods of the superclass.
*   The subclass can override inherited methods to provide a different implementation.
*   The subclass can also extend the superclass by adding new fields and methods.

This allows for both reuse and customization.

**Code Example: Car Hierarchy**

Let’s model a simple vehicle system.

```
class Car:
    def __init__(self):
        self.make = None
        self.model = None

    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")
```

This Car class defines basic attributes and common behaviors shared by all cars.

**Now you can create specialized types of cars:**

```
class ElectricCar(Car):
    def charge_battery(self):
        print("Battery charging")

class GasCar(Car):
    def fill_tank(self):
        print("Filling gas tank")
```

In this example:

*   Both ElectricCar and GasCar inherit the make, model, startEngine(), and stopEngine() methods from the Car class.
*   Each subclass adds behavior specific to its type.
*   This structure mirrors the real-world relationship: an electric car is a car, and so is a gas car.

**When to Use Inheritance**

Inheritance is powerful, but it should be used intentionally, only when it truly models a real-world relationship.

**Use inheritance when:**

*   There is a clear "is-a" relationship (e.g., Dog is an Animal, Car is a Vehicle)
*   The parent class defines common behavior or data that should be shared
*   The child class does not violate the behavior expected from the parent
*   You want to promote code reuse through shared logic and structure

**Avoid inheritance when:**

*   The relationship is more of a “has-a” or “uses-a” (e.g., a Car has an Engine, not is an Engine)
*   You want to combine behaviors dynamically
*   You need flexibility or runtime switching between behaviors
*   You don’t want child classes to be tightly coupled to parent internals

In these cases, composition is usually a better choice.

**Use Inheritance with Caution**

While inheritance is powerful, it's often overused. Incorrectly applying it can lead to rigid, fragile designs that are hard to maintain.

**Common Pitfalls:**

*   Misusing inheritance for code reuse: Inheriting from a class just to reuse methods, without a true “is-a” relationship, leads to poor design.
*   Deep inheritance chains: Complex hierarchies make systems difficult to understand, debug, or modify.
*   Tight coupling: Subclasses become too dependent on parent implementation details, making future changes risky.

This is why many modern OOP designs favor composition over inheritance for better modularity and flexibility.

**Inheritance vs. Composition**

Both Inheritance and Composition define relationships between classes but they serve different purposes and offer different trade-offs.

|     Aspect |     Inheritance |    Composition |
| --- | --- | --- |
| Relationship | “is-a” | “has-a” or “uses-a” |
| Coupling | Tightly coupled | Loosely coupled |
| Flexibility | Compile-time (fixed) | Runtime (dynamic) |
| Best for | Shared logic & hierarchy | Reusable and pluggable components |
| Example | Car extends Vehicle | Car has an Engine |

Prefer composition over inheritance when:

*   You need flexibility and runtime behavior changes
*   The relationship is "has-a" rather than "is-a"
*   You want to avoid coupling to a class hierarchy

**Example:**

Instead of this:

```
class Printer extends Logger {
    // bad inheritance just to reuse log()
}
```

**Do this:**
```
class Printer:
    def __init__(self, logger):
        self.logger = logger

    def print_(self, message):
        self.logger.log(f"Printing: {message}")
```

Here, the Printer _has a_ Logger, not _is a_ Logger. This keeps the design modular, testable, and loosely coupled.

Inheritance lets child classes share and extend behavior but what if multiple subclasses need to behave differently when responding to the same method call?

**That’s where Polymorphism comes in.**

In the next chapter, we’ll explore how polymorphism enables a single interface to represent multiple implementations allowing your code to be flexible, elegant, and truly object-oriented.

---

###**What is Polymorphism?**

Polymorphism allows the same method name or interface to exhibit different behaviors depending on the object that is invoking it.

The term "polymorphism" comes from Greek and means _"many forms."_ In programming, it allows us to write code that is generic, extensible, and reusable, while the specific behavior is determined at runtime or compile-time based on the object’s actual type.

Polymorphism lets you call the same method on different objects, and have each object respond in its own way.

You write code that targets a common type, but the actual behavior is determined by the concrete implementation.

**Real-World Analogy**

Think of a universal remote control.

*   The buttons are the same: powerOn(), volumeUp(), mute().
*   But depending on the device: a TV, Air Conditioner, or Projector each button performs a different action.

For the user, the interface (remote) never changes. But internally, each device interprets the same signal differently.

That’s polymorphism in action. The same interface triggers different behaviors depending on the receiver (device type).

**Why Polymorphism Matters**

*   Encourages loose coupling: You interact with abstractions (interfaces or base classes), not specific implementations.
*   Enhances flexibility: You can introduce new behaviors without modifying existing code, supporting the Open/Closed Principle.
*   Promotes scalability: Systems can grow to support more features with minimal impact on existing code.
*   Enables extensibility: You can “plug in” new implementations without touching the core business logic.

**Two Types of Polymorphism**

Polymorphism is broadly categorized into two types based on _when_ the method to be executed is determined.

**1. Compile-time Polymorphism (Static Binding)**

Also known as method overloading, compile-time polymorphism occurs when:

*   You have multiple methods with the same name in the same class.
*   Each method has a different parameter list (number, type, or order).
*   The method to call is decided at compile time, based on the arguments passed.

**Example:**

```
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }

    public double add(double a, double b) {
        return a + b;
    }

    public int add(int a, int b, int c) {
        return a + b + c;
    }
}
```
**Output:**

```
5
6.0
6
```

Here, the compiler determines which version of add() to call based on the parameters before the program runs.

**2. Runtime Polymorphism (Dynamic Binding)**

Also known as method overriding, this happens when:

*   A subclass overrides a method defined in its superclass or interface.
*   The method to invoke is determined at runtime, based on the actual object type.

**Example:**

Suppose you’re designing a system that sends notifications. You want to support email, SMS, push notifications, etc.

You start by defining a common interface.

```
class NotificationSender(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass
```

Now, you implement it in multiple ways:

```
class EmailSender(NotificationSender):
    def send_notification(self, message):
        print("Sending EMAIL:", message)

class SmsSender(NotificationSender):
    def send_notification(self, message):
        print("Sending SMS:", message)
```

And use it like this:
```
def notify_user(sender, message):
    sender.send_notification(message)
```

You can pass any implementation of NotificationSender, and the correct behavior will be triggered based on the object passed.

This is runtime polymorphism, where the decision of which method to execute is made during execution, not at compile time.

**Polymorphism in LLD Interviews**

Polymorphism is especially useful in Low-Level Design when:

*   You want to plug in different behaviors without modifying the core logic
*   You need to support extensible systems with new types of objects (e.g., different payment providers, transport types, etc.)
*   You want to design to interfaces or base classes and allow flexibility in how objects behave

For example: if you're designing a PaymentProcessor interface, you can have multiple implementations like CreditCardProcessor, PayPalProcessor, and UPIProcessor. The payment system doesn’t need to care which one it's using, it just calls processPayment().

```
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing credit card payment of ${amount}")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing PayPal payment of ${amount}")

class UPIProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing UPI payment of ₹{amount}")
```

**Client code:**

```
class PaymentService:
    def pay(self, processor: PaymentProcessor, amount: float) -> None:
        processor.process_payment(amount)
```

This system can easily be extended to support new payment types (like ApplePay or Stripe) without changing PaymentService.

Now that we have explored the four pillars of Object-Oriented Programming (Encapsulation, Abstraction, Inheritance, and Polymorphism), it’s time to look at how classes interact with one another in a real system.

Let’s begin with the most common and fundamental type of relationship: Association, where one class simply uses another to perform a specific function.
