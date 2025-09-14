# assignment3_exercises.py

import math

# 1. Area of rectangle
def rectangle_area(length, width):
    return length * width

# 2. Greeting message
def greeting(name, age):
    return f"Hello {name}, you are {age} years old!"

# 3. Even or odd
def even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

# 4. Max and min in list
def max_min(numbers):
    return max(numbers), min(numbers)

# 5. Check palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# 6. Compound interest
def compound_interest(principal, rate, time):
    # rate is in percent, time in years
    amount = principal * (1 + rate/100) ** time
    return amount - principal

# 7. Convert days to years, weeks, days
def convert_days(days):
    years = days // 365
    weeks = (days % 365) // 7
    remaining_days = (days % 365) % 7
    return years, weeks, remaining_days

# 8. Sum of positive numbers
def sum_of_positives(numbers):
    return sum(n for n in numbers if n > 0)

# 9. Count words in a sentence
def count_words(sentence):
    return len(sentence.split())

# 10. Swap two variables
def swap(a, b):
    return b, a

