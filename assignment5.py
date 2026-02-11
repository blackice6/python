def rectangle_area():
    length = 10
    width = 5
    area = length * width
    print("Area of rectangle:", area)

rectangle_area()

print("===============================")

def calculate_numbers(a, b):
    sum_result = a + b
    difference = a - b
    product = a * b
    division = a / b

    return sum_result, difference, product, division

# Example call
results = calculate_numbers(10, 5)
print("Sum:", results[0])
print("Difference:", results[1])
print("Product:", results[2])
print("Division:", results[3])

print("===============================")

def check_number():
    number = float(input("Enter a number: "))

    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

check_number()

print("===============================")

def sum_to_n(n):
    total = 0
    for number in range(1, n + 1):
        total += number
    print("Sum from 1 to", n, "is:", total)

sum_to_n(5)

print("===============================")

def squares_up_to():
    limit = int(input("Enter a number: "))
    number = 1

    while number <= limit:
        print("Square of", number, "is:", number * number)
        number += 1

squares_up_to()