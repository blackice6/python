# loops -> sections, we may need to do a piece of work a number of repeated time in such a cade we use loops.
# a loop  is a control structure that allows us to execute a bloch of code repeatedly untill a certain conditio is met
# there are two types of loops in python i.e : thefor loop and the while loop

# below is the syntax of a for loop in python:
"""
for variable in range(n):
    # block of code to be executed
"""



for greeting in range(5):
    print("hello Moses", greeting)


for number in range(10, 20):
    print(number) 


# find the even number in the range of 50 to 71
for number in range(50, 71, 2):
    print(number)

# create a python program that prints the odd numbers from 100 to 150
for number in range(101, 150, 2):
    print(number)

# create a program that prints the multiples of 3 startin from 201 to 150
for number in range(201, 149, -1):
    if number % 3==0:
        print(number)


# create a python program that prints the leap year in between 2000 and 2024
for year in range(2000, 2025, 4):
    print(year)