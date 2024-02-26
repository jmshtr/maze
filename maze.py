import os
import random

# Define the size of the maze
rows = 10
cols = 10

# Initialize the maze with walls everywhere
maze = [['#' for _ in range(cols)] for _ in range(rows)]

# Define the directions a player can move
directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']

# Define the starting position of the player
player = {'row': 1, 'col': 1}

# Define a function to generate the maze using Depth-First Search
def generate_maze():
    stack = [(1, 1)]
    visited = set()
    while stack:
        current_cell = stack[-1]
        maze[current_cell[0]][current_cell[1]] = ' '
        visited.add(current_cell)
        neighbors = [(current_cell[0] + 2, current_cell[1]), (current_cell[0] - 2, current_cell[1]),
                     (current_cell[0], current_cell[1] + 2), (current_cell[0], current_cell[1] - 2)]
        unvisited_neighbors = [neighbor for neighbor in neighbors if 0 < neighbor[0] < rows - 1 and 0 < neighbor[1] < cols - 1 and neighbor not in visited]
        if unvisited_neighbors:
            next_cell = random.choice(unvisited_neighbors)
            wall_between = ((next_cell[0] + current_cell[0]) // 2, (next_cell[1] + current_cell[1]) // 2)
            maze[wall_between[0]][wall_between[1]] = ' '
            stack.append(next_cell)
        else:
            stack.pop()

# Generate the maze
generate_maze()

# Define the minimum distance from the starting position for the exit
min_distance = max(rows, cols) // 2

# Randomly select the exit position
exit_found = False
while not exit_found:
    exit_row = random.randint(1, rows - 2)
    exit_col = random.randint(1, cols - 2)
    if abs(exit_row - player['row']) >= min_distance or abs(exit_col - player['col']) >= min_distance:
        maze[exit_row][exit_col] = '☆'
        exit_found = True

# Define the main game loop
while True:
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Update the maze with the player's position
    for r in range(rows):
        for c in range(cols):
            if player['row'] == r and player['col'] == c:
                print('*', end=' ')
            else:
                print(maze[r][c], end=' ')
        print()
    
    # Check if the player has reached the exit
    if maze[player['row']][player['col']] == '☆':
        print("Congratulations! You've reached the exit of the maze!")
        break
    
    # Get the player's move
    move = input("Enter your move (UP, DOWN, LEFT, RIGHT): ").upper()
    
    # Update the player's position based on the move
    if move == 'UP' and maze[player['row'] - 1][player['col']] != '#':
        player['row'] -= 1
    elif move == 'DOWN' and maze[player['row'] + 1][player['col']] != '#':
        player['row'] += 1
    elif move == 'LEFT' and maze[player['row']][player['col'] - 1] != '#':
        player['col'] -= 1
    elif move == 'RIGHT' and maze[player['row']][player['col'] + 1] != '#':
        player['col'] += 1
    else:
        print("Invalid move! Please enter UP, DOWN, LEFT, or RIGHT.")