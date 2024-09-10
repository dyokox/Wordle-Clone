from wordList import words
import random
import colorama
from colorama import Fore, Style

colorama.init()


print("=-=-=-=-=-= I N F O =-=-=-=-=-=\n Wordle clone made in Python, CLI.\n R U L E S\n 1. You have 5 lives\n 2. Each guess of the word is one life 3. Have fun ")

# global variable
lives = 0
count = 5

# color the word if it has any letters in the random word etc
# RED it doesn't, YELLOW it has but misplaced and GREEN its in the right place
def wordColor(userGuess, randomWord):

    global lives
    for i in range(len(userGuess)):
        if userGuess[i] == randomWord[i]:
            print(Fore.GREEN + userGuess[i], end="")
        elif userGuess[i] in randomWord:
            print(Fore.YELLOW + userGuess[i], end="")
        else:
            print(Fore.RED + userGuess[i], end="")	
    print(Style.RESET_ALL)	

# function if the player wants to continue playing
def resumeGame():
    while True:
        choice = input("Start again? (y/n)\n >> ").lower()
        if choice == "y":
            continue
        elif choice == "n":
            break
        else: 
            print("invalid choice")

# the actual game
def main():
    global lives
    lives = 0
    randomWord = random.choice(words)

    while lives < 5:            
        userGuess = input("\nGuess:\n >> ")

        if len(userGuess) == 5:
            if userGuess == randomWord:
                print(f"You won the word was {userGuess}")
                break
            else:
                wordColor(userGuess, randomWord)
                lives += 1
        else:
            print(f"\nThe word {userGuess} is not 5 letters\n")

        if lives >= 5:
            print(f"You lost, the word was {randomWord}\n") 
            break
        
# making the game work        
while True:
    main()
    if not resumeGame():
        print("Thanks for playing")
        break