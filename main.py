# Author: Gary, Florian, Evan
# File name: main.py
# What it does: It is a hangman game that a single user can play. 
# Date programmed: 2021-1-15 (start)
# 2021-1-18 (rough work finished)

import os
import time
import wordlist
import random

clear = lambda: os.system('cls')
word = (wordlist.words)
makelist = word.split('\n')

# Color class
class color():
    defualt = "\033[39m"
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"

# Input: This function does not take any argument.
# Return Value: none  
# What It Does: It prints the welcome message at the very start of the 
# program. It prints a sentence each time and asks the user to press enter 
# once they finish reading the line and want to proceed. 
# Limits: none
def welcome():
    print(color.red + 'Welcome to the hangman game!')
    input(color.defualt + 'Press enter to continue...')
    clear()
    print(color.blue + 'This is a single player game, so we will randomly choose a word from a list of 1000 words.')
    input(color.defualt + 'Press enter to continue...')
    clear()
    print(color.magenta + 'Word generated! The game is ready!')
    input(color.defualt + 'Press enter to continue...')
    time.sleep(1)
    clear()

# Input: This function takes a boolean, "condition", as an argument.
# If condition == True, then it will proceed as you won the game.
# Else, it will proceed as you lost the game.
# Return Value: none
# What It Does: It prints the end message at the end of the 
# program. It prints a sentence each time and asks the user to press enter 
# once they finish reading the line and want to proceed. 
# Limits: none
def end(condition):
    if condition == True:
        print(color.blue + 'Congratulations! You won!')
        condition = input(color.defualt+ 'Press enter to exit the game...')
        clear()
    else:
        print(color.red+ 'Sorry, you lost!')
        condition = input(color.defualt+ 'Press enter to exit the game...')
        clear()

    print(color.yellow + 'The game is finished!')
    

# Input: This function takes two string arguments, word and guessedlett.
# The word is the word that the user needs to guess. The guessedlett is a 
# collection of letters the user has gussed.
# Return Value: It returns the letter that the user needs to guess, 
# but for every word that the user did not successfully guessed, 
# it will hide that letter by printing an underscore instead.
# What it does: The function prints the letter that the user needs to guess, 
# but for every word that the user did not successfully guessed, 
# it will hide that letter by printing an underscore instead.
# Limits: none  
def hidetheword(word, guessedlett):
    
    lisofwords = []
    guessedlet = [' ']
    guessedlet.extend(guessedlett)
    for i in word:

        if i in guessedlet :
            lisofwords.append(i)
        else :
            lisofwords.append('_')
    x = (' '.join(lisofwords))
    return x


# Input: This function takes a int input, lives.
# Return Value: none
# What it does: It outputs the hangman, 
# according to the live the hangman has left.
# Limits: lives variable can only be integers from 1 to 6 (inclusive).
def hp(lives) :

    if lives == 1:
        print("  ____   ")
        print(" |    |  ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print("_|___    ")

    elif lives == 2:
        print("  ____   ")
        print(" |    |  ")
        print(" |    O  ")
        print(" |       ")
        print(" |       ")
        print("_|___    ")

    elif lives == 3:
        print("  ____   ")
        print(" |    |  ")
        print(" |   _O_ ")
        print(" |       ")
        print(" |       ")
        print("_|___    ")

    elif lives == 4:
        print("  ____   ")
        print(" |    |  ")
        print(" |   _O_ ")
        print(" |    |  ")
        print(" |       ")
        print("_|___    ")

    elif lives == 5:
        print("  ____   ")
        print(" |    |  ")
        print(" |   _O_ ")
        print(" |    |  ")
        print(" |   /   ")
        print("_|___    ")

    elif lives == 6:
        print("  ____   ")
        print(" |    |  ")
        print(" |   _O_ ")
        print(" |    |  ")
        print(" |   / \ ")
        print("_|___    ")


# Input: none
# Return value: none
# What it does: It prints the welcome message, 
# randomly choose a word from the wordlist, 
# and prints the word that hides letters the user did not guess.
# Limit: none
def start():

    welcome()
    guessed = []
    letter = []
    lives = 0
    hideword = makelist[(random.randint(0, 1000))]
    print(color.blue + 'starting')
    time.sleep(.5)
    clear()
    hidetheword(hideword,' ')

    while True : 
        hp(lives)
        print(hidetheword(hideword,letter))
        print(hideword)
        print(letter)

        imp = input('guess letter? ')

        guessed = [x for x in imp]

        for i in guessed: #check if is not enter
            if i != '': # if not empty character 
                for p in guessed:
                    if p not in letter:  # not a character thats already been picked
                        letter.append(i)
                        lives += sum([1 for o in guessed if o not in hideword]) #count wrong answers and addes lives
        
        clear()
        hp(lives)
        time.sleep(1.5)
        clear()

        #lose condition
        if lives > 6 :
            end(False)
            break
        #win condition if all guessed
        win = [i for i in hidetheword(hideword,letter)] 
        if '_' not in win :
            end(True)
            break


start()
