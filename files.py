#with open("books.txt") as books:
#    for line in books:
#        books = line.strip()
#        print(line)
    
#    print("goodbye")

#print("the file is closed now.")


#colors = "red green blue yellow"
#color_parts = colors.split()
#print(colors)
#print(color_parts)

#for color in color_parts:
#    print(color)

#second = color_parts [1]
#print(second)

## nesse caso, se seguir o memso exemplo, ao colocar o "E" no split,
## todas as letras "E" no sistema irão desaparecer.
#colors = "red green blue yellow"
#color_parts = colors.split("e")
#print(colors)
#print(color_parts)

## se fizer qualquer alteraação nos espaços do "name" (porém, sem bagunçar o nome)
## a função ".strip" no "clear_name" vai deixar intacto.
#name = "      Cristian Miranda      "
#clear_name = name.strip()
#print(f"-----{name}-----")
#print(f"-----{clear_name}-----")


#numbers = [42, 25, 18, 83, 23, 85, 38, 2]

#largest_so_far = numbers[0]
#for number in numbers:
#    if number > largest_so_far:

#        largest_so_far = number
#print(f"The largest is: {largest_so_far}")



#shopping_cart = [["Chips", 2.99],["Bread", 2.50],["Milk", 3.19],
#["Ice Cream", 6.99],["Cheese", 5.99],["Candy bar", 0.99]]

#max_price = -1
#for item in shopping_cart:
#    price = item[1]

#    if price > max_price:
#        max_price = price
#print(f"The maximum price is: {max_price}")

#max_price = -1
#max_product = ""
#for item in shopping_cart:
#    product_name = item[0]
#    price = item[1] 

#    if price > max_price:
#        max_price = price
#        max_product = product_name

#print(f"The maximum price is: {max_price}")
#print(f"The product with the maximum price is: {max_product}")



#Itere pela lista e exiba cada string na tela.
#Divida a string em nome e idade e imprima-os na tela
#Encontre a idade que é a mais jovem.
#Mantenha o controle do nome da pessoa mais jovem.

people = ["Stephanie 36","John 29","Emily 24","Gretchen 54",
"Noah 12","Penelope 32","Michael 2","Jacob 10"]

yongest_age = 99999
yongest_name = ""
for person in people:
    parts = person.split() 
    name = parts[0]
    age = int(parts[1]) 

    if age < yongest_age:
        yongest_age = age
        yongest_name = name
print(f"The yongest people is: {yongest_name}")
print(f"The yongest age is: {yongest_age}")