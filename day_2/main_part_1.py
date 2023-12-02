# Open file 
with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

# Map of colors to their constraints
constraints = {
    'red': 12,
    'green': 13,
    'blue': 14
} 

# Result 
result = 0

# Validate each game
for line in lines:
    # Parse game info from line
    game_info = line.split(':')
    game_id_num = int(game_info[0].split(' ')[1])
    game_rounds = game_info[1].split(';')
    
    # Valid game flag to break if constraint fails
    valid_game = True
    for game in game_rounds:
        if not valid_game:
            break 

        cube_counts = game.split(',')
        for cube_info in cube_counts:
            count, color = cube_info.strip().split(' ')
            # Check if each draw matches bag constraints
            if int(count) > constraints[color]:
                valid_game = False
                break
            
    # Add game ID to sum for valid games
    if valid_game:
        result += game_id_num   

print(result) # 2085

