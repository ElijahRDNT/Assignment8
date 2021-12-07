# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

import random
import msvcrt
import os

def system_header():
    print("\n                         ***   Guess The Number!   ***")
    print("\n\nInstructions:  The system will generate a random whole number ranging from 0 to 100. The game won't stop")
    print("               until you get the correct number. Don't worry, the system will provide clues as you play.")
    print("               The random number will not change all throughout the game.")


def input_validation(user_input1):
    if user_input1 != "":
        try:
            int_input1 = int(user_input1)
            return int_input1
        
        except ValueError:
            print("\nERROR: Any inputs (characters/symbols) except numbers are invalid.")
            return False
            
    else:
        print("\nEmpty input is invalid.")
        return False


def main_function():
    random_number = random.randint(0,100)
    answer = 'wrong'
    while answer == 'wrong':
        os.system('cls')
        system_header()
        number_input = input("\n\nWhat do you think is the number? (0-100):  ")
        user_number = input_validation(number_input)
        if user_number is False:
            print("Please avoid unnecessary inputs. Press any key to continue.")
            msvcrt.getch()

        elif user_number == random_number:
            print("\nCongratulations!\nYou have guessed the correct number.\n")
            answer = 'correct'

        elif 0 > user_number or user_number > 100:
                print("\nInputs should range from 0 to 100 only. Press any key to continue.")
                msvcrt.getch()

        else:
            if user_number > random_number:
                print("\nNice try. \nHint: Your number is greater than the unknown number. Press any key to try again.")
                msvcrt.getch()

            elif user_number < random_number:
                print("\nGood guess. \nHint: Your number is less than the unknown number. Press any key to try again.")
                msvcrt.getch()


main_function()
