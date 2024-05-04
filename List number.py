print()
numbers = []
number = -1
total = 0
average = 0
largest = -99999
smallest = 99999

print('Please enter a list of numbers, type 0 when finished: ')

while number != 0:
    number = int(input("Enter number: "))
    if number != 0:
        numbers.append(number)
print()
for number in numbers:
    total+=number
    if largest<number:
       largest=number
    if 0<number:
        if smallest>number:
            smallest=number   
print (f'The sum is: {total}')
print()
average = total / (len(numbers))
print (f'The average is: {average}')
print (f' The largest number is: {largest}')
print (f' The smallest number is: {smallest}')
print (f' The sorted list is: ')
sorted = numbers.sort()
for number in numbers:
    print (number)