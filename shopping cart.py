# I've added a system that allows you to collect and store prices and items at the same time, using
# a question and answer pattern with yes or no to follow the shopping list loop.

# I've added a farewell system if the number chosen by the participant is not between 1 and 5,
# this way, in addition to the list closing, it will say why it's closing.
print("Welcome to the Shopping Cart Program!")
print()
print("Please select one of the following: ")
print("1. Add item")
print("2. View cart")
print("3. Remove item")
print("4. Compute total")
print("5. Quit")
print()
options = int(input("Please enter an action: "))
while options > 0 and options < 6:
    if options == 1:
        things = []
        prices = []
        items = None
        choose = None
        while choose != "no":
            items = input ("(What item would you like to add? ")
            value = float(input("how much cost the item? "))
            things.append(items)
            prices.append(value)
            choose = input("do you want to add other product? (type: yes/no):  ")

        print()
        print("Please select one of the following: ")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")
        print()
        options = int(input("Please enter an action: "))
    elif options == 2:
        print()
        print("The shopping list is: ")
        for i in range(len(things)):
            items = things[i]
            value = prices[i]
            print(f"{i+1}. {items} - ${value}")
            
        print()
        print("Please select one of the following: ")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")
        print()
        options = int(input("Please enter an action: "))
    elif options == 3:
        print()
        index = int(input("Which item would you like to remove? "))
        index = index - 1
        things.pop(index)
        prices.pop(index)

        print("The shopping list is:")
        for i in range(len(things)):
            items = things[i]
            value = prices[i]
            print(f"{i+1}. {items} - ${value}")
        
        print()
        print("Please select one of the following: ")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")
        print()
        options = int(input("Please enter an action: "))
    elif options == 4:
        total = 0
        print()
        for value in prices:
            total += value
        print (f"The total is: {total:.2f}")

        print()
        print("Please select one of the following: ")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")
        print()
        options = int(input("Please enter an action: "))
    elif options == 5:
        print("thank you, good bye!")
        break
else:
    print("Your choice is not correct. try again")
