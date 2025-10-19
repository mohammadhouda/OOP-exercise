# Object-Oriented Programming (OOP) in Python — Cheat Sheet

This repository contains a **beginner-friendly OOP cheat sheet** that summarizes the **main concepts of Object-Oriented Programming in Python**.  
It’s designed for students and developers who want to understand and **practice OOP fundamentals** through short explanations and examples.

---

## About This Repository

-  Covers all key OOP principles: **Classes, Objects, Encapsulation, Inheritance, Polymorphism, and Methods**.  
-  Includes clean and minimal **Python code examples** for each concept.  
-  Encourages **self-learning** by motivating you to search and practice topics you find unclear.

---

## 1. Classes and Objects

A **class** is a blueprint for creating **objects** (instances).  
Objects represent real world entities with **attributes (data)** and **methods (behaviors)**.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Creating an object
car1 = Car("Tesla", "Model S")
car1.show_info()
```

## 2. Encapsulation

**Encapsulation** means keeping data and methods safe inside a class and controlling access to them.
In Python, attributes are public by default, but we can make them **private** using _ or __.

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

## 3. Inheritance

**Inheritance** allows a class to reuse and extend functionality from another class.
The new class is called a **child** (subclass), and the base is a **parent** (superclass).

``` python

class Car:
    def __init__(self, brand):
        self.brand = brand

class ElectricCar(Car):  # inherits from Car
    def __init__(self, brand, battery_range):
        super().__init__(brand)
        self.battery_range = battery_range

```
## 4. Polymorphism

**Polymorphism** means many forms — same method name but **different** behaviors depending on the object.

``` python

class Car:
    def fuel_type(self):
        return "Petrol"

class ElectricCar(Car):
    def fuel_type(self):
        return "Electric"

cars = [Car(), ElectricCar()]
for car in cars:
    print(car.fuel_type())  # Different outputs for same method name

```

## 5. Methods in Classes

| Method Type         | Description                                               | Example                |
| ------------------- | --------------------------------------------------------- | ---------------------- |
| **Instance Method** | Works on an instance (most common)                        | `def show_info(self):` |
| **Class Method**    | Works on the class itself, uses `@classmethod`            | `def count(cls):`      |
| **Static Method**   | Independent function inside a class, uses `@staticmethod` | `def greet():`         |


``` python

class Demo:
    count = 0

    def __init__(self):
        Demo.count += 1

    @classmethod
    def show_count(cls):
        print(f"Objects created: {cls.count}")

    @staticmethod
    def greet():
        print("Hello from class!")
```

## 6. Summary Table

| Concept           | Description                          | Example Keyword   |
| ----------------- | ------------------------------------ | ----------------- |
| **Class**         | Blueprint for creating objects       | `class`           |
| **Object**        | Instance of a class                  | `my_car = Car()`  |
| **Encapsulation** | Hiding data inside a class           | `_var`, `__var`   |
| **Inheritance**   | Reusing code from another class      | `class B(A):`     |
| **Polymorphism**  | Same method name, different behavior | `def speak()`     |

## Key Takeaway

OOP helps organize your code like the real world using classes and objects to make programs more readable, reusable, and scalable.

## Note for you

If you didn’t fully understand any topic from this cheat sheet (like class methods, or polymorphism),
take time to search, read more examples, and practice implementing each concept in code.
Understanding OOP deeply comes through doing, not just reading!

Author: Mohammad Houda
Python OOP Concepts Cheat Sheet — For Learning & Practice


