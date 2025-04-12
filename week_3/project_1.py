# Program to store the Data of 20 students

print("This table shows the data of 20 students!")

from tabulate import tabulate

students = [
    {"Name": "Evelyn", "Age": 17, "Height": 5.5, "Score": 80},
    {"Name": "Jessica", "Age": 16, "Height": 6.0, "Score": 85},
    {"Name": "Somto", "Age": 17, "Height": 5.4, "Score": 70},
    {"Name": "Edith", "Age": 18, "Height": 5.9, "Score": 60},
    {"Name": "Liza", "Age": 16, "Height": 5.6, "Score": 76},
    {"Name": "Madonna", "Age": 18, "Height": 5.5, "Score": 66},
    {"Name": "Waje", "Age": 17, "Height": 6.1, "Score": 87},
    {"Name": "Tola", "Age": 20, "Height": 6.0, "Score": 95},
    {"Name": "Aisha", "Age": 19, "Height": 5.7, "Score": 50},
    {"Name": "Latifa", "Age": 17, "Height": 5.5, "Score": 49},
    {"Name": "Chinedu", "Age": 19, "Height": 5.7, "Score": 74},
    {"Name": "Liam", "Age": 16, "Height": 5.9, "Score": 87},
    {"Name": "Wale", "Age": 18, "Height": 5.8, "Score": 75},
    {"Name": "Gbenga", "Age": 17, "Height": 6.1, "Score": 68},
    {"Name": "Abiola", "Age": 20, "Height": 5.9, "Score": 66},
    {"Name": "Kola", "Age": 19, "Height": 5.5, "Score": 78},
    {"Name": "Kunle", "Age": 16, "Height": 6.1, "Score": 87},
    {"Name": "George", "Age": 18, "Height": 5.4, "Score": 98},
    {"Name": "Thomas", "Age": 17, "Height": 5.8, "Score": 54},
    {"Name": "Wesley", "Age": 19, "Height": 5.7, "Score": 60}
]

table = tabulate(students, headers="keys", tablefmt="pipe")

print(table)
