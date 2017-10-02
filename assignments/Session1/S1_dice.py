#
# @author : Evan Ricchi, IUT Annecy le vieux, Licence DIM
# @brief : a dice game against a computer

# Importation of the the library random
from random import *

def dice_game():
    ##
    # Function able to simulate a fight between an user and a computer in a dice game 

    # Initialise variables
    user_score = 0
    computer_score = 0
    # Variable qui signifie True = Game in progress False = Game ended
    game=True
    
    # Conditions for ending the game
    while (user_score < 100) and (computer_score < 100) and (game == True):

        # User turn
        random_dice = randint(1,6)

        while random_dice != 1 and (game == True):

            # Show the user score
            print("Your score is : ",user_score)

            if user_score >= 100:
                game=False
            else:
                # Ask the user if he want continue to reroll the dice
                user_choice = raw_input("You can reroll the dice, if you want press 'yes' ! ")
                if user_choice == "yes":
                    user_score += random_dice;                   
                    random_dice = randint(1,6);              
                else:
                     random_dice = 1;

        # Computer turn
        random_dice = randint(1,6)

        while random_dice != 1 and (game == True):

            # Show the computer score
            print ("Computer score is : ",computer_score)

            if computer_score >= 100:
                game=False
            else:
                computer_score += random_dice
                random_dice = randint(1,6)

    if user_score >= 100:
        print("You Won !")
    if computer_score >= 100:
        print("You Lost !")

# Testing dice_game function
dice_game()

