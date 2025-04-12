print("                             Izifin Technology Employee Revenue Calculator")

# Getting inputs from user
name = str(input("Enter your full name: "))
age = int(input("Enter your Age: "))
exp = int(input("Years of work experience: "))

# Conditional statements 
if exp > 25 and age >= 55:
    print("Your Annual Tax Revenue is ₦5,600,000")

elif exp > 20 and age >= 45:
    print("Your Annual Tax Revenue is ₦4,480,000")

elif exp > 10 and age >= 35:
    print("Your Annual Tax Revenue is ₦1,500,000")

elif exp < 10 and age < 35:
    print("Your Annual Tax Revenue is ₦550,000")