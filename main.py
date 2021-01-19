# Author: Gary, Florian, Evan
# File name: main.py
# What it does: It is a hangman game that a single user can play. 
# Date programmed: 2021-1-15 (start)
# 2021-1-18 (rough work finished)

import os
import time
import wordlist
import random


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
    lisOfWords = []  # The word the user is trying to guess
    guessedlet = [' '] # A list of letters the user guessed
    guessedlet.extend(guessedlett)
    for i in word:
        if i in guessedlet :
            lisOfWords.append(i)
        else :
            lisOfWords.append('_')
    # The formatted word the user is trying to guess
    x = (' '.join(lisOfWords)) 
    return x


# Input: A integer input, lives.
# Return Value: none
# Limits: Lives variable can only be integers from 0 to 6 (inclusive).
def hp(intLives):
    """It outputs the hangman according 
    to the live the hangman has left."""
    if intLives == 0:
        print(color.strDefualt + "  ____   \n |       \n |       \n |       \n |       \n_|___    ")

    elif intLives == 1:
        print(color.strDefualt + "  ____   \n |    |  \n |       \n |       \n |       \n_|___    ")

    elif intLives == 2:
        print(color.strDefualt + "  ____   \n |    |  \n |    O  \n |       \n |       \n_|___    ")

    elif intLives == 3:
        print(color.strDefualt + "  ____   \n |    |  \n |   _O  \n |       \n |       \n_|___    ")

    elif intLives == 4:
        print(color.strDefualt + "  ____   \n |    |  \n |   _O_ \n |       \n |       \n_|___    ")

    elif intLives == 5:
        print(color.strDefualt + "  ____   \n |    |  \n |   _O_ \n |    |  \n |       \n_|___    ")

    elif intLives == 6:
        print(color.strDefualt + "  ____   \n |    | \n |   _O_ \n |    |  \n |   /   \n_|___    ")

    elif intLives == 7:
        print(color.strDefualt + "  ____   ")
        print(" |    |  \n |   _O_ \n |    |  \n |   / \ \n_|___    ")


# Clear screen for different OS
print('Before playing the game, you need to answer this question:')
print('What is your Operating System?')
print('1. Windows')
print('2. Mac')
print('3. Linux')
userOS = input('My Operating System is (enter a number): ') 
if userOS == '1':
    clear = lambda: os.system('cls')
    print('Your OS is Windows.')
elif userOS == '2':
    clear = lambda: os.system('clear')
    print('Your OS is Mac.')
else:
    clear = lambda: os.system('cls')
    print('Your OS is Linux.')
time.sleep(.5)
clear()


# Prints the welcome message
welcome()


# Loops the game as long as the user wants to play.
while True:


    # Set up variables and start
    strWord = (wordlist.words) 
    listWord = strWord.split('\n') 
    lisGuessed = [] # The current letter the user guessed 
    lisLetter = [] # The list of letters the user guessed
    intLives = 0 # Lives of hangman
    # The word the user needs to guess
    strHideWord = listWord[(random.randint(0, 1000))]  
    print(color.strBlue + 'starting')
    time.sleep(.25)
    clear()
    hidetheword(strHideWord,' ')


    # The body part. It repeats until the current game is finished. 
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
                

        # If all hangman lives are lost,tell the user 
        # he lost and ask whether he wants to review the game.
        if intLives > 6:
            hp(7)
            end(False)
            print(color.strDefualt + 'Would you like to review the game?')
            print('1. Yes! I would like to know the word!')
            print('2. No. Knowing that I lost is painful enough for me.')
            reviewGame = input('Enter a number: ')
            if reviewGame == '1':
                clear()
                print(f'The correct word is: {strHideWord}')
                time.sleep(1)
                print('You guessed: ' + ', '.join(lisLetter))
            print('')
            break


        # If all letters are guessed, tell the user he won and ask whether he wants to review the game.
        win = [i for i in hidetheword(strHideWord,lisLetter)] 
        if '_' not in win:
            end(True)
            print(color.strDefualt + 'Would you like to review the game?')
            print('1. Yes! I would like to see my guesses!')
            print('2. No. Knowing that I won is enough.')
            reviewGame = input('Enter a number: ')
            if reviewGame == '1':
                clear()
                print(f'The correct word is: {strHideWord}')
                time.sleep(1)
                print('You guessed: ' + ', '.join(lisLetter))
            print('')
            break


    # Ask the user whether he wants to play again 
    print('Would you like to play again?')
    print('1. Yes, I would like to play again!')
    print('2. No, End the program!')
    if input('Enter a number: ') == '2':
        clear()
        print('The program has ended!')
        break
    else:
        print('You chose to play the game again!')
        time.sleep(1)
        clear()
