# Calculate the area of a circle
def calculate_area(radius):
    pi = 3.14
    area = pi * (radius**2)
    print("The area of the circle is: ", area)



print("This Program calculates the area of a circle ")
radius = float(input("Enter the radius: "))
calculate_area(radius)