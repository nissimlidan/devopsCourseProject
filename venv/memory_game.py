from live import check_range
import os
import random
import time

COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[92m'
COLOR_YELLOW = '\033[93m'
COLOR_BLUE = '\033[94m'
COLOR_MAGENTA = '\033[95m'
COLOR_CYAN = '\033[96m'
COLOR_RESET = '\033[0m'

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def memory_game(difficulty, name):
    print(f"\nWelcome {name} to the Memory Game!")
    print("You will be shown a sequence of numbers for a short time.")
    print("Your task is to remember the numbers and input them correctly.")
    play(difficulty)


def generate_sequence(difficulty):
    sequence = []
    for _ in range(difficulty):
        sequence.append(random.randint(1, 101))
    return sequence

def get_list_from_user(difficulty):
    user_list = []
    for _ in range(difficulty):
        number = check_range(1,101)
        #number = int(input("Enter a number: "))
        user_list.append(number)
    return user_list

def is_list_equal(list1, list2):
    return list1 == list2

def play(difficulty):
    print(f"\n{COLOR_BLUE}Let's begin!(Start in 5 second){COLOR_RESET}")
    time.sleep(5)
    sequence = generate_sequence(difficulty)
    print("\nMemorize the following sequence:")
    print(sequence)
    time.sleep(0.7)
    clear_console()
    print(f"{COLOR_RED}Time's up!{COLOR_RESET} Now it's your turn.")

    flag2 = True

    while flag2:
        sequence = generate_sequence(difficulty)
        user_sequence = get_list_from_user(difficulty)

        if is_list_equal(sequence, user_sequence):
            print(f"{COLOR_GREEN}Congratulations! You won the game.{COLOR_RESET}")
            return True

        flag3 = True
        while flag3:
            print(f"\n{COLOR_RED}Wrong answer!!{COLOR_RESET}")
            if_to_continue = input(f"{COLOR_BLUE}If you want to try again type {COLOR_RED}Y{COLOR_RESET}, otherwise type {COLOR_RED}N{COLOR_RESET}: ")

            if if_to_continue.lower() == 'n':
                print(f'\n{COLOR_MAGENTA}Goodbye, hope to see you soon{COLOR_RESET}')
                exit()
            elif if_to_continue.lower() == 'y':
                flag3 = False
                play(difficulty)
            else:
                print(f'\n{COLOR_RED}Error, you entered an incorrect value{COLOR_RESET}')
                if_to_continue = input(f"Please enter a valid input. If you want to try again type {COLOR_RED}Y{COLOR_RESET}, otherwise type {COLOR_RED}N{COLOR_RESET}: ")
                if if_to_continue.lower() == 'n':
                    print(f'\n{COLOR_MAGENTA}Goodbye, hope to see you soon{COLOR_RESET}')
                    exit()