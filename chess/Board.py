class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None] for _ in range(self.size)]

    def pprint_board(self):
        divider_row = ['-'] + ['----' for _ in range(self.size)]
        print("".join(divider_row))
        for i in range(self.size):
            print("".join(['|   ' for _ in range(self.size)] + ['|']))
            print("".join(divider_row))


b = Board(5)
b.pprint_board()