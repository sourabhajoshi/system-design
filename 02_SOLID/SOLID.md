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
