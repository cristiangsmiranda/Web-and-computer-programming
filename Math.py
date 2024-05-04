#first_num = input ('enter the fisrt number: ')
#second_num = input ('enter se second number: ')
#print(int(first_num) - int(second_num))

#first_num = 5
#second_num = 6
#print(first_num + second_num)

#age = int(input(' how old are your? '))
#next_year_age = age + 1
#print(f'On your next birthday, you will be {next_year_age}')

#egg_cartons = int(input(' how many egg cartons do you have? '))
#cartons = egg_cartons * 12
#print(f'you have {cartons} eggs')

#cookies = int(input('how many cookies do you have? '))
#people = int(input('how many peoaple are there? '))
#cookies_per_people = cookies / people
#print(f'each person may have {cookies_per_people} cookies')

#Fahrenheit = int(input('what is the temperature in fahrenheit? '))
#value = (Fahrenheit - 32) * 5/9
#print(f'the temperature in Celsius is: {value:.1f} degrees. ')

print()
#o calculo com a base do quadrado nas 3 linhas abaixo são do trabalho em equipe
length = int(input('what is the length of a side of the square? '))
square = length ** 2
print(f'the area of the square is: {square}')
print()
#o calculo com a base do retangulo nas 4 linhas abaixo são do trabalho em euipe
length = int(input('what is the length of rectangle? '))
width = int(input('what is the width of the rectangle? '))
rectangle = length * width
print(f'The area of the rectangle is: {rectangle}')
print()
#o calculo com a area do circulo nas 4 linhas abaixo são do trabalho em equipe
pi = 3.14
radius = int(input('What is the radius of the circle? '))
area_circle = (radius ** 2) * pi
print(f'The area of the circle is: {area_circle}')
print()
#atividade referente ao stretch challenge 1
import math
radius = int(input('What is the radius of the circle? '))
area_circle_precisao = (radius ** 2) * math.pi
print(f'vThe area of the circle is: {area_circle_precisao}')
print()
#atividade referente ao streach challenge 2
import math
value = int(input('What is the value to be used? '))
area_square = value ** 2
area_circle = math.pi * (value ** 2)
volume_cube = value ** 3
volume_sphere = (4 / 3) * math.pi * (value ** 3)
print(f'Area of a square: {area_square}')
print(f'Area of a circle: {area_circle}')
print(f'Volume of a cube: {volume_cube}')
print(f'Volume of a sphere: {volume_sphere}')
print()
#atividade referente ao streach challenge 3
#area do quadrado
side = int(input('what is the length of a side of the square in cm? '))
area = side ** 2
print(f"The area of the square is: {area} cm^2")
print(f"The area of the square is: {area / 10000} m^2")
print()
#area do retangulo
length = int(input('what is the length of the rectangle in cm? '))
width = int(input('what is the width of the rectangle in cm? '))
area = length * width
print(f'the area of the rectangle is: {area} cm^2')
print(f'the area of the rectangle is: {area / 10000} m^2')
#area do circulo
pi = 3.14
radius = int(input('what is the radius of the circle in cm? '))
area = (radius ** 2) * pi
print(f'the area of the circle is: {area} cm^2 ')
print(f'the area of the circle is: {area / 10000} m^2 ')