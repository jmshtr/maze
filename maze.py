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

# Define the end position of the maze
end = {'row': rows - 2, 'col': cols - 2}

# Define a function to generate the maze using Depth-First Search algorithm
def generate_maze():
    stack = [(1, 1)]  # Start with the top-left cell
    visited = set()   # Keep track of visited cells
    while stack:
        current_cell = stack[-1]  # Get the current cell
        maze[current_cell[0]][current_cell[1]] = ' '  # Mark current cell as empty
        visited.add(current_cell)  # Mark current cell as visited
        # Generate the next cell's coordinates
        neighbors = [(current_cell[0] + 2, current_cell[1]), (current_cell[0] - 2, current_cell[1]),
                     (current_cell[0], current_cell[1] + 2), (current_cell[0], current_cell[1] - 2)]
        # Filter unvisited neighboring cells
        unvisited_neighbors = [neighbor for neighbor in neighbors if 0 < neighbor[0] < rows - 1 and 0 < neighbor[1] < cols - 1 and neighbor not in visited]
        if unvisited_neighbors:
            next_cell = random.choice(unvisited_neighbors)  # Choose a random neighboring cell
            wall_between = ((next_cell[0] + current_cell[0]) // 2, (next_cell[1] + current_cell[1]) // 2)  # Find the wall between current and next cell
            maze[wall_between[0]][wall_between[1]] = ' '  # Remove the wall between current and next cell
            stack.append(next_cell)  # Move to the next cell
        else:
            stack.pop()  # Backtrack if no unvisited neighboring cells

# Generate the maze
generate_maze()

# Set the exit position
maze[end['row']][end['col']] = '☆'

# Define the main game loop
while True:
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Update the maze with the player's position
    for r in range(rows):
        for c in range(cols):
            if player['row'] == r and player['col'] == c:
                print('*', end=' ')  # Print player marker
            else:
                print(maze[r][c], end=' ')  # Print maze cell
        print()
    
    # Check if the player has reached the end
    if player == end:
        print("Congratulations! You've reached the end of the maze!")
        break
    
    # Get the player's move
    move = input("Enter your move (UP, DOWN, LEFT, RIGHT): ").upper()
    
    # Check if the move is valid
    if move in directions:
        # Update the player's position
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
