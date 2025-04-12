# Program to list the factors of a positive number
def find_factors(num):
    factor_list = []
    for i in range(1, num+1):
        if num % i == 0:
            factor_list.append(i)
    print(f"The factors of {num} are: ", factor_list)

print("This program finds the factors of a number")
num = int(input("Enter the number: "))
find_factors(num)