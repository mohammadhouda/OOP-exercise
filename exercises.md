## Exercise: Build a Simple Car Management Program

### Goal
This exercise will help you **apply all the OOP concepts** you learned above — classes, objects, methods, inheritance, and polymorphism — by building a simple car management program.

---

### Task Description

You are working for a **car manufacturing company**, and you need to create a Python program that manages different types of cars.

Follow these steps carefully 👇

---

### Step 1: Create a `Car` class  
- Add attributes: `brand`, `model`, and `price`.  
- Add a method `car_info()` that prints the car’s brand, model, and price.

Example output:
Brand: Toyota | Model: Corolla | Price: $20000

yaml
Copy code

---

### Step 2: Create two subclasses that inherit from `Car`
1. **ElectricCar**  
   - Add an extra attribute: `battery_range` (in km).  
   - Override the `car_info()` method to include the battery range.

2. **GasCar**  
   - Add an extra attribute: `fuel_type` (like "Petrol" or "Diesel").  
   - Override the `car_info()` method to include the fuel type.

---

### Step 3: Create multiple car objects
- Create at least one `ElectricCar` and one `GasCar`.  
- Store them in a list called `cars`.

Example:


``` python
cars = [
    ElectricCar("Tesla", "Model 3", 45000, 500),
    GasCar("Toyota", "Corolla", 20000, "Petrol")
]
```

### Step 4: Loop through all cars
Loop through the cars list and print each car’s info using the car_info() method.

Expected output:
``` python
Tesla Model 3 (Electric)
Range: 500 km
Price: $45000
Toyota Corolla (Gas)
Fuel: Petrol
Price: $20000
```

### Bonus Challenge (Optional)
Try adding:

- A method called discount() that applies a discount to the price.

- A counter that keeps track of how many cars were created.

### What You’ll Practice
| Concept            | What you’ll do                                        |
| ------------------ | ----------------------------------------------------- |
| **Class & Object** | Create the `Car`, `ElectricCar`, and `GasCar` classes |
| **Inheritance**    | Make both subclasses inherit from `Car`               |
| **Polymorphism**   | Override `car_info()` in each subclass                |
| **Encapsulation**  | Store data inside objects                             |
| **Methods**        | Define actions inside your classes                    |


### Tip:
If you don’t understand a part of this exercise, go back to the cheat sheet sections and re-read the related concept.
Understanding OOP comes from writing code, not just reading it!

