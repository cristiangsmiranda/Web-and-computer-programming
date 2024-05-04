# While doing this work, I decided that it would be interesting to make a donation fee one of the main principles,
# of eating at this restaurant. so every family that decides to go to the restaurant knows that
# they can make a donation at the end of their meal.
child_meal = float(input("what is the price of a child's meal? "))
adult_meal = float(input("what is the price of a adult's meal? "))
children = int(input("how many children are there? "))
adults = int(input("how many adults are there? "))
subtotal = child_meal * children + adult_meal * adults
print(f"the subtotal is: ${subtotal:.2f}")
print()
sale_tax = float(input("what is the sales tax rate in percent? "))
total_with_tax = subtotal / sale_tax + subtotal
print(f"total: ${total_with_tax:.2f}")
print()
payment = float(input("what is the payment amount? "))
change = payment - total_with_tax
print(f"your change is: ${change:.2f}")
print()
print("As you have chosen to eat in our restaurant,")
print("you know that all our customers have the opportunity to do")
print("something charitable by donating a sum of money to the city's nursing homes.")
donate = float(input("How much would you like to donate? "))
print(f"then, the final value is: ${donate + total_with_tax:.2f}")
print(f"your final change is: ${payment - donate + total_with_tax:.2f}")