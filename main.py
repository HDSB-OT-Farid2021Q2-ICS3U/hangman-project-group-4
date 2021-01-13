#the manin file
import wordlist

x = (wordlist.words)

makelist = x.split('\n')


def head():
    print ('  (o)')

def body():
    print(' |[]|')

def legs():
    print('  LL')

print('''  |
  |
  |''')
head()
body()
legs()
