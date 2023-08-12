def show_board(tictac):
    for row in tictac:
        print(row)


def update_board(player,row,col,tictac):
    try:
        if(tictac[row][col]!=0):
            return tictac,False
        tictac[row][col]=player
        return tictac, True
    except Exception as e:
        return tictac,False

    
def win(tictac,selected_player):
    #Horiizontal check
    for row in tictac:
        if row.count(row[0])==len(row) and row[0]!=0:
            print(f"{selected_player} has won Horizontally")
            return True 
    
    #Vertical check:
    for col in range(len(tictac)):
        cols=[]
        for row in range(len(tictac)):
            cols.append(tictac[row][col])
        if cols.count(cols[0])==len(cols) and cols[0]!=0:
            print(f"{selected_player} has won Verically") 
            return True

    #Diagonal checks
    diag1=[]
    diag2=[]

    for i in range(len(tictac)):
        diag1.append(tictac[i][i])
    
    count=0
    for i in range(len(tictac)-1,-1,-1):
        diag2.append(tictac[count][i])
        count+=1
    
    if diag1.count(diag1[0])==len(diag1) and diag1[0]!=0:
            print(f"{selected_player} has won Diagonally left to right")
            return True 
    if diag2.count(diag2[0])==len(diag2) and diag2[0]!=0:
            print(f"{selected_player} has won Diagonally right to left")
            return True 
    return False


#Play Starts

import os
play_game=True

while play_game:
    
    #Tictactoe board Creation
    tictac=[]
    board_size=int(input("Enter tictactoe board size : "))
    for i in range(board_size):
        row=[]
        for j in range(board_size):
            row.append(0)
        tictac.append(row)
        
    show_board(tictac)
    print("-------------------------------------------------------------------------------------------------------------------------------")

    #Players playing Game Starts With X
    playing=True
    players=['X','O']
    choice=0
    total_moves= board_size*board_size
    actual_moves=0
    while playing:
        #Player X starts the game 
        selected_player=players[choice%2]
        choice+=1

        print(f"Player {selected_player} move now ")
        row=int(input("Enter row number to select (0 to board_size-1) "))
        col=int(input("Enter column number to select (0 to board_size-1) "))
        #Updates The board
        tictac,error=update_board(selected_player,row,col,tictac)
        current_move=actual_moves
        actual_moves+=1
        
        #If Update is not sucessful 
        if error==False:
            choice=choice-1
            print(f"Player {selected_player} selected positon already occupied!! OR WRongly Selected")
            actual_moves=current_move
        
        #else if update is successful
        show_board(tictac)

        print("-------------------------------------------------------------------------------------------------------------------------------")
        #Check win
        output=win(tictac,selected_player)
        
        #If output is True means one of the player won the game
        if output or actual_moves==total_moves:
            playing=False
            want_to_play_again= input("Want to play again yes|no :")
            if want_to_play_again.lower()=='yes':
                os.system('cls')
                play_game=True
                playing=False
            else:
                play_game=False
                playing=False
                os.system('cls')

        

