from live import load_game, welcome
from guess_game import guess_game
from currency_roulette_game import currency_roulette_game
from memory_game import memory_game

name_of_person = welcome()
game_number,game_difficulty, game_type = load_game()

print(f'\nYou choose the {game_type} in difficulty level {game_difficulty}, good luck!')
if game_number == 1:
    memory_game(game_difficulty, name_of_person)
elif game_number == 2:
    guess_game(game_difficulty, name_of_person)
elif game_number == 3:
    currency_roulette_game(game_difficulty)
else:
    exit()
