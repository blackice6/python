# Test 1
# By use of a function that accepts parameters, calculate the simple interest given principal as 45000, rate is 7% and the time taken is 8 years. (si = p*r*t/100)
# Use the same function inside of a loop to calculate two other simple interests. Note use your own principal, rate and time.# Test 1
# By use of a function that accepts parameters, calculate the simple interest given principal as 45000, rate is 7% and the time taken is 8 years. (si = p*r*t/100)
# Use the same function inside of a loop to calculate two other simple interests. Note use your own principal, rate and time.

def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    print("The simple interest is: ", si)
simple_interest(45000, 7, 8)
print("===========================")
# loop to calculate two other simple interests
for i in range(2):
    principal = int(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = int(input("Enter the time in years: "))
    simple_interest(principal, rate, time)
    