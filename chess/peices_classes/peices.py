from enum import Enum

class Color(Enum):
    BLACK = 1
    WHITE = 2

class King():
    def __init__(self, row, col, color):
        '''
        color (Color): BLACK or WHITE
        '''


class Pawn():
    def __init__(self, row, col, color):
        '''
        color (Color): BLACK or WHITE
        '''
        self.row = row
        self.col = col
        self.color = color
    
    def get_legal_moves(self, Board):
        '''
        TODO: function does not check if player is in check

            - pawns can move up one if there is no piece blocking
            - pawns can move up two if they are in itial position
            - pawns can take diagonally
            - pawns can transform if they reach the opposite side of the board
        '''
        legal_moves = set() # return value #1
        can_transform = False # return value #2 

        if self.color == Color.WHITE:
            if (Board.board[self.row + 1][self.col] == None):
                legal_moves.add((self.row + 1, self.col))
            if (Board.board[self.row + 1][self.col + 1] != None):
                legal_moves.add(self.row + 1, self.col + 1)
            if (Board.board[self.row + 1][self.col - 1] != None):
                legal_moves.add(self.row + 1, self.col - 1)
            if (Board.board[self.row + 1][self.col] == None and \
                Board.size == self.row + 2):
                # piece can transform
                can_transform = True
        else:  # it must be true that color == Color.BLACK
            if (Board.board[self.row - 1][self.col] == None):
                legal_moves.add((self.row - 1, self.col))
            if (Board.board[self.row - 1][self.col + 1] != None):
                legal_moves.add(self.row - 1, self.col + 1)
            if (Board.board[self.row - 1][self.col - 1] != None):
                legal_moves.add(self.row - 1, self.col - 1)
            if (Board.board[self.row - 1][self.col] == None and \
                self.row - 2 == 0):
                # piece can transform
                can_transform = True
        
        return legal_moves, can_transform
    
    def move(self, Board, row, col, transform_into = None):
        '''
        If a pawn moves to a location where there is already a piece, the piece
        in that location will be taken (model doesn't have to emmit any 
        <Take_Piece> token)

        For research purposes, we do not include a check for if it is legal for
        the pawn to take actions in this function (e.g., turning into a Queen 
        even if it hasn't reached the end of the board). We want to see if the 
        model learns to cheat. 
        '''
        old_row = self.row
        old_col = self.col
        Board.board[row][col] = Board.board[old_row][old_col] # move the piece in the board class
        Board.board[old_row][old_col] = None
        self.row = row
        self.col = col

        if transform_into != None:
            # TODO: transform into another class (Queen, Knight, ect) if needed
            pass

    def __str__(self) -> str:
        return " P "
    



