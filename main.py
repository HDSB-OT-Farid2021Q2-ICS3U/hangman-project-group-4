# Author: Gary, Florian, Evan
# File name: main.py
# What it does: It is a hangman game that a single user can play. 
# Date programmed: 2021-1-15 (start)
# 2021-1-18 (rough work finished)

import os
import time
import wordlist
import random


# Clear function
clear = lambda: os.system('clear')


# Make a list of words to randomly choose from.
strWord = (wordlist.words) 
listWord = strWord.split('\n') 

# Color class. It is used to print colored texts.
class color():
    strDefualt = "\033[39m"
    strBlack = "\033[30m"
    strRed = "\033[31m"
    strGreen = "\033[32m"
    strYellow = "\033[33m"
    strBlue = "\033[34m"
    strMagenta = "\033[35m"
    strCyan = "\033[36m"

# Input: none
# Return Value: none  
# Limits: none
def welcome():
    """It prints the welcome message"""
    print(color.strBlue + 'Welcome to the hangman game!')
    input(color.strDefualt + 'Press enter to continue...')
    clear()
    print(color.strBlue + 'This is a single player game, so we will randomly choose a word from a list of 1000 words.')
    input(color.strDefualt + 'Press enter to continue...')
    clear()
    print(color.strBlue + 'Word generated! The game is ready!')
    input(color.strDefualt + 'Press enter to continue...')
    time.sleep(1)
    clear()


# Input: A boolean, "condition", as an argument.
# If condition == True, then it will proceed as you won the game.
# Else, it will proceed as you lost the game.
# Return Value: none
# Limits: none
def end(condition):
    """It prints the end-game message, according 
    to whether the user won the game or not."""
    if condition == True:
        print(color.strBlue + 'Congratulations! You won!')
        condition = input(color.strDefualt+ 'Press enter to continue...')
        clear()
    else:
        print(color.strRed + 'Sorry, you lost!')
        condition = input(color.strDefualt + 'Press enter to continue...')
        clear()

    print(color.strYellow + 'The game is finished!')
    

# Input: Two string arguments, word and guessedlett.
# The word is the word that the user needs to guess. The guessedlett is a 
# list of letters the user has gussed.
# Return Value: It returns the letter that the user needs to guess, 
# but for every word that the user did not successfully guessed, 
# it will hide that letter by printing an underscore instead.
# Limits: none  
def hidetheword(word, guessedlett):
    """The function prints the letter that the user needs to guess, 
    but for every word that the user did not successfully guessed, 
    it will hide that letter by printing an underscore instead."""
    lisOfWords = []
    guessedlet = [' ']
    guessedlet.extend(guessedlett)
    for i in word:

        if i in guessedlet :
            lisOfWords.append(i)
        else :
            lisOfWords.append('_')
    x = (' '.join(lisOfWords))
    return x


# Input: A integer input, lives.
# Return Value: none
# Limits: Lives variable can only be integers from 0 to 6 (inclusive).
def hp(intLives):
    """It outputs the hangman according 
    to the live the hangman has left."""
    if intLives == 0:
        print(color.strDefualt + "  ____   ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print("_|___    ")

    elif intLives == 1:
        print(color.strDefualt + "  ____   ")
        print(" |    |  ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print("_|___    ")

    elif intLives == 2:
        print(color.strDefualt + "  ____   ")
        print(" |    |  ")
        print(" |    O  ")
        print(" |       ")
        print(" |       ")
        print("_|___    ")

    elif intLives == 3:
        print(color.strDefualt + "  ____   ")
        print(" |    |  ")
        print(" |   _O_ ")
        print(" |       ")
        print(" |       ")
        print("_|___    ")

    elif intLives == 4:
        print(color.strDefualt + "  ____   ")
        print(" |    |  ")
        print(" |   _O_ ")
        print(" |    |  ")
        print(" |       ")
        print("_|___    ")

    elif intLives == 5:
        print(color.strDefualt + "  ____   ")
        print(" |    |  ")
        print(" |   _0_ ")
        print(" |    |  ")
        print(" |   /   ")
        print("_|___    ")

    elif intLives == 6:
        print(color.strDefualt + "  ____   ")
        print(" |    |  ")
        print(" |   _O_ ")
        print(" |    |  ")
        print(" |   / \ ")
        print("_|___    ")


# Input: none
# Return value: none
# Limit: none
def start():
    """The main part of the program. It prints the welcome message, 
    randomly chooses a word from the wordlist, 
    prints the hangman drawing, prints the word that hides letters 
    the user did not guess, 
    prints the list of letters the user guessed."""

    # Set up variables and start
    welcome()
    lisGuessed = []
    lisLetter = []
    intLives = 0
    strHideWord = listWord[(random.randint(0, 1000))]
    print(color.strBlue + 'starting')
    time.sleep(.25)
    clear()
    hidetheword(strHideWord,' ')

    # The body part. It repeats until the game is finished. 
    while True: 

        # It prints the hangman, displays the hidden word, 
        # and asks the user to input a letter.
        hp(intLives)
        print(hidetheword(strHideWord,lisLetter))
        print(f'The list of letters you guessed: {lisLetter}')
        strImp = input(color.strBlue + 'Input a letter you would guess: ')
        lisGuessed = [x for x in strImp]

        # Counts wrong answers and updates hangman's lives
        for i in lisGuessed: #check if is not enter
            if i != '': # if not empty character 
                for p in lisGuessed:
                    if p not in lisLetter:  # not a character thats already been picked
                        lisLetter.append(i)
                        intLives += sum([1 for o in lisGuessed if o not in strHideWord]) 
        
        # Clear the screen at the end of each iteration.
        clear()
        
        # If all hangman lives are lost,tell the user he lost and ask whether he wants to review the game.
        if intLives > 6:
            end(False)
            reviewGame = input(color.strDefualt + 'Would you like to review the game?(Y/N):\n')
            if reviewGame == 'Y':
                print(f'The correct word is: {strHideWord}')
                print('You guessed: ' + ', '.join(lisLetter))
            break


        # If all letters are guessed, tell the user he won and ask whether he wants to review the game.
        win = [i for i in hidetheword(strHideWord,lisLetter)] 
        if '_' not in win:
            end(True)
            reviewGame = input(color.strDefualt + 'Would you like to review the game?(Y/N):\n')
            if reviewGame == 'Y':
                print(f'The correct word is: {strHideWord}')
                print('You guessed: ' + ', '.join(lisLetter))
            break

# Run the start function
start()
