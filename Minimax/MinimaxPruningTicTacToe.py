# Constants for the game setup
BOARD_SIZE = 3       # The Tic-Tac-Toe board is 3x3
REWARD = 10          # Score for winning the game

class TicTacToe:
    def __init__(self, board):
        self.board = board
        self.player = 'O'
        self.computer = 'X'

    def run(self):
        print("Welcome to Tic-Tac-Toe!")
        print("You are 'O' and the computer is 'X'")
        print("Positions are numbered 1-9 from top-left to bottom-right")
        print("--------------------------------------")
        
        # Computer makes first move
        self.move_computer()
        
        while True:
            self.move_player()
            self.move_computer()

    def print_board(self):
        print("\n")
        print(f" {self.board[1]} | {self.board[2]} | {self.board[3]} ")
        print("---+---+---")
        print(f" {self.board[4]} | {self.board[5]} | {self.board[6]} ")
        print("---+---+---")
        print(f" {self.board[7]} | {self.board[8]} | {self.board[9]} ")
        print("\n")

    def is_cell_free(self, position):
        return self.board[position] == ' '

    def update_player_position(self, player, position):
        if self.is_cell_free(position):
            self.board[position] = player
            self.check_game_state()
        else:
            print(f"Position {position} is already occupied!")
            if player == self.player:
                self.move_player()
            else:
                self.move_computer()

    def check_game_state(self):
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

    def is_winning(self, player):
        # Check rows
        for i in range(1, 8, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] == player:
                return True
        # Check columns
        for i in range(1, 4):
            if self.board[i] == self.board[i+3] == self.board[i+6] == player:
                return True
        # Check diagonals
        if self.board[1] == self.board[5] == self.board[9] == player:
            return True
        if self.board[3] == self.board[5] == self.board[7] == player:
            return True
        return False

    def is_draw(self):
        for pos in self.board:
            if self.board[pos] == ' ':
                return False
        return True

    def move_player(self):
        while True:
            try:
                position = int(input("Enter your move (1-9): "))
                if 1 <= position <= 9:
                    self.update_player_position(self.player, position)
                    break
                else:
                    print("Please enter a number between 1 and 9")
            except ValueError:
                print("Please enter a valid number!")

    def move_computer(self):
        best_score = -float('inf')
        best_move = None
        
        for move in self.board:
            if self.is_cell_free(move):
                # Try the move
                self.board[move] = self.computer
                score = self.minimax(0, -float('inf'), float('inf'), False)
                # Undo the move
                self.board[move] = ' '
                
                if score > best_score:
                    best_score = score
                    best_move = move
        
        self.update_player_position(self.computer, best_move)

    def minimax(self, depth, alpha, beta, is_maximizer):
        # Base cases
        if self.is_winning(self.computer):
            return REWARD - depth
        if self.is_winning(self.player):
            return -REWARD + depth
        if self.is_draw():
            return 0
        
        if is_maximizer:  # Computer's turn (maximizing)
            best_score = -float('inf')
            for move in self.board:
                if self.is_cell_free(move):
                    self.board[move] = self.computer
                    score = self.minimax(depth + 1, alpha, beta, False)
                    self.board[move] = ' '
                    
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if alpha >= beta:
                        break
            return best_score
        else:  # Player's turn (minimizing)
            best_score = float('inf')
            for move in self.board:
                if self.is_cell_free(move):
                    self.board[move] = self.player
                    score = self.minimax(depth + 1, alpha, beta, True)
                    self.board[move] = ' '
                    
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if alpha >= beta:
                        break
            return best_score


if __name__ == '__main__':
    # Create empty board dictionary with keys 1 to 9, all set to space ' '
    board = {pos: ' ' for pos in range(1, 10)}

    # Instantiate TicTacToe game with this board
    game = TicTacToe(board)

    # Start the game loop
    game.run()