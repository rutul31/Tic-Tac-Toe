''' This is a simple Tic Tac Toe game'''
from os import system
board_num = " 7|8|9\n-------\n 4|5|6\n-------\n 1|2|3"
print("Welcome to Tic-Tac-Toe!")
print(board_num)
print("Instructions:\n1.Enter the number wherever you want to put X or O\n2.The numbers are set according to your numkeypad")
winner=True
def ttt():
    global winner
    board = "  | | \n-------\n  | | \n-------\n  | | "
    board_list = list(board)
    winner =True
    def play_num_choose():
        while True:
            player_no = input("Player 1 choose X or O: ")
            if player_no.upper() =='X' :
                return player_no.upper()
            elif player_no.upper()=='O':
                return player_no.upper()
            else:
                print("Invalid input! Please try again!")
    def display_board():
        system("cls")
        board = ''.join(board_list)
        print(board)
    def user_choice():
        global winner
        tup = {'1':31,'2':33,'3':35,'4':16,'5':18,'6':20,'7':1,'8':3,'9':5}
        print(board)
        new = True
        if play_num_choose()=='X':
            for i in range(0,5):
                clicked=True
                while clicked and winner :
                    p1 = input("Player one ( X ): ")
                    if p1 in tup.keys() :
                        board_list[tup[p1]] = 'X'
                        tup.pop(p1)
                        display_board()
                        check_win()
                        clicked = False
                    else:
                        print("Invalid input! Please try again!")
                clicked = True
                if i==4:
                    new=False
                while clicked and new and winner:
                    p1 = input("Player two ( O ) : ")
                    if p1 in tup.keys() :
                        board_list[tup[p1]] = 'O'
                        tup.pop(p1)
                        display_board()
                        check_win()
                        clicked = False
                    else:
                        print("Invalid input! Please try again!")
        else:
            for i in range(0,5):
                clicked=True
                while clicked and winner:
                    p1 = input("Player one ( O ): ")
                    if p1 in tup.keys() :
                        board_list[tup[p1]] = 'O'
                        tup.pop(p1)
                        display_board()
                        check_win()
                        clicked = False
                    else:
                        print("Invalid input! Please try again!")
                clicked = True
                if i==4:
                    new=False
                while clicked and new and winner:
                    p1 = input("Player two ( X ) : ")
                    if p1 in tup.keys() :
                        board_list[tup[p1]] = 'X'
                        tup.pop(p1)
                        display_board()
                        check_win()
                        clicked = False
                    else:
                        print("Invalid input! Please try again!")
    def check_win():
        global winner
        for i in (1,16,31):
            if board_list[i]=='X':
                i+=2
                if board_list[i]=='X':
                    i+=2
                    if board_list[i]=='X':
                        winner = False
                        print("player X wins!")
        for i in (1,3,5):
            if board_list[i]=='X':
                i+=15
                if board_list[i]=='X':
                    i+=15
                    if board_list[i]=='X':
                        winner = False
                        print("player X wins!")
        for i in {1}:
            if board_list[i]=='X':
                i+=17
                if board_list[i]=='X':
                    i+=17
                    if board_list[i]=='X':
                        winner = False
                        print("player X wins!")

        for i in {5}:
            if board_list[i]=='X':
                i+=13
                if board_list[i]=='X':
                    i+=13
                    if board_list[i]=='X':
                        winner = False
                        print("player X wins!")
        for i in (1,16,31):
            if board_list[i]=='O':
                i+=2
                if board_list[i]=='O':
                    i+=2
                    if board_list[i]=='O':
                        winner = False
                        print("player O wins!")
        for i in (1,3,5):
            if board_list[i]=='O':
                i+=15
                if board_list[i]=='O':
                    i+=15
                    if board_list[i]=='O':
                        winner = False
                        print("player O wins!")
        for i in {1}:
            if board_list[i]=='O':
                i+=17
                if board_list[i]=='O':
                    i+=17
                    if board_list[i]=='O':
                        winner = False
                        print("player O wins!")

    def play_again():
        global winner
        while True:
            if winner==True:
                print("Its a Draw!")
            again = input("Want to play again Y or N: ")
            if again.upper() =='Y':
                ttt()
                break
            elif again.upper() == 'N':
                break
            else:
                print("Sorry! I did not understand that try again!")
    def play():
        user_choice()
        play_again()
    play()
ttt()
