
def welcome():
    name = input("Please enter your name: ")
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")
    return name

def check_range_with_try(min_range,max_range):
    flag = True
    while flag:
        try:
            number = int(input('Select the number: '))
        except:
            print('Error! this is not a number')
        else:
            if number in range(min_range,max_range):
                flag = False
                return number
            else:
                print('Error! number not in the correct range')

def check_range(min_range,max_range):
    flag = True
    number = input('Select the number: ')
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

def load_game():
    min_range_games, max_range_games = 1,4
    min_range_difficulty, max_range_difficulty = 1,6
    game_list = ['Memory Game', 'Guess Game', 'Currency Roulette']
    difficulty_list = ['You choose level 1, good luck', 'Nice choice, good luck in level 2',
                       'Level 3 is not easy, good luck ', 'Level 4 is a very difficult choice, good luck!',
                       'Wow good luck, its hard choice!!']

    print('Please choose a game to play:')
    print('1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back')
    print('2. Guess Game - guess a number and see if you chose like the computer')
    print('3. Currency Roulette - try and guess the value of a random amount of USD in ILS')

    game_number = check_range(min_range_games, max_range_games)
    print(f'Great choice!! you choose the {game_list[game_number-1]}')

    print('Now please choose game difficulty from 1 to 5')
    game_dif = check_range(min_range_difficulty, max_range_difficulty)
    #print(difficulty_list[game_dif-1])

    return game_number, game_dif, game_list[game_number-1]
