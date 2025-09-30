# exercise_prime_json_csv_question.py

"""
Python Exercise:

Write a Python program that does the following:

1. Ask the user to enter 10 numbers (one by one).
2. From these numbers, find which ones are prime.
3. Store the prime numbers inside a dictionary
   (example format: {"prime_0": 2, "prime_1": 11}),
   where the key is "prime_index" and the value is the prime number.
4. Save this dictionary into a JSON file (primes.json).
5. Read back the JSON file and extract only the prime numbers
   that are greater than 7.
6. Save these filtered prime numbers into a CSV file (filtered_primes.csv)
   with one column named prime_number.

--------------------------------------------
Example Run:

Input:
Enter number 1: 4
Enter number 2: 7
Enter number 3: 11
Enter number 4: 15
Enter number 5: 2
Enter number 6: 13
Enter number 7: 20
Enter number 8: 3
Enter number 9: 9
Enter number 10: 19

Dictionary saved to JSON (primes.json):
{
    "prime_2": 11,
    "prime_4": 2,
    "prime_5": 13,
    "prime_7": 3,
    "prime_9": 19
}

Filtered primes > 7 saved to CSV (filtered_primes.csv):
prime_number
11
13
19
"""

#  Your solution goes here...
