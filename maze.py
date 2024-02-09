import os

# Define the maze as a list of lists
maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],  # Walls
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],  # Start
    ['#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#'],  # Walls
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],  # Empty space
    ['#', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],  # Walls
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],  # Empty space
    ['#', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],  # Walls
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],  # End
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']   # Walls
]

# Define the directions a player can move
directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']

# Define the starting position of the player
player = {'row': 1, 'col': 1}

# Define the end position of the maze
end = {'row': 7, 'col': 8}

# Define the main game loop
while True:
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Update the maze with the player's position
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if player['row'] == r and player['col'] == c:
                print('*', end=' ')  # Player marker
            else:
                print(maze[r][c], end=' ')
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
            maze[player['row']][player['col']] = ' '  # Replace previous position with empty space
            player['row'] -= 1
        elif move == 'DOWN' and maze[player['row'] + 1][player['col']] != '#':
            maze[player['row']][player['col']] = ' '  # Replace previous position with empty space
            player['row'] += 1
        elif move == 'LEFT' and maze[player['row']][player['col'] - 1] != '#':
            maze[player['row']][player['col']] = ' '  # Replace previous position with empty space
            player['col'] -= 1
        elif move == 'RIGHT' and maze[player['row']][player['col'] + 1] != '#':
            maze[player['row']][player['col']] = ' '  # Replace previous position with empty space
            player['col'] += 1
    else:
        print("Invalid move! Please enter UP, DOWN, LEFT, or RIGHT.")
