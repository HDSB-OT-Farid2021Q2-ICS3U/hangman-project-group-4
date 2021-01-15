#the manin file

# TODO: Check if the letter is contained @Florian
# TODO: Hide the word @Florian


# TODO: Draw hangman @Evan
# TODO: Import a list of words @Evan


# TODO: Welcome (introduction) message @Gary
# TODO: End game (conclusion) message @Gary


import os
import wordlist
clear = lambda: os.system('clear')

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

x = (wordlist.words)

# A list of words
makelist = x.split('\n')

# Different parts of hangman
def hang():
   print('''  |
  |
  |''')

def head():
    print ('  (o)')

def arms():
    print(' |[]|')

def body():
    print('  []')

def legs():
    print('  LL')


# Hideword function
def hideword(word, guessedlett):
    lisofwords = []
    guessedlet = [' ']
    sep = ''
    guessedlet.extend(guessedlett)
    for i in word:

        if i in guessedlet :
            lisofwords.append(i)
        else :
            lisofwords.append('_')
    print(''.join(lisofwords))
    
    
# welcome message
def welcome():
    print(color.red + 'Welcome to the hangman game!' + color.red)
    continueProgram = input(color.defualt + 'Press enter to continue...' + color.defualt)
    clear()
    print(color.blue + 'This is a single player game, so we will randomly choose a word from a list of 1000 words.' + color.blue)
    continueProgram = input(color.defualt + 'Press enter to continue...' + color.defualt)
    clear()
    print(color.magenta + 'Word generated! The game is ready!' + color.magenta)
    continueProgram = input(color.defualt + 'Press enter to continue...' + color.defualt)
    clear()


# end message
def end():
    if winTheGame == True:
        print(color.blue + 'Congratulations! You won!' + color.blue)
        continueProgram = input(color.defualt+ 'Press enter to exit the game...' + color.defualt)
        clear()
    else:
        print(color.red+ 'Sorry, you lost!' + color.red)
        continueProgram = input(color.defualt+ 'Press enter to exit the game...' + color.defualt)
        clear()
    print(color.yellow + 'The game is finished!' + color.yellow)

