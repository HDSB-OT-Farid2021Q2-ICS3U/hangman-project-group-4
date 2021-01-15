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
