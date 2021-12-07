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


def main_function():
    random_number = random.randint(0,100)
    answer = 'wrong'
    while answer == 'wrong':
        os.system('cls')
        system_header()
        number_input = int(input("\n\nWhat do you think is the number? (0-100):  "))

        if number_input == random_number:
            print("\nCongratulations!\nYou have guessed the correct number.\n")
            answer = 'correct'

        else:
            if number_input > random_number:
                print("\nNice try. \nHint: Your number is greater than the unknown number. Press any key to try again.")
                msvcrt.getch()

            elif number_input < random_number:
                print("\nGood guess. \nHint: Your number is less than the unknown number. Press any key to try again.")
                msvcrt.getch()

main_function()
