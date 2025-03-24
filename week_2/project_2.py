# Introduction 
print("Welcome to the Polynomial Root calculator!!!")
print("I can calculate the roots of the following:")
print("1. Quadratic Equation")
print("2. Cubic Equation")
print("3. Quartic Equation")

# Getting input from user
option = int(input("What type of equation will you be working with? (Select 1-3)"))

if option == 1 :
   a = float(input("What is the value of a?"))
   b = float(input("What is the value of b?"))
   c = float(input("What is the value of c?"))
   d = (b**2) - (4 * a * c)
   if d < 0:
      print("No real roots")
   elif d == 0:
      root = (-b) / (2*a)
      print(f"The root is {root}")
   else:
        root1 = (-b + (d** 0.5)) / 2 * a
        root2 = (-b - (d** 0.5)) / 2 * a
        print(f"Root 1 = {root1}, Root 2 = {root2}")
elif option != 1 :
   print("I can't solve this yet!")