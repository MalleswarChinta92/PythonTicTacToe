from IPython.display import clear_output

def printBoard(board):
    clear_output()
    print(board[7] + ' |' + board[8] + ' | ' + board[9])
    print(board[4] + ' |' + board[5] + ' | ' + board[6])
    print(board[1] + ' |' + board[2] + ' | ' + board[3])

def playerInput():
    marker = ''
    while (marker != 'X' and marker != 'O'):
        marker = input('Choose your marker Player 1')
    player1 = marker
    if (player1 == 'X'):
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)

def replay():
    choice = input('Do you want to replay')
    return choice == 'YES'

def isWin(board):
    return (board[1] != '' and (board[1] == board[2] == board[3])) or  (board[4] != '' and (board[4] ==  board[5] ==  board[6])) or (board[7] != '' and (board[7] ==  board[8] ==  board[9])) or (board[1] != '' and (board[1] ==  board[5] ==  board[9])) or (board[3] != '' and (board[3] ==  board[5] ==  board[7]))

def isFull(board):
    for i in range(1,10):
        if (board[i] == ''):
            return False
    return True

def canPutMarker(board, position):
    if position not in range (1,10):
        return False
    return board[position] == ''

print('Welcome to Tic Tac Toe')
playNow = True
while playNow:
    player1, player2 = playerInput()
    player1Turn = True
    board = ['']*10
    while True:
        printBoard(board)
        if (not isFull(board) or isWin(board)):
            currentMarker = player1 if player1Turn else player2
            currentGamer = 'player1' if player1Turn else 'player2'
            position = 0
            while position == '' or position == 0 or not canPutMarker(board, position):
                try:
                    position = int(input('Input your position ' + currentGamer))
                except ValueError:
                    print('Please input a value between 0 and 9')
                    continue
            board[position] = currentMarker
            if (isWin(board)):
                print(currentGamer + 'Wins')
                playNow = replay()
                break
            elif (isFull(board)):
                print('Tie')
                playNow = replay()
                break
            player1Turn = not player1Turn

            
