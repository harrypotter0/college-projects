from __future__ import print_function
import random



def display_board(board):
    print(board[6], '|', board[7], '|', board[8])
    print('----------')
    print(board[3], '|', board[4], '|', board[5])
    print('----------')
    print(board[0], '|', board[1], '|', board[2])



def player_input():
    print('Player1 : Do you want "X" or "O"?')
    player1= raw_input().upper()

    while not(player1=='X' or player1=='O'):
        print('Please enter the correct mark')
        player1 = raw_input().upper()

    if player1=='X':
        return ('X','O')
    else:
        return ('O','X')




def place_marker(board, marker, position):
    board[position] = marker
    display_board(board)


def choose_first():  # Assign first turn
    draw = random.randint(0, 1)  # generate random number either '0' or '1'
    if draw == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):  # Check if chosen position is empty or not
    if board[position] == " ":
        return True
    else:
        return False


def full_board_check(board):  # Check if board is still empty or not
    for index in range(0,9):

        if space_check(board,index):
            return False



    return True   


def win_check(board, mark):
    index = 0
    while index <= 8:

        # if %3==0
        if index % 3 == 0:

            # check the same marker horizontally
            i = index
            while i <= index + 2:
                if board[i] != mark:
                    break

                i += 1
            if i > index + 2:
                return True

                # if >=0 and <=2
        if index >= 0 and index <= 2:

            # check vertically
            i = index
            while i <= index + 6:
                if board[i] != mark:
                    break
                i += 3

            if i > index + 6:
                return True


                # check diagonally for only %2==0
            if index % 2 == 0:
                
                i = index

                # if position is 0
                if index == 0:
                    increment = 4
                # if position is 2
                if index == 2:
                    increment = 2

                while i <= index + increment * 2:
                    if board[i] != mark:
                        break
                    i = i + increment

                if i > index + increment * 2:
                    return True

        index = index + 1

    return False

def player_choice(board):

    print('Enter the position 1-9')

    position = int(raw_input())

    while not (position in range(1,10)):
        print('Please enter the position 1-9 only')
        position = int(raw_input())
    return position


def replay():
    print('Wanna replay? Enter "y" to continue "n" to exit')
    return raw_input().lower().startswith('y')
  


print('Welcome to Tic Tac Toe Game!')


while True:

    board = [" "] * 9
    player1, player2 = player_input()  # getting  elements from tuples
    
    display_board(board)

    turn = choose_first()
    print(turn +' will go first')
    game_on=True

    while game_on:
    
        if turn =='Player 1':
            print('Player 1')
            pos = player_choice(board)
            while not(space_check(board,pos-1)):
                print('Position already filled Please enter again ')
                pos= int(raw_input())
            else:
                place_marker(board,player1,pos-1)


            if win_check(board,player1):
                print('Congratulation',turn,'Win')

                game_on=False

            if full_board_check(board):
                print('Match draw')
                game_on=False
                break

            turn = 'Player 2'
    
        else:
          
            if turn=='Player 2':


                print('Player 2')
                pos = player_choice(board)
                while not(space_check(board,pos-1)):
                    print('Position already filled Please enter again ')
                    pos= int(raw_input())
                else:
                    place_marker(board,player2,pos-1)


                if win_check(board,player2):
                    print('Congratulation',turn,'Win')
                    game_on=False

                if full_board_check(board):
                    print('Match draw')
                    game_on=False
                    
                turn = 'Player 1'

    if not replay():
        print('Thanks for playing')
        break
