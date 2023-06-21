from live import check_range
import os
import random

COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[92m'
COLOR_YELLOW = '\033[93m'
COLOR_BLUE = '\033[94m'
COLOR_MAGENTA = '\033[95m'
COLOR_CYAN = '\033[96m'
COLOR_RESET = '\033[0m'

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def guess_game(game_difficulty, name):
    number_of_cards = game_difficulty * 2
    clear_console()

    print('\n')
    print(f'Hey {name} and welcome to the famous guessing game. \nI will generate a number between 1 and {number_of_cards} and you have to guess, if you succeed you will win the game.')
    flag = True
    while flag:
        secret_number = random.randint(1,number_of_cards)  # Generates a random integer between 1 and game_difficulty * 2
        #user_guess = input('\nChose number: ')
        user_guess = check_range(1,number_of_cards+1)
        if int(secret_number) == int(user_guess):
            print(f"\n{COLOR_GREEN}Congratulations!! \nYou managed to beat me.\nNow it's time to try a higher level{COLOR_RESET}")
            flag = False
        else:
            flag2 = True
            if_to_continue = input(f"\n{COLOR_RED}Wrong answer!!{COLOR_RESET}\nI chose the {COLOR_CYAN}number {secret_number}{COLOR_RESET} and you chose the {COLOR_MAGENTA}number {user_guess}{COLOR_RESET}, {COLOR_BLUE}if you want to try again type {COLOR_RED}Y{COLOR_RESET} otherwise type {COLOR_RED}N{COLOR_RESET}: ")
            if if_to_continue == 'N' or if_to_continue == 'n':
                print(f'\n{COLOR_YELLOW}Goodbye, hope to see you soon{COLOR_RESET}')
                break
            elif if_to_continue == 'Y' or if_to_continue == 'y':
                continue
            else:
                while flag2:
                    print(f'\n{COLOR_RED}Error, you entered an incorrect value{COLOR_RESET}')
                    if_to_continue = input(f"Please print valid input, {COLOR_BLUE}if you want to try again type {COLOR_RED}Y{COLOR_RESET} otherwise type {COLOR_RED}N{COLOR_RESET}:")
                    if if_to_continue.lower() == 'y':
                        flag2 = False
                        break
                    elif if_to_continue.lower() == 'n':
                        print(f'\n{COLOR_YELLOW}Goodbye, hope to see you soon{COLOR_RESET}')
                        exit()

