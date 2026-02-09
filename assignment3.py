gross_salary = float(input("Enter gross salary: "))

if gross_salary < 0:
    print("Error: Salary must be greater than 0.")
elif gross_salary <= 5999:
    contribution = 150
elif gross_salary <= 7999:
    contribution = 300
elif gross_salary <= 11999:
    contribution = 400
elif gross_salary <= 14999:
    contribution = 500
elif gross_salary <= 19999:
    contribution = 600
elif gross_salary <= 24999:
    contribution = 750
elif gross_salary <= 29999:
    contribution = 850
elif gross_salary <= 49999:
    contribution = 1000
elif gross_salary <= 99999:
    contribution = 1500
else:  # Over 100,000
    contribution = 2000

print("NHIF Monthly Contribution: Ksh",contribution)