[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=350249&assignment_repo_type=GroupAssignmentRepo)
# Hangman Assignment

Use this file as a README documentation (edit me!)

# Developers

This game was developed by Gary, Florian and Evan.

# Game Rule

The computer will randomly choose a word from a list of 1000 words. You will only know the length of that word. 
You need to guess the word by inputting a letter each time.
If the letter you inputted is contained in the word, then you will know the position(s) of that letter in the word.
If the letter you guessed is not contained, then you will be informed that you made an incorrect guess and the hangman
will lose one live. After six incorrect attempts, the hangman will lose all 6 lives and the game is lost. If you guessed
the entire word using less than six lives, you win the game.

# How to play

This is an online, single-player hangman game. If you are not familiar with the game rule, read the "Game Rule" section above.

This game is coded using Python. You will need an editor and a compiler that can compile Python files. Repl and VS Code are recommended.
Once you have one of those two ready, download the github repository. You will need the main.py and wordlist.py files. Put those files 
on your editor, and run the main.py file. 

Once you run the main.py file, the game starts. First, it will display a series of introduction messages. Once you finish reading
what is displayed on the terminal, press enter the continue. 

At the top, the program shows you the hangman drawing (the hangman drawing will only be visible after you guessed at least one word).
The program will display the word, with each letter you have not guessed replaced by "_". The next line displays a list of all 
letters you have guessed, regardless of whether your guess is correct or not. Lastly, it will ask you to input another letter you want 
to guess. Press enter once you finish inputting the letter. 

The hangman drawing will be updated each time you incorrectly input a letter. The word will display the letter 
you just guessed if you guessed correctly. The list of letters you guessed will be updated every time. 

If you guessed all letters before the hangman drawing is finished, the program will proceed to end the game.
The game will also end if all hangman lives are lost. 
