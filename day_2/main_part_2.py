from collections import defaultdict

# Open file 
with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

# Result 
result = 0

# Find power of each game
for line in lines:
    # Parse game info from line
    game_info = line.split(':')
    game_id_num = int(game_info[0].split(' ')[1])
    game_rounds = game_info[1].split(';')
    max_color_values = defaultdict(int)
    
    for game in game_rounds:
    
        cube_counts = game.split(',')
        for cube_info in cube_counts:
            count, color = cube_info.strip().split(' ')
            max_color_values[color] = max(max_color_values[color], int(count))
            
    # Find power of game and add to result
    power = 1
    for key, val in max_color_values.items():
        power *= val
    result += power

print(result) 

