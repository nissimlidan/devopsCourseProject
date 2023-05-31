from live import load_game, welcome

name_of_person = welcome()
game_number,game_difficulty, game_type = load_game()

print(f'Hey {name_of_person}, you choose the {game_type} in difficulty level {game_difficulty}, good luck!')