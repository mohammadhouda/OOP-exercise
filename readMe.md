# Python Cheatsheet: JSON, CSV, and Prime Numbers

## 🔢 Prime Numbers
```python
# Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Only check up to sqrt(n)
        if n % i == 0:
            return False
    return True

# Example
print(is_prime(7))  # True
print(is_prime(10)) # False
```

---

## 📂 JSON (JavaScript Object Notation)

### Save dictionary to JSON
```python
import json

data = {"primes": [2, 3, 5, 7, 11]}

# Write to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)  # indent=4 makes it pretty
```

### Read JSON file
```python
with open("data.json", "r") as f:
    loaded_data = json.load(f)

print(loaded_data)  # {'primes': [2, 3, 5, 7, 11]}
```

---

## 📊 CSV (Comma-Separated Values)

### Write to CSV
```python
import csv

primes = [11, 13, 17, 19]

with open("primes.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Prime Numbers"])  # Header
    for p in primes:
        writer.writerow([p])  # Each number in a row
```

### Read from CSV
```python
with open("primes.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```
