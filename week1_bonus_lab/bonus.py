#Erick Cordon

#Calulator Bonus

#--------------------------------------------------------------------------------------------------------------------------------------

#Functions
def menu():

    print("SEARCH MENU")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    print("3. Exit")

    pick = input("Hello, Please make a selection from the following below [1-3]: ")

    while pick != "1" and pick != "2" and pick != "3":
        print("\nSorry...An invalid input was made. Please try again")

        pick = input("Hello, Please make a selection friom the following below [1-5]: ")

    return pick
#--------------------------------------------------------------------------------------------------------------------------------------
print("Welcome to the Calculator!")

answer = "y"

while answer =="y":

    choice = menu()

    if (choice == 3):
        print("choice 3 was made")
        answer = input("Would you like to continue? y/n: ")

print("Exit")