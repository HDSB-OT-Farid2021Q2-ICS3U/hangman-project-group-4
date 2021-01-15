#the manin file



def hideword(word, guessedlett):
    lisofwords = []
    guessedlet = [' ']
    sep = ''

    for x in guessedlett :
        guessedlet.append(x)

    
    for i in word:

        if i in guessedlet :
            lisofwords.append(i)
        else :
            lisofwords.append('_')


    print(','.join(lisofwords))

