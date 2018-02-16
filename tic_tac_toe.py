board = [' ' for i in range(9)]


def print_board(board):
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def player_move(icon):
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2
    print('Your turn player {}'.format(number))
    choice = int(input('Enter your move (1-9)').strip())
    if board[choice - 1] == ' ':
        board[choice - 1] = icon
        if is_victory(icon):
            print('Won')
    else:
        print()
        print('That space is empty')


def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon):
        print('Hello')


while True:
    print_board(board)
    player_move('X')
    print_board(board)
    player_move('O')