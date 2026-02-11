# functions with parametas
# parameters: are variables that get passed as arguments given to a function inside the parenthesis. 

from unicodedata import name


def greetings(name):
    print(f"{name} how are you? hope everything is fine.")

greetings("John")
greetings("Alice")
greetings("Bob")

print("===========================")
def message(name):
    print(f"hello.{name} we shall be having a general meeting on date...please avail yourself")

message("Joy")
message("Mary")

print("===========================")
# create a function that accepts parameters to add two numbers
def addition(num1, num2):
    sum = num1 + num2
    print("The sum of the numbers is: ", sum)
addition(10, 20)