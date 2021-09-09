import time
import math
from player import HumanPlayer, ComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # 3x3 board
        self.current_winner = None
       
        
    def print_board(self):
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
      
            
    @staticmethod
    def print_board_nums():
        # | 0 | 1 | 2 |
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    
    def available_moves(self):
        return[i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # 
        #     if spot == ' ':
        #         moves.append(i)
        # return moves
        
    
    def empty_squares(self):
        return ' ' in self.board
    
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    # runs after each move
    # if there is a winner, returns True
    def winner(self, square, letter):
        # check rows
        # index:0 ... self.board[0:3] ... 0,1,2
        # index:1 ... self.board[3:6] ... 3,4,5
        # index:2 ... self.board[6:9] ... 6,7,8
        row_ind = square // 3 # result without decimal part
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # check columns
        # index:0 ... self.board[0->3->6]
        # index:1 ... self.board[1->4->7]
        # index:2 ... self.board[2->5->8]
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # check diagonals    
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        
        return False    
    
    
def play(game, x_player, o_player, print_game=True):
   
    if print_game:
        game.print_board_nums()
    
    # first move is always X
    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square,letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')
                
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
                    
            
            # after a move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X'
        
        # puts some time interval between the moves
        time.sleep(.9)
    
    if print_game:
        print('It\'s a tie!')
        
        

if __name__ == '__main__':
    # players can assign differently 
    x_player = HumanPlayer('X') # X player will be human
    o_player = ComputerPlayer('O') # O player will be computer
    
    t = TicTacToe()
    # print_game property automatically assigned to True,
    # that is going to be helpful while making computer play with itself 
    # and just counting the wins without printing the game for the sake of probability 
    play(t, x_player, o_player, print_game=True)