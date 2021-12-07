# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

import random
import sys
import time
import os

def system_header():
    print("\n                         ***   Welcome to the LOTTERY   ***")
    print("\n\nInstructions:  Enter 3 whole numbers one at a time. The numbers should be ranging between 0 to 9.")
    print("               Do not enter unnecessary inputs to avoid termination of the game. Good luck!")


def generate_number():
    first_random = random.randint(0,9)
    second_random = random.randint(0,9)
    third_random = random.randint(0,9)
    
    return first_random, second_random, third_random


def get_input():
    num1_input = input("\nEnter first number (0-9):  ")
    num2_input = input("Enter second number (0-9):  ")
    num3_input = input("Enter third number (0-9):  ")

    return num1_input, num2_input, num3_input


def input_validation(user_input1, user_input2, user_input3):
    if user_input1 != "" and user_input2 != "" and user_input3 != "" :
        try:
            int_input1 = int(user_input1)
            int_input2 = int(user_input2)
            int_input3 = int(user_input3)
            if (0 >  int_input1 or int_input1 > 9) or (0 > int_input2 or int_input2 > 9) or (0 > int_input3 or int_input3 > 9 ):
                print("\nInputs should not be less than 0 or greater than 9. Try again.\n")
                return None, None, None

            else:
                return int_input1, int_input2, int_input3
        
        except ValueError:
            print("\nERROR: Invalid input. Game is terminated.\n")
            return False, False, False

    else:
        print("\nEmpty input is invalid.\n")
        return False, False, False


def loading_animation():
    for i in range (0,7):
        sys.stdout.write('\rLoading . . .')
        time.sleep(0.1)
        sys.stdout.write('\rLoading · . .')
        time.sleep(0.1)
        sys.stdout.write('\rLoading . · .')
        time.sleep(0.1)
        sys.stdout.write('\rLoading . . ·')
        time.sleep(0.1)


def lottery_main():
    start_lottery = 'yes'
    while start_lottery[0] == 'y':
        os.system('cls')
        system_header()
        lottery_numA, lottery_numB, lottery_numC = generate_number()
        user_num1, user_num2, user_num3 = get_input()
        valid_num1, valid_num2, valid_num3 = input_validation(user_num1, user_num2, user_num3)
        if ((valid_num1 is False) or (valid_num2 is False) or (valid_num3 is False)):
            break

        elif ((valid_num1 == None) or (valid_num2 == None) or (valid_num3 == None)):
            start_lottery = 'yes'
            loading_animation()

        else:
            if ((valid_num1 == lottery_numA and valid_num2 == lottery_numB and valid_num3 == lottery_numC) or
                (valid_num1 == lottery_numA and valid_num2 == lottery_numC and valid_num3 == lottery_numB) or
                (valid_num1 == lottery_numB and valid_num2 == lottery_numA and valid_num3 == lottery_numC) or
                (valid_num1 == lottery_numB and valid_num2 == lottery_numC and valid_num3 == lottery_numA) or
                (valid_num1 == lottery_numC and valid_num2 == lottery_numA and valid_num3 == lottery_numB) or
                (valid_num1 == lottery_numC and valid_num2 == lottery_numB and valid_num3 == lottery_numA)):
                print("\nResult:  Winner\nCongratulations!")

            else:
                print("\nResult:  You lost.\nBetter luck next time :)")
                print("Correct Numbers (in no particular order): " + str(lottery_numA) + ", " + str(lottery_numB) + ", and " + str(lottery_numC))

            start_lottery = input("\nDo you want to try again? (Y or N):  ")

            if start_lottery[0] == 'y':
                loading_animation()
            
            elif start_lottery[0] == 'n':
                print("Thank you for playing!\n")

            else:
                print("Invalid input. Game is terminated.")


lottery_main()