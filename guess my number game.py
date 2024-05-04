import random
again = "yes"

while again == "yes":
    number = random.randint(1, 10)
    guess = 0
    attempts = 0
    while guess != number:
        guess = int(input(f"choice a number between 1 until 10: "))
        attempts = attempts + 1
        if guess > number:
            print(f"the number is smaller! ")
        elif guess < number:
            print(f"the number is higher! ")

    print(f"you got it right. congratulations")
    print(f"the number of attempts was: {attempts} ")
    again = input("do you want to try again? yes/no ")