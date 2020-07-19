#!/usr/bin/env python
# coding: utf-8

# Creating the tic tac toe game. 
# 
# 
# Actions
# * Display a board 
# * Allow and verify user input
# * Replace user input with an X or O 
# * Ask if user wants to replay or end
# 
# Notes:
# * Display board after every turn 
# * Make sure while loops end when the correct condition is entered 
# 


#Print rules and instructions at the beginning of the game 

def rules():
    print("""Welcome to Tic Tac Toe! 
    
Here's how to play: 
    1. Pick a number to replace on the board. It will be replaced with X or O - depending on what you were assigned.
    2. Normal tic tac toe rules apply.
    3. You will be able to replay the game at the end.""")


# In[20]:


#rules()


# In[21]:


#Displays the lists required to create a board

from IPython.display import clear_output

board = list(range(0,10))

def display_board(board): 
    clear_output()
    print(' ' + str(board[1]) + ' | ' + str(board[2]) + ' | ' + str(board[3]))
    print("----------")
    print(' ' + str(board[4]) + ' | ' + str(board[5]) + ' | ' + str(board[6]))
    print("----------")
    print(' ' + str(board[7]) + ' | ' + str(board[8]) + ' | ' + str(board[9]))



#Asks the player to enter a number between 1 and 9. Then returns that number as an integer.
def player_input():
    user_choice = 'not digit' #this the original value - not an integer.
    
    #accepted = list(range(1,10))
    
    while user_choice.isdigit() == False: #while the choice isn't a digit and not in the range, keep asking for an input. 
        user_choice = int(input("Please pick a number you would like to replace (1 - 9): "))
        if user_choice not in board: 
            print("Sorry that is not a valid. Please enter a number between 1 and 9:")
            user_choice = 'False'
        else:
            return user_choice
    return int(user_choice)


#Asks the player if they'd like to be X or O
def player_marker():
    m = ""
    while not m == ((m =='X' or m == 'O')):
        m = input("Would you like to be X or O?").upper()
 
    #this then determines the order they will go in.      
        if m == "X":
            return ("X", "O")
        else: 
            return ("O", "X")

#REPLACEMENT FUNCTION - should take the number chosen in the board, replace it with an X or O
def replacement(board, m, position):
    board[position] = m #Takes the board at position selected and replaces it with the marker the user has chosen


#win function

def win_check(board, m): #checks the board for m in a row of 3.
    return ((board[1] == m and board[2] == m and board[3] == m) #top
        or (board[4] == m and board[5] == m and board[6] == m) #middle
        or (board[7] == m and board[8] == m and board[9] == m) #bottom
        or (board[1] == m and board[4] == m and board[7] == m) #col1
        or (board[2] == m and board[5] == m and board[8] == m) #col2
        or (board[3] == m and board[6] == m and board[9] == m) #col3
        or (board[1] == m and board[5] == m and board[9] == m)) #diagonal

#checks if there is a space on the board.
#Doesn't work

def space_on_board(board):
    List1 = list(range(1,10))
    List2 = board
    space_is_true = any(x in List1 for x in List2)
 
    if space_is_true == True:
        print("The board is not full")
        return True #if 1 - 9 appears on the board
    else:
        print("The board is full - the game is a draw")
        return False #if 1 - 9 doesn't appear on the board

return True


full_board = ["X", "O","X", "O","X", "O","X", "O", "X"]
space = [1, 2, 3, 4, 5, 6, 7, 8, "X"]

space_on_board(space)

# Chooses who goes first 
import random 

def choose_first():
    if random.randint(0,1) == 0:
        return "Player 1"
    else:
        return "Player 2"


#Asks the player if they want to replay the game. Returns a True if they do 
def replay():
    return input("Would you like to play again? Enter 'Yes' or 'No' ").lower().startswith('y')

#The whole game put together... 

rules()

while True: 
    #setting up the game
    board = list(range(0,10))
    marker_1, marker_2 = player_marker()
    display_board(board)
    turn = choose_first()
    print(turn + " will go first!")
    
    play_game = input("Would you like to begin? Enter yes or no")
    
    if play_game.lower()[0] == "y": #Why not "yes"? Because people can enter "yes " which breaks the code. 
        game_con = True
    else:
        game_con = False
    
    while game_con: #while it is true
        if turn == "Player 1": #Player 1's turn 
            print("Player 1's turn. Please place an " + marker_1)
            display_board(board) #shows the board
            position = player_input() #asked for their position. It should be part of the board (if it isn't , they'll be asked again)
            replacement(board, marker_1, position) #if the above is true, then it takes the position and replaces it on the board 
            if win_check(board, marker_1) == True:
                display_board(board)
                print("Congrats! Player 1 won!")
                game_con = False
            else: #To check if it's a draw
                if space_on_board(board) == False: #if the board is full
                    display_board(board)
                    print("The game is a draw!")
                    break
                else:
                    turn = 'Player 2'
                    
        else:
            if turn == "Player 2": #Player 2's turn 
                print("Player 2's turn. Please place an " + marker_2)
                display_board(board) #shows the board
                position = player_input() #asked for their position. It should be part of the board (if it isn't , they'll be asked again)
                replacement(board, marker_2, position) #if the above is true, then it takes the position and replaces it on the board 
                if win_check(board, marker_2) == True:
                    display_board(board)
                    print("Congrats! Player 2 won!")
                    game_con = False
                else: #To check if it's a draw
                    if space_on_board(board) == False: #if the board is full
                        display_board(board)
                        print("The game is a draw!")
                        break
                    else:
                        turn = 'Player 1'
                       
    if not replay(): #asking if they want to replay the game if "game_con" isn't true
        break




