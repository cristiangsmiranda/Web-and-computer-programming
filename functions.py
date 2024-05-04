def get_initial(name):
    initial = name[0:1].upper()
    return initial
first_name = input("enter your first name: ")
first_name_initial = get_initial(first_name)
print("your initial is: " + first_name_initial)


def a_phrase_regular(phrase):
    print(phrase)
def a_phrase_upper(phrase):
    new_phrase = phrase.upper()
    print(new_phrase)
def a_phrase_lower(phrase):
    new_phrase = phrase.lower()
    print(new_phrase)
your_phrase = input("What is your message? ")
a_phrase_regular(your_phrase)
a_phrase_upper(your_phrase)
a_phrase_lower(your_phrase)




import math

def compute_area_square(side):
    return side * side

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return math.pi * radius * radius

choice = ""

while choice != "quit":
    print("Choose one of the options: Square, Rectangle, Circle")
    choice = input("What do you want? ")
    if choice.lower() == "square":
        length = float(input("What is the length of the side? "))
        area = compute_area_square(length)
        print(f"The area is {area}")
    elif choice.lower() == "rectangle":
        length = float(input("What is the length? "))
        width = float(input("What is the width? "))
        area = compute_area_rectangle(length, width)
        print(f"The area is {area}")
    elif choice.lower() == "circle":
        radius = float(input("What is the radius? "))
        area = compute_area_circle(radius)
        print(f"The area is {area}")