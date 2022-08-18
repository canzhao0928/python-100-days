
import random
from tkinter import Y
from replit import clear
def get_card () :
    return random.randint(1,13)

def calculate_score(cards):
    score =0 
    for num in cards:
        if num > 10:
            score += 10
        else: 
            score += num
    return score
    

new_game = "y"
while new_game == "y":
    #init
    clear()
    you_cards = [get_card(),get_card()]
    computer_cards = [get_card(),get_card()]
    print("Your cards:", str(you_cards))
    print("Computer's first cards:", computer_cards[0])
    choic= "y"

    #user choice
    while choic == "y":
        choic = input('Type "y" to get another cards, type "n" to pass\n')
        if choic == "y":
            you_cards.append(get_card())
            print("Your cards:", str(you_cards))
            print("Computer's first cards:", computer_cards[0])
        else :
            you_score = calculate_score(you_cards)
            computer_score = calculate_score(computer_cards)
            print("your score:",you_score,"comperter score:",computer_score)
            print("Your final hand:", str(you_cards))
            print("Computer's final hand:", str(computer_cards))
            if you_score > computer_score:
                print("You WIN!")
            elif (you_score< computer_score) :
                print("You lose...")
            else :
                print("Draw")
    new_game= input('Type "y" to start a new game, type "n" to over\n')