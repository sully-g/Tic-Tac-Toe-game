from IPython.display import clear_output

def display_board(board):
    clear_output()
    print (board[7] + "|" + board[8] + "|" + board[9]) 
    print ("-|-|-")      
    print (board[4] + "|" + board[5] + "|" + board[6]) 
    print ("-|-|-")      
    print (board[1] + "|" + board[2] + "|" + board[3]) 
        
          
        
    
    pass



test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


from IPython.display import clear_output

def player_input():
    player1_marker = "wrong"
    
    while player1_marker != "X" and player1_marker!= "O":
        player1_marker = input("Player 1 please choose the marker X or O: ").upper()
        
        if player1_marker not in ["X","O"]:
            clear_output()
            print("Sorry, your marker is invalid. Choose X or O")
    
    if player1_marker == "X":
        player2_marker = "O"
    else:
        player2_marker = "X"
    
    return (player1_marker,player2_marker)


def place_marker(board, marker, position):
    board[position] = marker
    
    
    pass

def win_check(board, mark):
    if (board[7] == board[8] == board[9] == mark)\
    or(board[4] == board[5] == board[6] == mark)\
    or(board[1] == board[2] == board[3] == mark)\
    or(board[7] == board[4] == board[1] == mark)\
    or(board[8] == board[5] == board[2] == mark)\
    or(board[9] == board[6] == board[3] == mark)\
    or(board[7] == board[5] == board[3] == mark)\
    or(board[1] == board[5] == board[9] == mark):
        return True
    else:
        pass
    
import random

def choose_first():
    first_player = random.randint(0,1)
    if first_player == 0:
        return 'Player 1'
    else:
        return 'Player 2'
 

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

        
    return position


def replay():
    
    decision = 'wrong'
    
    while decision not in ['Y','N']:
        
        decision = input("Would you like to keep playing? Y or N ")
        
        if decision not in ['Y','N']:
            clear_output()
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")

    
    return decision == "Y"






#WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to Tic Tac Toe!')

while True:
    
    #PLAY GAME
    
    ##SET GAME UP (BOARD, WHO's FIRST, CHOOSE MARKERS)
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn + "will go first")
    
    play_game = input ("Ready to play? yes or no? ")
    
    if play_game == "yes":
        game_on = True
    else:
        game_on = False
    
    ##GAMEPLAY
    while game_on:
        
        if turn == "Player 1":
           ###PLAYER ONE TURN 
            #show the board
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            #Place the marker on the position
            place_marker(the_board,player1_marker,position)
            #check if won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print ("PLAYER 1 HAS WON")
                game_on = False
            
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                #no tie and no win? then next player's turn
                
                else:
                    turn = "Player 2"
 ###PLAYER TWO TURN
                       
        else:
            #show the board
            display_board(the_board)
            #choose a position
            position = player_choice(the_board)
            #Place the marker on the position
            place_marker(the_board,player2_marker,position)
            #check if won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print ("PLAYER 2 HAS WON")
                game_on = False
            
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                #no tie and no win? then next player's turn
                
                else:
                    turn = "Player 1"
    
    
    if not replay():
        break




#BREAK OUT OF WHILE LOOP ON REPLAY()
