# -*- coding: utf-8 -*-
"""cs_py_rock_paper_scissor.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1liDVh471jHmnrrdvkInLJ06fTsQK9ADP
"""

import random

print("Welcome to the game of Rock-Paper-Scissors")

def play(user_input):
    inputs_list = ['rock','paper','scissor']
    computer_input = random.choice(inputs_list)

    if user_input == 'r' and computer_input == 'paper':
        print(f"use choose {user_input} and computer choose {computer_input}\nComputer Wins")
    if user_input == 'r' and computer_input == 'scissor':
        print(f"use choose {user_input} and computer choose {computer_input}\nUser Wins")
    if user_input == 'r' and computer_input == 'rock':
        print(f"use choose {user_input} and computer choose {computer_input}\nIts a tie")

    if user_input == 'p' and computer_input == 'paper':
        print(f"use choose {user_input} and computer choose {computer_input}\nIts a tie ")
    if user_input == 'p' and computer_input == 'scissor':
        print(f"use choose {user_input} and computer choose {computer_input}\nComputer Wins")
    if user_input == 'p' and computer_input == 'rock':
        print(f"use choose {user_input} and computer choose {computer_input}\nUser Wins")

    if user_input == 's' and computer_input == 'paper':
        print(f"use choose {user_input} and computer choose {computer_input}\nUser Wins")
    if user_input == 's' and computer_input == 'scissor':
        print(f"use choose {user_input} and computer choose {computer_input}\nIts a tie")
    if user_input == 's' and computer_input == 'rock':
        print(f"use choose {user_input} and computer choose {computer_input}\nComputer Wins")

while True:
    enter_input = input("Enter \n 1. to start 2. to exit \n")
    if enter_input == "1":
        user_input = input("Enter r for rock , s for scissor , p for paper \n")
        play(user_input)
    else:
        break