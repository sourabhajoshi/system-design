# SOLID

The SOLID principles are five design principles intended to make software designs more understandable, flexible, and maintainable. They are especially useful in object-oriented design and often applied during system design, HLD, and LLD phases.

- S	Single Responsibility Principle
- O	Open/Closed Principle
- L	Liskov Substitution Principle
- I	Interface Segregation Principle
- D	Dependency Inversion Principle

SOLID gives you a clean, modular, and maintainable codebase that’s easier to build, test, grow, and hand over.

#### **Building a Restaurant Kitchen**

Without SOLID : Imagine you hired one person to:

- Cook food
- Take customer orders
- Handle payments
- Clean dishes
- Restock ingredients

What could go wrong?

- Overloaded person (hard to maintain)
- Messy handoffs (code coupling)
- One change affects everything (hard to scale)
- Cannot replace them easily (low flexibility)

With SOLID : 

- Chef: only cooks food (Single Responsibility)
- Cashier: handles payments (Interface Segregation)
- Manager: doesn’t care how cashier works, just wants a receipt (Dependency Inversion)
- You can replace the chef with a robot as long as it cooks the same food (Liskov Substitution)
- Want to add “delivery”? Just extend the system without breaking the kitchen (Open/Closed)

#### **Why SOLID is Important?**

1. Easy to Understand
Code becomes clearer and less confusing.
You know exactly what each part does.Like having labels on rooms – “Kitchen”, “Bedroom” – no guesswork.

2. Easy to Maintain
You can fix bugs or add features without breaking other things. Fixing a light in the kitchen doesn’t cut power to the bathroom.

3. Scalable
New developers can join and understand the code easily. Projects can grow without turning into a mess.
You can add more floors without the base collapsing.

4. Reusable Code
You write code once and reuse it across the project.
Like using the same door design for every room.

5. Testable
Each class does one thing, so it's easier to write unit tests.
You can test each appliance separately, like the fridge or fan.

### 1. Single Responsibility Principle

Every class (or module) should have only one reason to change.
That means it should only do one specific job.

```
<!-- Bad Code -->

class RestaurantWorker:
    def take_order(self): pass
    def cook_food(self): pass
    def clean_table(self): pass
    def handle_payment(self): pass

```

```
<!-- Good code -->

class Waiter:
    def take_order(self): pass

class Chef:
    def cook_food(self): pass

class Cleaner:
    def clean_table(self): pass

class Cashier:
    def handle_payment(self): pass
```

- SRP in Real Life: One person = one job
- SRP in Code: One class = one responsibility

### 2. Open/Closed Principle

A class, module, or function should be open for extension but closed for modification.

Why is OCP Important?
- Reduces the risk of breaking working code.
- Encourages code reuse.
- Makes it easier to adapt software to future requirements.
- Ideal for maintaining large-scale, long-lived systems.

```
<!-- Bad Code : That Violates OCP -->
class PaymentProcessor:
    def process(self, payment_type, amount):
        if payment_type == "credit_card":
            print(f"Processing credit card payment of ${amount}")
        elif payment_type == "paypal":
            print(f"Processing PayPal payment of ${amount}")
```
Note : Every time a new payment method is introduced (e.g., UPI, crypto), you must modify this class.

```
<!-- Good code : Compliant Version Using Polymorphism -->
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def process(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment(PaymentMethod):
    def process(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# Now the processor works with any payment method
class PaymentProcessor:
    def __init__(self, method: PaymentMethod):
        self.method = method

    def pay(self, amount):
        self.method.process(amount)
```

Another example of Notification system

```
<!-- Bad code : Every new channel (like Slack or WhatsApp) forces a change to Notifier.-->
class Notifier:
    def notify(self, message, channel):
        if channel == "email":
            print(f"Email: {message}")
        elif channel == "sms":
            print(f"SMS: {message}")
        elif channel == "push":
            print(f"Push: {message}")
```

```
class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotifier(NotificationChannel):
    def send(self, message):
        print(f"Email: {message}")

class SMSNotifier(NotificationChannel):
    def send(self, message):
        print(f"SMS: {message}")

class PushNotifier(NotificationChannel):
    def send(self, message):
        print(f"Push: {message}")

class Notifier:
    def __init__(self, channel: NotificationChannel):
        self.channel = channel

    def notify(self, message):
        self.channel.send(message)

class WhatsAppNotifier(NotificationChannel):
    def send(self, message):
        print(f"WhatsApp: {message}")

```

Open : You can add new code (via subclassing or new modules)

Closed : You don’t need to change existing code to add new behavior

### 3. Liskov Substitution Principle

Subtypes must be substitutable for their base types without altering the correctness of the program.

If class S is a subclass of class T, then objects of class T should be replaceable with objects of class S without breaking the program. If you replace a parent class object with a child class object, the program should still work correctly.

```
# parant class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

# sub class
class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width  # Forces height to be same

    def set_height(self, height):
        self.height = height
        self.width = height  # Forces width to be same

def print_area(rect):
    rect.set_width(5)
    rect.set_height(10)
    print("Expected area = 50")
    print("Actual area =", rect.get_area())

# Test
print_area(Rectangle(2, 3))  # Works: 5 x 10 = 50
print_area(Square(2))        # Wrong: set_height(10) sets width = 10, so area = 100

```