class Pieces:
    def __init__(self, my_cords, color):
        self.my_cords = my_cords
        self.color = color


class Pawn(Pieces):
    def __init__(self, my_cords, color):
        super().__init__(my_cords, color)

    def move(self, my_cords, color, n):
        x, y = my_cords.copy()
        if color == 'b':
            my_cords[0] += n  # cords = [1, 5]
        else:
            my_cords[0] -= n
        table[my_cords[0]][my_cords[1]] = table[x][y]
        table[x][y] = None



table = [[None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None]]

for i in range(8):
    table[1][i] = Pawn([1, i], 'b')
    table[6][i] = Pawn([6, i], 'w')

table[6][4].move(table[6][4].my_cords, table[6][4].color, 2)

for i in range(8):
    for j in range(8):
        if table[i][j] != None:
            print(table[i][j].color, end='    ')
        else:
            print(table[i][j], end=' ')
    print()