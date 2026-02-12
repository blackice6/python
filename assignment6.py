# 1
# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si

# Example usage
principal = 1000  # Amount in rupees
rate = 5  # Rate in percentage
time = 2  # Time in years
interest = calculate_simple_interest(principal, rate, time)
print(f"Simple Interest: {interest}")  # Output: Simple Interest: 100.0

# 2
# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Example usage
weight = 70  # in kg
height = 1.75  # in meters
bmi = calculate_bmi(weight, height)
print(f"BMI: {bmi:.2f}")  # Output: BMI: 22.86

# 3
# Function to calculate area of a triangle
def calculate_triangle_area(base, height):
    area = (base * height) / 2
    return area

# Example usage
base = 10
height = 5
area = calculate_triangle_area(base, height)
print(f"Area of Triangle: {area}")  # Output: Area of Triangle: 25.0

# 4
import math

# Function to calculate area of a circle
def calculate_circle_area(radius):
    area = math.pi * (radius ** 2)
    return area

# Example usage
radius = 7
area = calculate_circle_area(radius)
print(f"Area of Circle: {area:.2f}")  # Output: Area of Circle: 153.94

# 5
shopping = {
    'sugar': 120,
    'rice': 200,
    'milk': 60,
    'bread': 60
}

# 1. Print this dictionary
print("Shopping Dictionary:")
print(shopping)
# Output:
# Shopping Dictionary:
# {'sugar': 120, 'rice': 200, 'milk': 60, 'bread': 60}

# 2. Find the sum of all items in above dictionary
total_sum = sum(shopping.values())
print(f"Sum of all items: {total_sum}")  # Output: Sum of all items: 440

# 6
# person = {'john': 40, 'peter': 45}

# This will raise a KeyError because 'susan' is not a key in the dictionary
# print(person['susan'])

# 7
# Create a list of towns
towns = ['New York', 'London', 'Tokyo', 'Paris']

# Reverse the list
towns.reverse()

# Print the reversed list
print("Reversed list of towns:")
print(towns)

# 8
# Loop to print from 10 to 40
for i in range(10, 41):  # range(start, end+1)
    print(i)

# 9
# Loop to print from -10 to -50
for i in range(-10, -51, -1):  # range(start, end-1, step)
    print(i)

# 10
# Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage
year = 2024
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 11
# Function to calculate BMI
def find_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Example usage
weight = 80  # in kg
height = 1.8  # in meters
bmi = find_bmi(weight, height)
print(f"Body Mass Index: {bmi:.2f}") 

# 12
# Program to calculate travel cost based on distance

distance = float(input("Enter the distance traveled: "))

if distance >= 0 and distance <= 100:
    cost = 5.00
elif distance > 100 and distance <= 500:
    cost = 8.00
elif distance > 500 and distance < 1000:
    cost = 10.00
else:   # 1000 or more
    cost = 12.00

print("The travel cost is $", cost)

# 13
# Program to check if a number is odd or even

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

