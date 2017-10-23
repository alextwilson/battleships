import random

class Board():

    def __init__(self, columns=8, rows=8):
        self.columns = columns
        self.rows = rows
        self.grid = [ [' ' for x in range(columns)] for y in range(rows)]

    def display(self):
        column_names = '123456789'[:self.columns]
        print('  |' + '|'.join(column_names) + '|')
        for number, row in enumerate(self.grid, 1):
            print(number, '|' + '|'.join(row) + '|')

    def random_row(self):
        return random.randint(1,len(self.grid))

    def random_column(self):
        return random.randint(1,len(self.grid[0]))

    def update_board_hit(self, guess_row, guess_column):
        self.grid[guess_row-1][guess_column-1] = 'X'

    def update_board_miss(self, guess_row, guess_column):
        self.grid[guess_row-1][guess_column-1] = 'O'
