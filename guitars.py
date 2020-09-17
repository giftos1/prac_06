from practical_6.guitar import Guitar
"""Run program with reference to Guitar class"""

guitars = []  # create an empty list
print("My guitars !")
name = input("Name: ")
while name != "":
    year = int(input("Year "))
    cost = float(input("Cost: $"))
    print(name, "({}) : {:,.2f} added".format(year, cost))  # print input information as per the format

    guitar_information = Guitar(name, year, cost)
    guitars.append(guitar_information)  # Adds new guitar information to the empty list
    name = input("Name: ")
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
print()
print("Name:\n\n...snip...")
print()

