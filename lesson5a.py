# python functions
# they are block of code/ statements that perform a given task/action. they can be reused through out the program to perform different tasks.
# functions are defined using the def keyword.(define)
# we have two main types of functions i.e:
# 1. in-built function =>-> They come preinstalled with the interpreter i.e print(), pop(), range(), append() etc...
# 2. User defined functions => They are created by a programmer to solve a given task.
# To define a function you need to give it a name followed by parenthesis.
# For the functions, it is usually indented and to invoke a function we use the function name.


def greetings():
    print("Hello, how are you?")
# below we called the function by use of the function name
greetings()

print("===========================")
# addition function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is: ", sum)

addition()


print("===========================")
# create a function that  is able to multiply three values
def multiplication():
    num1 = 10
    num2 = 20
    num3 = 30
    product = num1 * num2 * num3
    print("The product of the numbers is: ", product)

multiplication()

print("===========================")
#below is a division function
def division():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    quotient = num1 / num2
    print("The quotient of the numbers is: ", quotient)

division()

for function in range(3):
    division()