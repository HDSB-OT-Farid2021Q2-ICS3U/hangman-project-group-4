#the manin file

# TODO: Check if the letter is contained @Florian
# TODO: Hide the word @Florian


# TODO: Draw hangman @Evan
# TODO: Import a list of words @Evan


# TODO: Welcome (introduction) message @Gary
# TODO: End game (conclusion) message @Gary


import os
clear = lambda: os.system('clear')


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
    print('Welcome to the hangman game!')
    continueProgram = input('Press enter to continue...')
    clear()
    print('This is a single player game, so we will randomly choose a word from a list of words.')
    continueProgram = input('Press enter to continue...')
    clear()
    print('Word generated! The game is ready!')
    continueProgram = input('Press enter to start the game!')
    clear()


# end message
def end():
    if winTheGame == True:
        print('Congratulations! You won!')
        continueProgram = input('Press enter to continue...')
        clear()
    else:
        print('Sorry, you lost!')
        continueProgram = input('Press enter to continue...')
        clear()
    print('The game is finished!')

