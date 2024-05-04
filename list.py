#friends = []
#name = None
#
#while name != "end":
#    name = input("Type the name of a friend: ")

#    if name != "end":
#        friends.append(name)
#print()
#print("Your friends are:")
#for friend in friends:
#    print(friend)



#Faça um loop pelos itens da maneira normal (por exemplo, for thing in the_list)
#e exiba cada um deles para ter certeza de que a lista inicial foi criada corretamente.

#Adicione outro loop para percorrer e imprimir os itens da lista, mas, dessa vez,
#em vez de usar a sintaxe for ... in, use um índice (por exemplo, for ... in range) e acesse
#o item usando o índice e os colchetes. Imprima o índice na frente dos itens da seguinte forma: 0. Milk

#Peça ao usuário um índice e um novo item da lista de compras. Substitua o item nesse
#índice pelo novo item. Em seguida, exiba a lista inteira novamente.

things = []
items = None
while items != "quit":
    items = input ("Please enter the items of the shopping list (type: quit to finish): ")

    if items != "quit":
        things.append(items)
print()
print("The shopping list is: ")
for items in things:
    print(items)
print()
print("The shopping list with indexes is:")
for i in range(len(things)):
    items = things[i+1]
    print(f"{i+1}. {items}")

print()
index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

things[index] = new_item

print("The shopping list with indexes is:")
for i in range(len(things)):
    item = things[i]
    print(f"{i}. {item}")







