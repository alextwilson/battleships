from battleships_board import Board

ships_remaining = 1
board = Board(5,5)
ship_row = board.random_row()
ship_column = board.random_column()

while ships_remaining != 0:

    board.display()
    print(ship_column)
    print(ship_row)
    guess_column = int(input("\nWhat column do you guess? \n"))
    guess_row = int(input("\nWhat row do you guess? \n"))

    if (guess_row == ship_row) and (guess_column == ship_column):
        ships_remaining -= 1
        board.update_board_hit(guess_row, guess_column)
        board.display()
        print("\nHit! You sunk the battleship! Many lives were lost.")
        print("\nWas it worth it?")
        print("\nAre you safe?\n")
        break

    else:
        if (guess_row < 1 or guess_row > board.rows) or (guess_column < 1 or guess_column > board.columns):
            print("\nSuper miss.\n")

        elif (board.grid[guess_row-1][guess_column-1] == "O"):
            print("\nYou guessed that already.\n")

        else:
            print("\nMiss.\n")
            board.update_board_miss(guess_row, guess_column)
