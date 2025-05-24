BOARD_SIZE = 3
REWARD = 10

class TicTacToe:
    def __init__(self, board):
        # Challenge 1: Initialize the board as a dictionary with keys 1-9 all set to ' '
        # Set player symbol to 'O' and computer symbol to 'X'
        self.board = board
        self.player = 'O'
        self.computer = 'X'
        self.reset_board()
    def reset_board(self):
        self.board = {pos: ' ' for pos in range(1, 10)}

    def run(self):
        print("Welcome to Tic-Tac-Toe!")
        print("You are 'O' and the computer is 'X'")
        print("Positions are numbered 1-9 from top-left to bottom-right")
        print("--------------------------------------")
        
        #computer makes first move
        self.move_computer()
        while True:
            self.move_player()
            self.move_computer()

    def print_board(self):
        # Challenge 2: Print the current state of the board
        # Format the board for better readability
        print("\n")
        print(f" {self.board[1]} | {self.board[2]} | {self.board[3]} ")
        print("---+---+---")
        print(f" {self.board[4]} | {self.board[5]} | {self.board[6]} ")
        print("---+---+---")
        print(f" {self.board[7]} | {self.board[8]} | {self.board[9]} ")
        print("\n")

    def is_cell_free(self, position):
        # Challenge 3: Check if the cell at 'position' is free (not occupied)
        # Return True if free, False otherwise
        return self.board[position] == ' '

    def update_player_position(self, player, position):
        # Challenge 4: If the cell at 'position' is free, place 'player' symbol there
        if self.is_cell_free(position):
            self.board[position] = player
            self.check_game_state()
        else:
            print(f"Position {position} is already occupied!")
            if player == self.player:
                self.move_player()
            else:
                self.move_computer()

    def is_winning(self, player):
        # Challenge 5: Check if 'player' has 3 in a row horizontally, vertically, or diagonally
        #check rows
        for i in range(1, 8, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] == player:
                return True
        #check columns
        for i in range(1, 4):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] == player:
                return True
        #check diagonals
        if self.board[1] == self.board[5] == self.board[9] == player:
            return True
        if self.board[3] == self.board[5] == self.board[7] == player:
            return True
        return False
        

    def is_draw(self):
        # Challenge 6: Return True if no empty cells remain on the board (all positions filled)
        for position in self.board:
            if self.board[position] == ' ':
                return False

    def check_game_state(self):
        # Challenge 7: Print the board and check if the game ended
        self.print_board()
        if self.is_winning(self.computer):
            print("Computer wins!")
            exit()
        elif self.is_winning(self.player):
            print("Player wins!")
            exit()
        elif self.is_draw():
            print("It's a draw!")
            exit()
        else:
            print("Game continues...")

    def move_player(self):
        # Challenge 8: Ask the human player to enter a position (1-9)
        while True:
            try:
                position = int(input("Enter your move (1-9): "))
                if position < 1 or position > 9:
                    print("Invalid position! Please enter a number between 1 and 9.")
                    continue
                self.update_player_position(self.player, position)
                break
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 9.")

    def move_computer(self):
        # Challenge 9: Iterate over all free cells on the board
        best_score = -float('inf')
        best_move = None

        for move in self.board:
            if self.is_cell_free(move):
                # Try the move
                self.board[move] = self.computer
                score = self.minimax(0, False)
                # Undo the move
                self.board[move] = ' '
                
                if score > best_score:
                    best_score = score
                    best_move = move
        self.update_player_position(self.computer, best_move)

    def minimax(self, depth, is_maximizer):
        # Challenge 10: Implement recursive minimax algorithm:
        if self.is_winning(self.computer):
            return REWARD - depth
        if self.is_winning(self.player):
            return -REWARD + depth
        if self.is_draw():
            return 0
        if is_maximizer:
            best_score = -float('inf')
            for move in self.board:
                if self.is_cell_free(move):
                    # Try the move
                    self.board[move] = self.computer
                    score = self.minimax(depth + 1, False)
                    # Undo the move
                    self.board[move] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.board:
                if self.is_cell_free(move):
                    # Try the move
                    self.board[move] = self.player
                    score = self.minimax(depth + 1, True)
                    # Undo the move
                    self.board[move] = ' '
                    best_score = min(score, best_score)
            return best_score


if __name__ == '__main__':
    # Challenge 1: Initialize empty board dictionary with keys 1 to 9 set to ' '
    board = {pos: ' ' for pos in range(1, 10)}

    game = TicTacToe(board)
    # Challenge 11: Start the game loop
    game.run()
