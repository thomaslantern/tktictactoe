import random
import tkinter as tk
from tkinter import ttk

board_list = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
available_moves = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
gameExit = False
turn = ""
player_move = ""
difficulty = []
comp_strategy = 0


root = tk.Tk()
root.title("Tic Tac Toe")


canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()

game_text = tk.Label(canvas, text = "Welcome to \n Tic Tac Toe \n Please Choose Game Difficulty:")
game_text.grid(row = 0, column = 1)

easy = ttk.Button(canvas, text = "Easy", command = lambda: difficulty.append("E"))
easy.grid(row=2, column=0)

difficult = ttk.Button(canvas, text = "Difficult")
difficult.grid(row=2, column=1)

impossible = ttk.Button(canvas, text = "Impossible")
impossible.grid(row=2, column=2)

gameboard = tk.Canvas(canvas, width = 600, height = 600)
gameboard.grid(row=3, column=0)

tict = gameboard.create_line(10, 10, 55, 10, fill="blue", width=10)
tict2 = gameboard.create_line(35, 10, 35, 70, fill="blue", width=10)

tici = gameboard.create_line(65, 10, 65, 70, fill="blue", width=10)

ticc = gameboard.create_line(75, 10, 120, 10, fill="blue", width=10)
ticc2 = gameboard.create_line(80, 10, 80, 60, fill="blue", width=10)
ticc3 = gameboard.create_line(75, 65, 120, 65, fill="blue", width=10)

tact = gameboard.create_line(130, 10, 175, 10, fill="blue", width=10)
tict2 = gameboard.create_line(155, 10, 155, 70, fill="blue", width=10)

taca = gameboard.create_line(185, 10, 215, 10, fill="blue", width=10)
taca2 = gameboard.create_line(185, 10, 185, 70, fill="blue", width=10)
taca3 = gameboard.create_line(215, 10, 215, 70, fill="blue", width=10)
taca4 = gameboard.create_line(185, 40, 215, 40, fill="blue", width=10)

tacc = gameboard.create_line(225, 10, 270, 10, fill="blue", width=10)
tacc2 = gameboard.create_line(230, 10, 230, 60, fill="blue", width=10)
tacc3 = gameboard.create_line(225, 65, 270, 65, fill="blue", width=10)

toet = gameboard.create_line(280, 10, 325, 10, fill="blue", width=10)
toet2 = gameboard.create_line(305, 10, 305, 70, fill="blue", width=10)

toeo = gameboard.create_line(335, 10, 365, 10, fill="blue", width=10)
toeo2 = gameboard.create_line(335, 10, 335, 60, fill="blue", width=10)
toeo3 = gameboard.create_line(335, 65, 365, 65, fill="blue", width=10)
toeo4 = gameboard.create_line(365, 10, 365, 60, fill="blue", width=10)

toee = gameboard.create_line(385, 10, 415, 10, fill="blue", width=10)
toee2 = gameboard.create_line(385, 10, 385, 60, fill="blue", width=10)
toee3 = gameboard.create_line(385, 65, 415, 65, fill="blue", width=10)
toee4 = gameboard.create_line(385, 37, 415, 37, fill="blue", width=10)
#toee

board_line_y = gameboard.create_line(250, 150, 250, 450, fill = "black", width=5)
board_line_y2 = gameboard.create_line(350, 150, 350, 450, fill = "black", width=5)
board_line_x = gameboard.create_line(150, 250, 450, 250, fill = "black", width=5)
board_line_x2 = gameboard.create_line(150, 350, 450, 350, fill = "black", width=5)


board_line_centrex = gameboard.create_line(255, 345, 345, 255, fill = "red", width=5)
board_line_centrex = gameboard.create_line(255, 255, 345, 345, fill = "red", width=5)

board_line_lowerx = gameboard.create_line(155, 445, 245, 355, fill = "red", width=5)
board_line_lowerx = gameboard.create_line(155, 355, 245, 445, fill = "red", width=5)

board_line_upperx = gameboard.create_line(355, 155, 445, 245, fill = "red", width=5)
board_line_upperx = gameboard.create_line(355, 245, 445, 155, fill = "red", width=5)


root.mainloop()




#Set a value for each row, column, and diagonal respectively to facilitate best computer moves
board_values = [0, 0, 0, 0, 0, 0, 0, 0]


def display_board(board):
    print(board_list[0])
    print(board_list[1])
    print(board_list[2])
    print("\n")


#Update board_values to optimize computer moves as well as for checking for winner
def update_values(board_vals, coords, player):

    #default amount to add; 2 for player, 5 for computer
    amount = 0


    if player == "P":
        amount = 2
    else:
        amount = 5


    if coords == [0, 0]:
        board_vals[0] += amount
        board_vals[3] += amount
        board_vals[6] += amount
    elif coords == [0, 1]:
        board_vals[0] += amount
        board_vals[4] += amount
    elif coords == [0, 2]:
        board_vals[0] += amount
        board_vals[5] += amount
        board_vals[7] += amount
    elif coords == [1, 0]:
        board_vals[1] += amount
        board_vals[3] += amount
    elif coords == [1, 1]:
        board_vals[1] += amount
        board_vals[4] += amount
        board_vals[6] += amount
        board_vals[7] += amount
    elif coords == [1, 2]:
        board_vals[1] += amount
        board_vals[5] += amount
    elif coords == [2, 0]:
        board_vals[2] += amount
        board_vals[3] += amount
        board_vals[7] += amount
    elif coords == [2, 1]:
        board_vals[2] += amount
        board_vals[4] += amount
    elif coords == [2, 2]:
        board_vals[2] += amount
        board_vals[5] += amount
        board_vals[6] += amount

    return board_vals


def computer_move(board_vals, difficulty):

    if difficulty == "I":
            if max(board_vals) == 2 and [1, 1] not in available_moves:
                return 0
    
    board_index = 0
    highest_val = 0
    best_move = 0
    print("BOARD VALS:")
    print(board_vals)
    for vals in board_vals:
        if vals == 10:
            highest_val = 14
            best_move = board_index
        elif vals == 4 and highest_val != 14:
            print("DO IT WEE BABABADABO")
            highest_val = 13
            best_move = board_index
        elif vals > highest_val and vals not in (7, 9, 12):
            highest_val = vals
            best_move = board_index
        board_index += 1
    print("STRATEGY: " + str(best_move))
    print("HIGHEST VAL: " + str(highest_val))
    return best_move
    
    
print("Welcome to Tic Tac Toe!")
print("You will be playing against the computer.")
   
while not gameExit:    
    
    
    
    #while difficulty.upper() not in ("E", "D", "I"):
     #   print("Please choose the difficulty level of the computer")
      #  difficulty = input("(E)asy, (D)ifficult, (I)mpossible: ")

       
    while turn.upper() != "P" and turn.upper() != "C":
        print("Please choose whether you would like to go first.")
        turn = input("(P)layer, (C)omputer: ")


    

    
    if turn.upper() == "C":
        display_board(board_list)
        if difficulty.upper() == "D" or difficulty.upper() == "I":
            print("Computer is taking its turn...")
            #insert an "X" into the center of the board if it's empty
            if board_list[1][1] == "5":
                board_list[1][1] = "X"
                available_moves.remove([1, 1])
                board_values = update_values(board_values, [1, 1], "C")
                turn = "P"
            else:
                comp_strategy = computer_move(board_values, difficulty.upper())
                #insert an "X" into a row if it's the best move
                if comp_strategy == 0:
                    for number in range(0, 3):
                        if [0, number] in available_moves and turn !="P":
                            board_list[0][number] = "X"
                            available_moves.remove([0, number])
                            board_values = update_values(board_values, [0, number], "C")
                            turn = "P"
                elif comp_strategy == 1:
                    for number in range(0, 3):
                        if [1, number] in available_moves and turn !="P":
                            board_list[1][number] = "X"
                            available_moves.remove([1, number])
                            board_values = update_values(board_values, [1, number], "C")
                            turn = "P"          
                elif comp_strategy == 2:
                    for number in range(0, 3):
                        if [2, number] in available_moves and turn !="P":
                            board_list[2][number] = "X"
                            available_moves.remove([2, number])
                            print([2, number])
                            board_values = update_values(board_values, [2, number], "C")
                            turn = "P"
                #insert an "X" into a column if it's the best move
                elif comp_strategy == 3:
                    for number in range(0, 3):
                        if [number, 0] in available_moves and turn !="P":
                            board_list[number][0] = "X"
                            available_moves.remove([number, 0])
                            board_values = update_values(board_values, [number, 0], "C")
                            turn = "P"
                elif comp_strategy == 4:
                    for number in range(0, 3):
                        if [number, 1] in available_moves and turn !="P":
                            board_list[number][1] = "X"
                            available_moves.remove([number, 1])
                            board_values = update_values(board_values, [number, 1], "C")
                            turn = "P"
                elif comp_strategy == 5:
                    for number in range(0, 3):
                        if [number, 2] in available_moves and turn !="P":
                            board_list[number][2] = "X"
                            available_moves.remove([number, 2])
                            board_values = update_values(board_values, [number, 2], "C")
                            turn = "P"
                #insert an "X" into the top-left to bottom-right diagonal if it's the best move                       
                elif comp_strategy == 6:
                    for number in range(3):
                        if [number, number] in available_moves and turn !="P":
                            board_list[number][number] = "X"
                            available_moves.remove([number, number])
                            board_values = update_values(board_values, [number, number], "C")
                            turn = "P"
                else:
                    for number in range(3):
                        if [number, (2 - number)] in available_moves and turn !="P":
                            print([number, (2 - number)])
                            board_list[number][2 - number] = "X"
                            available_moves.remove([number, (2 - number)])
                            board_values = update_values(board_values, [number, (2 - number)], "C")
                            turn = "P"
        else:
            new_move = random.choice(available_moves)
            available_moves.remove(new_move)
            board_list[new_move[0]][new_move[1]] = "X"
            board_values = update_values(board_values, new_move, "C")
            turn = "P"
            

        
        
    if 15 in board_values:
        display_board(board_list)
        print("Computer wins!")
        gameExit = True
    elif available_moves == [] and not gameExit:
        display_board(board_list)
        print("Tie game!")
        gameExit = True
        
    #Player's Turn
    elif turn.upper() == "P":
    
        display_board(board_list)
         
        print("It is your turn. Please choose where to place your piece.")
        player_move = input("Choose one of the listed numbers to place your piece. \n")
        try:
            player_move = int(player_move)
            #find player's choice in board_value list
            board_row = int((player_move - 1) / 3)
            board_col = (player_move - 1) % 3
            

            if board_list[board_row][board_col] == "X" or board_list[board_row][board_col] == "O":
                print("Please choose an unoccupied space.")
            else:
                board_list[board_row][board_col] = "O"
               
                # CALL BOARD VALUES
                available_moves.remove([board_row, board_col])
                board_values = update_values(board_values, [board_row, board_col], "P")
                turn = "C"
        except:
            print("Please make a valid choice for your move.")

        

    if 6 in board_values:
        display_board(board_list)
        print("Player wins!")
        gameExit = True
    elif available_moves == [] and not gameExit:
        display_board(board_list)
        print("Tie game!")
        gameExit = True

root.mainloop()

