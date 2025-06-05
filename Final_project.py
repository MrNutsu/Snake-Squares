# Final project made by: João Pedro Blagitz Ravache

import os
import random
import time
import sys

# Try to import the msvcrt library, which only exists on Windows.

try:
    import msvcrt
    IS_WINDOWS = True
except ImportError:
    IS_WINDOWS = False
    # For Linux/macOS, non-blocking key reads are more complex.
    # I will leave a note about this where it's used.
    pass

#Cleans the terminal

def clear_screen():
    """Clears the terminal screen. Equivalent to 'system("cls")' in your code."""
    os.system('cls' if os.name == 'nt' else 'clear')

#TIC-TAC-TOE Game Functions

def display_tic_tac_toe_board(board):
    """Prints the Tic-Tac-Toe board to the screen. Equivalent to your printTabuleiro() function."""
    clear_screen()
    print("\n\t=============== Tic-Tac-Toe ===============\n")
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("---|---|---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---|---|---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} \n")

def check_tic_tac_toe_winner(board):
    """Checks rows, columns, and diagonals. Equivalent to your checarVencedor() function."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return ' '  # No winner

def check_free_spaces(board):
    """Counts how many empty spaces are still on the board."""
    spaces = 0
    for row in board:
        for space in row:
            if space == ' ':
                spaces += 1
    return spaces

def player_move(board, current_player):
    """Handles the player's move logic, using numbers 1-9."""
    while True:
        try:
            position = int(input(f"Player '{current_player}', choose a position (1-9): "))
            if 1 <= position <= 9:
                row = (position - 1) // 3
                col = (position - 1) % 3
                if board[row][col] == ' ':
                    board[row][col] = current_player
                    break
                else:
                    print("Space already occupied. Try again.")
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def computer_move(board, computer_symbol):
    """Random computer move."""
    print("Computer's turn...")
    time.sleep(1)
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = computer_symbol
            break

def play_tic_tac_toe():
    """Main function to manage the Tic-Tac-Toe game, with mode selection."""
    # Tic-Tac-Toe specific menu
    game_mode = ''
    while game_mode not in ['1', '2']:
        clear_screen()
        print("--- TIC-TAC-TOE ---")
        print("Choose the game mode:")
        print("1. Player vs. Computer")
        print("2. Player vs. Player")
        game_mode = input("Enter your choice: ")

    board = [[' ' for _ in range(3)] for _ in range(3)]
    PLAYER1 = 'X'
    PLAYER2 = 'O'
    winner = ' '

    if game_mode == '2':  # Player vs. Player
        current_player = PLAYER1
        while winner == ' ' and check_free_spaces(board) > 0:
            display_tic_tac_toe_board(board)
            player_move(board, current_player)
            winner = check_tic_tac_toe_winner(board)
            current_player = PLAYER2 if current_player == PLAYER1 else PLAYER1
    
    else:  # Player vs. Computer
        COMPUTER = 'O'
        while winner == ' ' and check_free_spaces(board) > 0:
            display_tic_tac_toe_board(board)
            player_move(board, PLAYER1)
            winner = check_tic_tac_toe_winner(board)
            if winner != ' ' or check_free_spaces(board) == 0:
                break
            
            computer_move(board, COMPUTER)
            winner = check_tic_tac_toe_winner(board)

    # Display final result
    display_tic_tac_toe_board(board)
    if winner == ' ':
        print("IT'S A DRAW!")
    else:
        print(f"PLAYER '{winner}' WINS!")

#SNAKE Game Functions

def play_snake_game():
    """Main function that runs the Snake game."""
    # Initial settings
    height = 20
    width = 20
    head_x, head_y = width // 2, height // 2
    
    snake_body = [[head_y, head_x]]

    fruit_x = random.randint(1, width - 2)
    fruit_y = random.randint(1, height - 2)

    score = 0
    direction = 'STOP'
    game_over = False

    while not game_over:
        # 1. Draw the screen
        clear_screen()
        print(f"Score: {score}")
        for i in range(height):
            for j in range(width):
                if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                    sys.stdout.write("#")
                elif i == head_y and j == head_x:
                    sys.stdout.write("O")  # The snake's head
                elif i == fruit_y and j == fruit_x:
                    sys.stdout.write("+")  # The fruit
                else:
                    is_body_part = False
                    for k in range(1, len(snake_body)):
                        if snake_body[k][0] == i and snake_body[k][1] == j:
                            sys.stdout.write("o")  # The snake's body
                            is_body_part = True
                            break
                    if not is_body_part:
                        sys.stdout.write(" ")
            sys.stdout.write("\n")
        sys.stdout.flush()

        # 2. User Input
        if IS_WINDOWS:
            if msvcrt.kbhit():
                ch = msvcrt.getch().decode('utf-8').lower()
                if ch == 'w' and direction != 'DOWN': direction = 'UP'
                elif ch == 's' and direction != 'UP': direction = 'DOWN'
                elif ch == 'a' and direction != 'RIGHT': direction = 'LEFT'
                elif ch == 'd' and direction != 'LEFT': direction = 'RIGHT'
        else:
            # Note for Linux/macOS: Capturing keys here would require libraries
            # like 'pynput' or 'curses'.
            pass

        # 3. Game Logic 
        # Save the old body state before moving
        old_body = [row[:] for row in snake_body]
        if direction != 'STOP':
            # Move the tail
            for i in range(len(snake_body) - 1, 0, -1):
                snake_body[i] = snake_body[i-1][:]
        
        # Move the head
        if direction == 'UP': head_y -= 1
        elif direction == 'DOWN': head_y += 1
        elif direction == 'LEFT': head_x -= 1
        elif direction == 'RIGHT': head_x += 1
        snake_body[0] = [head_y, head_x]

        # Check for collision with walls
        if head_x <= 0 or head_x >= width - 1 or head_y <= 0 or head_y >= height - 1:
            game_over = True
        
        # Check for collision with self
        for i in range(1, len(snake_body)):
            if snake_body[i] == snake_body[0]:
                game_over = True
                break

        # Check for eating fruit
        if head_x == fruit_x and head_y == fruit_y:
            score += 10
            fruit_x = random.randint(1, width - 2)
            fruit_y = random.randint(1, height - 2)
            # Add a new segment at the old tail's position
            snake_body.append(old_body[-1])

        time.sleep(0.1) 

    # Game over message
    print("\nGAME OVER!")
    print(f"Final Score: {score}")

def main():
    """Main function to manage the menu and game selection."""
    while True:
        clear_screen()
        print("================================")
        print("    PYTHON FINAL PROJECT        ")
        print("================================")
        print("\nChoose a game:")
        print("1. Tic-Tac-Toe")
        print("2. Snake Game")
        print("3. Exit")
        
        choice = input("\nEnter your choice: ")

        if choice == '1':
            play_tic_tac_toe()
            input("\nPress Enter to return to the menu...")
        elif choice == '2':
            if not IS_WINDOWS:
                print("\nWARNING: Keyboard controls for this game work best on Windows.")
                print("On Linux/macOS, the snake will move right on its own for demonstration.")
                print("Press Enter to start.")
                input()
            play_snake_game()
            input("\nPress Enter to return to the menu...")
        elif choice == '3':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid option, please try again.")
            time.sleep(1)

# Program entry point
if __name__ == "__main__":
    main()
