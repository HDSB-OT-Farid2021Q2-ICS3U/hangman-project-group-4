# Author: Gary, Florian, Evan
# File name: main.py
# What it does: It is a hangman game that a single user can play. 
# Date programmed: 2021-1-15 (start)
# 2021-1-18 (rough work finished)

import os
import time
import wordlist
import random

clear = lambda: os.system('clear')
strWord = (wordlist.words) 
listWord = strWord.split('\n') # The list of words to randomly choose from

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

# Input: This function does not take any argument.
# Return Value: none  
# What It Does: It prints the welcome message at the very start of the 
# program. It prints a sentence each time and asks the user to press enter 
# once they finish reading the line and want to proceed. 
# Limits: none
def welcome():
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
        print(color.strBlue + 'Congratulations! You won!')
        condition = input(color.strDefualt+ 'Press enter to exit the game...')
        clear()
    else:
        print(color.strRed + 'Sorry, you lost!')
        condition = input(color.strDefualt + 'Press enter to exit the game...')
        clear()

    print(color.strYellow + 'The game is finished!')
    

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


# Input: This function takes a int input, lives.
# Return Value: none
# What it does: It outputs the hangman, 
# according to the live the hangman has left.
# Limits: lives variable can only be integers from 1 to 6 (inclusive).
def hp(intLives) :

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
        print(" |   _O_ ")
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
# What it does: It runs the program. It prints the welcome message, 
# randomly chooses a word from the wordlist, 
# prints the hangman drawing, 
# prints the word that hides letters the user did not guess, 
# prints the list of letters the user guessed.
# Limit: none
def start():

    welcome()
    lisGuessed = []
    lisLetter = []
    intLives = 0
    strHideWord = listWord[(random.randint(0, 1000))]
    print(color.strBlue + 'starting')
    time.sleep(.25)
    clear()
    hidetheword(strHideWord,' ')

    while True : 
        hp(intLives)
        print(hidetheword(strHideWord,lisLetter))
        # print(strHideWord)
        print(f'The list of letters you guessed: {lisLetter}')

        strImp = input(color.strBlue + 'Input a letter you would guess: ')

        lisGuessed = [x for x in strImp]

        for i in lisGuessed: #check if is not enter
            if i != '': # if not empty character 
                for p in lisGuessed:
                    if p not in lisLetter:  # not a character thats already been picked
                        lisLetter.append(i)
                        intLives += sum([1 for o in lisGuessed if o not in strHideWord]) #count wrong answers and addes lives
        
        clear()
        hp(intLives)
        time.sleep(.5)
        clear()

        #lose condition
        if intLives > 6 :
            end(False)
            print(f'The correct word is: {strHideWord}')
            break
        #win condition if all guessed
        win = [i for i in hidetheword(strHideWord,lisLetter)] 
        if '_' not in win :
            end(True)
            break


start()
