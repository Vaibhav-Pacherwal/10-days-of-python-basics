## Game to guess a random number
import random

def guess(num):
    user_guess = 0
    attempt_count = 0
    while user_guess != num:
        user_guess = int(input("guess the number(1-10): "))
        attempt_count += 1
        if(user_guess < num):
            print("sorry, try again, Too Low..")
        elif(user_guess > num):
            print("sorry, try again, Too High..")
        else: 
            print("yayy! congrats you guessed it right!")
            print("Attempts Taken:", attempt_count)

randomNum = random.randint(1, 10)
guess(randomNum)