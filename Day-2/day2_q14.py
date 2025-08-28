## Hangman Game
import random
from words import words

word = random.choice(words)

def play():
    print("current word: ", end="")
    for i in range(0, len(word)):
        print('-', end="")

    print()
    wrong_count = 0
    user_word_letters = set()
    word_letters = set(word.lower())
    print("Hints:", end=" ")
    print(word_letters)
    back_up = {}
    while len(word_letters) != 0:
        if wrong_count == 6:
            print("you lost, try again")
            break
        user_word = input("guess a letter:").lower()
        if user_word in word_letters:
            user_word_letters.add(user_word)
            word_letters.remove(user_word)
            print("You have used these letters:", end=" ")
            for el in user_word_letters:
                print(el, end=" ")
            print()
            letter_index = word.find(user_word)
            print("current word: ", end="")
            for i in range(len(word)):
                if i == letter_index:
                    back_up[i] = word[i]  
                if i in back_up:
                    print(back_up[i], end="") 
                else:
                    print('-', end="")   

        else:
            wrong_count+=1
            user_word_letters.add(user_word)
            print("You have used these letters:", end=" ")
            for el in user_word_letters:
                print(el, end=" ")
            print()
            print("oops! wrong guess, try again!")

        print()

play()