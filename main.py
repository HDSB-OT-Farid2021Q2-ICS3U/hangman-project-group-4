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

    
    def lives(lives)
    if lives == 1
        print("  ____   ")
        print(" |    |  ")
        print(" |       ")
        print(" |       ")
        print(" |       ")
        print("_|___    ")
        
    elif lives == 2
        print("  ____   ")
        print(" |    |  ")
        print(" |    O  ")
        print(" |       ")
        print(" |       ")
        print("_|___    ")

    elif lives == 3
        print("  ____   ")
        print(" |    |  ")
        print(" |   _O_ ")
        print(" |       ")
        print(" |       ")
        print("_|___    ")

    elif lives == 4
        print("  ____   ")
        print(" |    |  ")
        print(" |   _O_ ")
        print(" |    |  ")
        print(" |       ")
        print("_|___    ")

    elif lives == 5
        print("  ____   ")
        print(" |    |  ")
        print(" |   _O_ ")
        print(" |    |  ")
        print(" |   /   ")
        print("_|___    ")

    elif lives == 6
        print("  ____   ")
        print(" |    |  ")
        print(" |   _O_ ")
        print(" |    |  ")
        print(" |   / \ ")
        print("_|___    ")
