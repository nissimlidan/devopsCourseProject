import os

def welcome():
    name = input("Please enter your name: ")
    print(f"\nHello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n")
    return name
def check_range(min_range, max_range):
    flag = True
    number = input('\nSelect the number: ')
    while flag:
        if number.isdigit() == True:
            number = int(number)
            if number >= min_range and number < max_range:
                flag = False
                return number
            else:
                number = input('Error, the number is out of range, please try again: ')
        else:
            number = input('Error, this is not a number, please try again: ')
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
def check_range_with_try(min_range, max_range):
    flag = True
    while flag:
        try:
            number = int(input('Select the number: '))
        except:
            print('Error! this is not a number')
        else:
            if number in range(min_range, max_range):
                flag = False
                return number
            else:
                print('Error! number not in the correct range')
def load_game():
    # Text color codes
    COLOR_RED = '\033[91m'
    COLOR_GREEN = '\033[92m'
    COLOR_YELLOW = '\033[93m'
    COLOR_BLUE = '\033[94m'
    COLOR_MAGENTA = '\033[95m'
    COLOR_CYAN = '\033[96m'
    COLOR_RESET = '\033[0m'

    # Example usage

    min_range_games, max_range_games = 1, 4
    min_range_difficulty, max_range_difficulty = 1, 6
    game_list = ['Memory Game', 'Guess Game', 'Currency Roulette']

    print('Please choose a game to play:\n')
    print(
        COLOR_CYAN + '[1]. Memory Game ' + COLOR_RESET + '- a sequence of numbers will appear for 1 second and you have to guess it back' + COLOR_RESET)
    print(COLOR_GREEN + '[2]. Guess Game ' + COLOR_RESET + '- guess a number and see if you chose like the computer')
    print(
        COLOR_BLUE + '[3]. Currency Roulette ' + COLOR_RESET + '- try and guess the value of a random amount of USD in ILS' + COLOR_RESET)

    game_number = check_range(min_range_games, max_range_games)
    print(f'\nGreat choice!! you choose the {COLOR_RED} {game_list[game_number - 1]} {COLOR_RESET}')

    print('Now please choose game difficulty:')
    print(COLOR_GREEN + '[1] - Very Easy' + COLOR_RESET)
    print(COLOR_BLUE + '[2] - Esay' + COLOR_RESET)
    print(COLOR_MAGENTA + '[3] - Medium' + COLOR_RESET)
    print(COLOR_YELLOW + '[4] - Hard' + COLOR_RESET)
    print(COLOR_RED + '[5] - Extreme' + COLOR_RESET)

    game_dif = check_range(min_range_difficulty, max_range_difficulty)
    # print(difficulty_list[game_dif-1])

    return game_number, game_dif, game_list[game_number - 1]
