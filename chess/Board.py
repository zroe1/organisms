from peices_classes.peices import Pawn 

class Board:
    def __init__(self):
        self.size = 8
        self.board = [[None for _ in range(self.size)] for _ in range(self.size)]
        for j in range(self.size):
            self.board[2][j] = Pawn(2, j, "white")
        for j in range(self.size):
            self.board[self.size - 2][j] = Pawn(self.size - 2, j, "black")


    def pprint_board(self):
        divider_row = ['-'] + ['----' for _ in range(self.size)]
        print("".join(divider_row))
        for i in range(self.size):
            current_row = []
            for j in range(self.size):
                current_piece = self.board[i][j]
                # print(current_piece)
                # print("*" * 80)
                # print(str(current_piece))
                if current_piece != None:
                    current_row += [f'|{current_piece}']
                else:
                    current_row += "|   "
            current_row += ['|']
            print("".join(current_row))
            print("".join(divider_row))

b = Board()
b.pprint_board()