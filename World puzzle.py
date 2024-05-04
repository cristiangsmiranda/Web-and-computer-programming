# as a point of creativity, I learned and added a limit count of attempts that the player can have,
# however, I allowed these limit attempts not to be directly connected to the number of final attempts, 
# this allows that even after he gets it wrong 9 times, if he tries each letter individually and gets the word right,
# he won't get a "game over" on attempt number 10, but can continue on to victory.
# Another point of creativity was to add several word options, so each time the game starts,
# a new word has to be guessed
# Although the player can write down their guess using the whole word, I think it's more interesting to write down
# only the letter you think is right, so the letter will appear in the correct place to make the game simpler
# and understandable
import random
secret = ["elephant","giraffe","lion","chimpanzee","gorilla","kangaroo","panda","tiger","koala","leopard","zebra","snake"]
letter = random.choice(secret)
print()
print("Welcome to the word guessing game!")
print()
print("your hint is: Animals in the zoo.")
guesses = ""
attempts = 0
turns = 10
while turns > 0:
    attempts += 1
    failed = 0
    for character in letter:
        if character in guesses:
            print(character.upper(), end=" ")
        elif character in guesses:
            print(character.lower(), end=" ")
        else:
            print("_ ", end=" ")
            failed += 1
    if failed == 0:
        print()
        print("Congratulations! You guessed it!")
        break
    print()
    guess = input("What is your guess? Choose a letter that you think is correct: ")
    guesses += guess
    if guess not in letter:
        turns -= 1
        print("Your guess was not correct.")
        print("You have", + turns, 'more guesses') 
        if turns == 0:
            print("You Loose")
    print(f"It took you {attempts} guesses ")

