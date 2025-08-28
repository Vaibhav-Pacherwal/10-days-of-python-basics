## Make rock-paper-scissor game
import random

def play():
    comp_move = random.choice(['r', 'p', 's'])
    user_move = input("enter 'R' for rock, 'P' for paper and 'S' for scissor: ").lower()
    print(f"your move: {user_move}")

    if(comp_move == user_move):
        print("it's a tie!")
    
    if(user_move == 'r'):
        if(comp_move == 'p'):
            print(f"my move: {comp_move}")
            print("you lost! Paper covers Rock")
        else:
            print(f"my move: {comp_move}")
            print("you win! Rock smashes Scissors")

    if(user_move == 'p'):
        if(comp_move == 'r'):
            print(f"my move: {comp_move}")
            print("you win! Paper covers Rock")
        else:
            print(f"my move: {comp_move}")
            print("you lost! Scissor cuts Paper")

    if(user_move == 's'):
        if(comp_move == 'r'):
            print(f"my move: {comp_move}")
            print("you lost! Rock smashes Scissors")
        else:
            print(f"my move: {comp_move}")
            print("you win! Scissors cut Paper")

play()