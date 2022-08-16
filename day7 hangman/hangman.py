
import random
from hangman_words import word_list
from hangman_art import HANGMANPICS

# check the guess letter and update the lives 
def func_check_guess ():
        guess = input("Your Guess:\n").lower()
        global lives
        if guess not in  letters_list :
            lives = lives-1
            print(HANGMANPICS[6-lives])
        else :
            for i in range(len(letters_list)):
                if guess == letters_list[i]:
                    result_list[i]=guess
        print(result_list)
        print(lives,"lives left!")


lives = 7
word = random.choice(word_list)  
letters_list=[]
result_list=[]
for index,value in enumerate(word):
    letters_list.append(value)
    result_list.append("_")

while "_" in result_list:
    if lives!=0:
        func_check_guess()
    else :
        print("You lose...")
        break
if lives>0 :
    print("You Win!")