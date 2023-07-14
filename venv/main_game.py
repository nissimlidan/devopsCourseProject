from live import load_game, welcome
from Games import guess_game, memory_game, currency_roulette_game
from score import add_score
from Utils.utils import *

class colors:
    COLOR_RED = '\033[91m'
    COLOR_GREEN = '\033[92m'
    COLOR_YELLOW = '\033[93m'
    COLOR_BLUE = '\033[94m'
    COLOR_MAGENTA = '\033[95m'
    COLOR_CYAN = '\033[96m'
    COLOR_RESET = '\033[0m'


def main():
    clear_console()
    name_of_person = welcome()
    game_number, game_difficulty, game_type = load_game()
    score_file = open(SCORES_FILE_NAME, 'w')
    score_file.write('0')
    score_file.close()
    print(f'\nYou choose the {game_type} in difficulty level {game_difficulty}, good luck!')
    results(game_number, game_difficulty)

    ask_for_continue = ""
    while ask_for_continue != '3':
        ask_for_continue = input('You want:\n1. Play again this game.\n2. Choose another game.\n3. Exit.\n')
        while ask_for_continue.isnumeric() is False or int(ask_for_continue) > 3 or int(ask_for_continue) <= 0:
            ask_for_continue = input('Wrong input, try again: ')  # Check correct input
        if ask_for_continue == '1':
            clear_console()
            results(game_number, game_difficulty)
        elif ask_for_continue == '2':
            clear_console()
            game_number, game_difficulty, game_type = load_game()
            results(game_number, game_difficulty)
        else:
            print("Thank you and hope to see you soon! ")

def results(game_number,difficulty):
    if game_number == 1: #Memory Game
        result = memory_game.play(difficulty)
        if result[0]:
            print(f"\n{colors.COLOR_GREEN}Congratulations!! You are the WINNER. \nYou have an excellent memory!.{colors.COLOR_RESET}")
            add_score(difficulty)
        else:
            print(colors.COLOR_RED + "We're sorry, but you missed it, maybe next time" + colors.COLOR_RESET)
            print(f"The number is {result[1]}")
    elif game_number == 2: #Guess Game
        result = guess_game.play(difficulty)
        if result[0]:
            print(f"\n{colors.COLOR_GREEN}Congratulations!! You are the WINNER. \nIt's your lucky day, it's time to fill out a lottery ticket.{colors.COLOR_RESET}")
            add_score(difficulty)
        else:
            print(colors.COLOR_RED + "We're sorry, but you missed it, maybe next time" + colors.COLOR_RESET)
            print(f"The number is {result[1]}")
    elif game_number == 3: #Currency Roulette
        result = currency_roulette_game.play(difficulty)
        print(result)
        if result[0]:
            print(f"\n{colors.COLOR_GREEN}Congratulations!! You are the WINNER. \nYou managed to beat me.{colors.COLOR_RESET}")
            add_score(difficulty)
        else:
            print(colors.COLOR_RED + "We're sorry, but you missed it, maybe next time" + colors.COLOR_RESET)
            print(f"The number is {result[1]}")


if __name__ == '__main__':
    main()