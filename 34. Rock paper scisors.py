# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 20:10:53 2022

@author: Timor
"""

import random 

while True:

    choices = ["rock","paper","scissors"]
    
    computer = random.choice(choices)
    player = None

    
    while player not in choices:
        player = input("Rock, Paper or scissors? : ").lower()
    
    if player == computer :
        print(player)
        print(computer)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print(player)
            print(computer)
            print("You lose!")
        if computer == "scissors":
            print(player)
            print(computer)
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print(player)
            print(computer)
            print("You lose!")
        if computer == "rock":
            print(player)
            print(computer)
            print("You win!")
    elif player == "scissors":  
        if computer == "rock":
            print(player)
            print(computer)
            print("You lose!")
        if computer == "paper":
            print(player)
            print(computer)
            print("You win!")
    
    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
    
print("Bye")



