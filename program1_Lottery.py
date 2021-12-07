# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

import random

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


system_header()
lottery_numA, lottery_numB, lottery_numC = generate_number()
user_num1, user_num2, user_num3 = get_input()