import random
import requests

COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[92m'
COLOR_YELLOW = '\033[93m'
COLOR_BLUE = '\033[94m'
COLOR_MAGENTA = '\033[95m'
COLOR_CYAN = '\033[96m'
COLOR_RESET = '\033[0m'

def currency_roulette_game(difficulty):
    play(difficulty)
def get_money_interval(difficulty):
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    exchange_rates = response.json().get('rates')
    exchange_rate = exchange_rates.get('ILS')
    total_money = random.randint(1, 100)
    lower_bound = total_money - (5 - difficulty)
    upper_bound = total_money + (5 - difficulty)

    return (total_money, lower_bound * exchange_rate, upper_bound * exchange_rate)

def get_guess_from_user(total_money):
    while True:
        try:
            guess = float(input(f'\nEnter your guess for the value {total_money}$ in ILS(₪): '))
            return guess
        except ValueError:
            print('Invalid input. Please enter a number.')

def play(difficulty):
    total_money, lower_bound, upper_bound = get_money_interval(difficulty)
    guess = get_guess_from_user(total_money)
    print(f'\n{COLOR_MAGENTA}Your guess for {total_money}$ was {guess}₪{COLOR_RESET}\n{COLOR_CYAN}The lower bound guess was - {lower_bound} and the upper bound guess was {upper_bound}{COLOR_RESET}')
    if lower_bound <= guess <= upper_bound:
        print(f'\n{COLOR_GREEN}Congratulations! You won the game\nNext time make a harder level{COLOR_RESET}')
        return True
    while True:
        answer = input(
            f'{COLOR_BLUE}If you want to try again, type {COLOR_RED}Y{COLOR_RESET}. Otherwise, type {COLOR_RED}N{COLOR_RESET}: ')

        if answer.lower() == 'n':
            print(f'\n{COLOR_MAGENTA}Goodbye! Hope to see you soon.{COLOR_RESET}')
            break
        elif answer.lower() == 'y':
            play(difficulty)
            break
        else:
            print('Invalid input. Please enter either Y or N.')
