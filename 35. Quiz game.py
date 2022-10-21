# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 22:22:55 2022

@author: Timor
"""
#-------------------------------------
def  new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions :
        print("-------------------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter A, B, C, or D: ").upper()
        guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
        
    display_score(correct_guesses, guesses)

#-------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0

#-------------------------------------
def display_score(correct_guesses,guesses):
    print("-------------------------------------------------")
    print("Results")
    print("-------------------------------------------------")
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Your answer: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()
    
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: " + str(score) + "%")

#-------------------------------------
def play_again():
    response = input("Do you want to play again?: (yes or no) ").upper()
    if response == "YES":
        return True 
    else:
        return False 
    


#-------------------------------------

questions = {
    "Who created python?: ": "A",
    "What year was python created?: ": "B",
    "Python is tributed to which comedy group: ": "C",
    "Is the earth round: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

new_game()

while play_again():
    new_game()
    
print("Bye!")






