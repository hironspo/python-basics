# this a basic game to play battleship
import random

board = []

for x in range(0,5):
    board.append(["O"] * 5)

def printBoard(board):
    for row in board:
        print(' '.join(row))

printBoard(board)

def randomRow(board):
    return random.randint(0, len(board) - 1)

def randomCol(board):
    return random.randint(0, len(board[0]) - 1)

shipRow = randomRow(board)
shipCol = randomCol(board)

# debuggers - delete before paying
#print(shipRow)
#print(shipCol)

for turn in range(4):
    print('Turn', turn + 1)
    guessRow = int(input('Guess row: '))
    guessCol = int(input('Guess colomn: '))

    if guessRow == shipRow and guessCol == shipCol:
        print('Congratulations! You sank my battleship!')
        break
    else:
        if guessRow not in range(5) or guessCol not in range(5):
            print('Oops, that is not even in the ocean')
        elif board[guessRow][guessCol] == "X":
            print('You guessed that already')
        else:
            print('Missed')
            board[guessRow][guessCol] = "X"
            if turn == 3:
                print('Game over!')
            printBoard(board)
