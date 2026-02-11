# on the try and except block:you run some codes/statements and if it is succesful the try block will get executed other the except block will be executed other the except block will be executed when there is an anticipeted error.

try:
    number = 100

    answer = number / 0

    print(answer)
except Exception as e:
    print("there is an error:", e)