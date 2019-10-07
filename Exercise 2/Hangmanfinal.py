import random
import sys

words = ["python", "computer", "software", "desktop", "screen", "code", 
            "program", "mouse", "keyboard", "headphones", "dongle", "adapter", 
            "tablet", "socket", "cable"
           ]

guesses = []
secretword = random.choice(words) 
length = len(secretword)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter = []

print("Let's play hangman!!")

def change():

    for character in secretword: 
        guesses.append("-")

    print("The word you need to guess has", length, "characters")

    print("You may enter only 1 letter at a time\n")

    print(guesses)

def guessing():
    turns = 1

    while turns < 5:

        guess = input("Pick a letter\n").lower()

        if guess not in alphabet: 
            print("Enter a letter from a-z")
        elif guess in letter: 
            print("You have already guessed that letter!")
        else: 

            letter.append(guess)
            if guess in secretword:
                print("You guessed correctly!")
                for x in range(0, length): 
                    if secretword[x] == guess:
                        guesses[x] = guess
                        print(guesses)

                if not '-' in guesses:
                    print("You won!")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                turns += 1
                if turns == 5:
                    print("Sorry you lost :( The word was", secretword)

change()
guessing()

print("GAME OVER!")
