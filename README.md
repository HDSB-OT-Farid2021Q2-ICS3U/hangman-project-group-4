[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=350249&assignment_repo_type=GroupAssignmentRepo)

# Gaming instructions

This is an online, single-player hangman game. If you are not familiar with the game rule, read the "Game Rule" section below.

Although this product can work on most computers, it is recommended that you check the "Hardware Requirement" section below.

Make sure that your computer can run Python files. If you don't know how to do so, read the "Software Requirement and Guide" section. 

Download the github repository. You will need the main.py and wordlist.py files. Put those files 
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

# Game Rule

The computer will randomly choose a word from a wide list of words. You will only know the length of that word. 
You need to guess the word by inputting a letter each time.
If the letter you inputted is contained in the word, then you will know the position(s) of that letter in the word.
If the letter you guessed is not contained, then you will be informed that you made an incorrect guess and the hangman
will lose one live. After seven incorrect attempts, the hangman will lose all its lives and the game is lost. If you guessed
the entire word before the hangman lost all his lives, you win the game.

# Harware Requirement

A functioning computer with a keyboard and a mouse is necessary. 

# Software Requirement and Guide

This game is coded using Python. You will need an editor and a compiler that can compile Python files. Repl or VS Code are recommended.

# Questions and Concerns

If you have any questions or concerns about how to play the game, feel free to contact us. 
