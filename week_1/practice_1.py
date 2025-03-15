print("Simple Interest Calculator")

p = int(input("Enter the principal amount: "))
r = int(input("Enter the rate: "))
t = int(input("Enter the time: "))

a = p * (1 + (0.01*r) * t)
print("Amount: ",a)

print("Compund Interest Calculator")

P = int(input("Enter the principal amount: "))
R = int(input("Enter the rate: "))
T = int(input("Enter the time: "))
n = int(input("Enter the value of n: "))

A = P * ((1 + (R/n)) ** (n*T))
print("Amount: ",A)

print("Annuity Plan Calculator")

PMT = int(input("Enter the PMT amount: "))
rate = int(input("Enter the rate: "))
time = int(input("Enter the time: "))
no = int(input("Enter the value of n: "))

Amount = (PMT * ((1 + (rate/no)) ** (no*time) - 1)) / (rate/no) 
print("Amount: ",Amount)

