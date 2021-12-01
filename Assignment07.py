# ------------------------------------------------- #
# Title: Assignment 07
# Description: A simple try-catch demo with pickling
# ChangeLog: (Who, When, What)
# KWong,11.30.2021,Created Script
# ------------------------------------------------- #
import pickle

# declare variables and constants
file_name = "GroceryList.dat" # An object that represents a file
dicRow = {}    # A row of data separated into elements of a dictionary {item, cost}
strChoice = '' # A Capture the user option selection

#try to open file and unpickle the data
try:
    strFile = open(file_name, "rb")
    dicRow = pickle.load(strFile) #unpickling
    print("Your current grocery list is: \n")
    for item, cost in dicRow.items():
        print(item, '-', cost)
    strFile.close()

# create file and add data to file
except FileNotFoundError as e:
    print("No data found! Let's get some data!")
    item = str(input("What item do you need? "))
    cost = str(input("How much does this item cost? " ))
    dicRow[item] = cost
    strFile = open(file_name, "wb")
    pickled_grocery = pickle.dump(dicRow, strFile) #pickle the data
    strFile.close()

# Processing
while True:
    print("""
    Menu of Options
    1) Add to dictionary
    2) Remove an existing item
    3) Save Data to File
    4) Exit Program
    """)
    strChoice = str(input("What would you like to do? "))
    # add data
    if strChoice == "1":
        item = str(input("What else would you like to add to your list? "))
        if item not in dicRow:
            cost = str(input("How much does this cost? "))
            dicRow[item] = cost
            print('\n', item, "has been added.")
        else:
            print("This item is already on your list! ")
        continue

    # delete data
    elif strChoice == "2":
        for item, cost in dicRow.items():
            print(item)
        item = str(input("Which item would you like to remove? "))
        try:
            del dicRow[item]
            print("n\Okay, I deleted", item)
        except:
            print(item, "does not exist!")

    # save file
    elif strChoice == "3":
        strFile = open(file_name, "wb")
        pickled_grocery = pickle.dump(dicRow, strFile)
        strFile.close()
        print("File saved.")

    # end loop
    elif strChoice == '4':
        break