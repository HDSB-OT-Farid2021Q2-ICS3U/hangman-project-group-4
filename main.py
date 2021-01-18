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

# end message
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
    
def hidetheword(word, guessedlett):
    
    lisofwords = []
    guessedlet = [' ']
    sep = ''
    guessedlet.extend(guessedlett)
    for i in word:

        if i in guessedlet :
            lisofwords.append(i)
        else :
            lisofwords.append('_')
    x = (''.join(lisofwords))
    return x

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

def start():

    #welcome()
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
            if i != '':
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


