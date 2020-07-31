import random
import tkinter as tk
from tkinter import ttk



board_list = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
available_moves = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
turn = ""
player_move = ""
difficulty = []
drawing_list = []

#Set a value for each row, column, and diagonal respectively to facilitate best computer moves
board_values = [0, 0, 0, 0, 0, 0, 0, 0]


root = tk.Tk()
root.title("Tic Tac Toe")


def reload_game():
    easy.grid(row=2, column=0)
    difficult.grid(row=2, column=1)
    impossible.grid(row=2, column=2)
    play_again_yes.grid_forget()
    play_again_no.grid_forget()
    for tiles in drawing_list:
        gameboard.delete(tiles)
    board_list.clear()
    for list_items in [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]:
        board_list.append(list_items)
    available_moves.clear()
    for avail_items in [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]:
        available_moves.append(avail_items)
    difficulty.clear()
    drawing_list.clear()
    for values in range(8):
        board_values[values] = 0

def player_turn(player):
    player_first.grid_forget()
    computer_first.grid_forget()
    gameboard.delete(board_line_centrex1)
    gameboard.delete(board_line_lowerx1)
    gameboard.delete(board_line_upperx1)
    gameboard.delete(board_line_centrex2)
    gameboard.delete(board_line_lowerx2)
    gameboard.delete(board_line_upperx2)

    if player == "P":
        game_text.config(text="Please take your turn.")
    else:
        computer_move()
        

def set_difficulty(diff):
   
    easy.grid_forget()
    difficult.grid_forget()
    impossible.grid_forget()
    player_first.grid(row=2, column=0)
    computer_first.grid(row=2, column=1)
    game_text.config(text="Please choose a difficulty level for computer")
    for numkeys in range (9):
        root.bind((numkeys + 1), place_piece)
    return diff
    
def update_values(move, active_player):
    choice = int(move)
    #default amount to add; 2 for player, 5 for computer
    amount = 0
    print("ACTIVE PLAYER: " + str(active_player))

    if active_player == "P":
        amount = 2
    else:
        amount = 5
    print("AMOUNT: " + str(amount))
    print("MOVE: " + str(move))
    if choice == 1:
        board_values[0] += amount
        board_values[3] += amount
        board_values[6] += amount
    elif choice == 2:
        board_values[0] += amount
        board_values[4] += amount
    elif choice == 3:
        board_values[0] += amount
        board_values[5] += amount
        board_values[7] += amount
    elif choice == 4:
        board_values[1] += amount
        board_values[3] += amount
    elif choice == 5:
        board_values[1] += amount
        board_values[4] += amount
        board_values[6] += amount
        board_values[7] += amount
    elif choice == 6:
        board_values[1] += amount
        board_values[5] += amount
    elif choice == 7:
        board_values[2] += amount
        board_values[3] += amount
        board_values[7] += amount
    elif choice == 8:
        board_values[2] += amount
        board_values[4] += amount
    elif choice == 9:
        board_values[2] += amount
        board_values[5] += amount
        board_values[6] += amount
 
         
def place_piece(event):

    
    if type(event) == tk.Event and "your" in game_text.cget('text'):
        board_row = int((int(event.char) - 1)/3)
        board_col = (int(event.char) - 1) % 3
        if [board_row, board_col] in available_moves:
            available_moves.remove([board_row, board_col])
            print("avail moves: " + str(available_moves))
            print("EVENT CHAR: " + str(event.char))
            #place
            x1 = int(event.char)
            y1 = 0
            #155-245 x1 for 1, 4, 7
            #255-345 x1 for 2, 5, 8
            #355-445 x1 for 3, 6, 9

            #155-245 y1 for 1, 2, 3
            #255-345 y1 for 4, 5, 6
            #355-445 y1 for 7, 8, 9
            #if its 1mod3, x1 is 155-245; 2mod3, x1 is 255-345; 0mod3, x1 is 355-445

            if x1 < 4:
                y1 = 155
                x1 = (x1 *100) + 55
                x2 = x1 + 90
                y2 = 245
            elif 4 <= x1 <= 6:
                y1 = 255
                x1 = ((x1 - 3) * 100) + 55
                x2 = x1 + 90
                y2 = 345
            else:
                y1 = 355
                x1 = ((x1 - 6) * 100) + 55
                x2 = x1 + 90
                y2 = 445
                
            drawing_list.append(gameboard.create_line(x1, y1, x2, y2, width=5, fill="purple"))
            drawing_list.append(gameboard.create_line(x1, y2, x2, y1, width=5, fill="purple"))
            game_text.config(text = "Computer's turn.")
            board_list[board_row][board_col] = "O"
            update_values(event.char, "P")
        

            if 6 in board_values:
                game_text.config(text = "Player wins! \n Play again?")
                play_again()
                
            elif available_moves == []:
                game_text.config(text = "Tie game! \n Play again?")
                play_again()
                
            elif 15 in board_values:
                game_text.config(text = "COMPUTER WINS! \n Play again?")
                play_again()


            else:
                computer_move()
               

        
    elif type(event) == int:
        print("COMP FRIG")
        board_row = int((event - 1)/3)
        board_col = (event - 1) % 3
        #place
        x1 = int(event)
        y1 = 0
        #155-245 x1 for 1, 4, 7
        #255-345 x1 for 2, 5, 8
        #355-445 x1 for 3, 6, 9

        #155-245 y1 for 1, 2, 3
        #255-345 y1 for 4, 5, 6
        #355-445 y1 for 7, 8, 9
        #if its 1mod3, x1 is 155-245; 2mod3, x1 is 255-345; 0mod3, x1 is 355-445

        if x1 < 4:
            y1 = 155
            x1 = (x1 *100) + 55
            x2 = x1 + 90
            y2 = 245
        elif 4 <= x1 <= 6:
            y1 = 255
            x1 = ((x1 - 3) * 100) + 55
            x2 = x1 + 90
            y2 = 345
        else:
            y1 = 355
            x1 = ((x1 - 6) * 100) + 55
            x2 = x1 + 90
            y2 = 445
            
        drawing_list.append(gameboard.create_line(x1, y1, x2, y2, width=5, fill="red"))
        drawing_list.append(gameboard.create_line(x1, y2, x2, y1, width=5, fill="red"))

        
        if 6 in board_values:
            print(text = "Player wins! \n Play again?")
            play_again()
            
        elif available_moves == []:
            game_text.config(text = "Tie game! \n Play again?")
            play_again()
            
        elif 15 in board_values:
            game_text.config(text = "COMPUTER WINS! \n Play again?")
            play_again()


def play_again():
    play_again_yes.grid(row=1, column=2)
    play_again_no.grid(row=1, column=3)
        
canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()


    
game_text = tk.Label(canvas, text = "Welcome to \n Tic Tac Toe \n Please Choose Game Difficulty:")
game_text.grid(row = 0, column = 1)

easypic = tk.PhotoImage(file="easy.png")


 




easy = ttk.Button(canvas, image=easypic, command = lambda: difficulty.append(set_difficulty("E")))
easy.grid(row=2, column=0)

difficult = ttk.Button(canvas, text = "Difficult", command = lambda: difficulty.append(set_difficulty("D")))
difficult.grid(row=2, column=1)

impossible = ttk.Button(canvas, text = "Impossible", command = lambda: difficulty.append(set_difficulty("I")))
impossible.grid(row=2, column=2)

player_first = ttk.Button(canvas, text = "Player", command = lambda: player_turn("P"))


computer_first = ttk.Button(canvas, text = "Computer", command = lambda: player_turn("C"))

play_again_yes = ttk.Button(canvas, text = "Yes", command = lambda: reload_game())
play_again_no = ttk.Button(canvas, text = "No", command = lambda:root.destroy())


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

board_line_y = gameboard.create_line(250, 150, 250, 450, fill = "black", width=5)
board_line_y2 = gameboard.create_line(350, 150, 350, 450, fill = "black", width=5)
board_line_x = gameboard.create_line(150, 250, 450, 250, fill = "black", width=5)
board_line_x2 = gameboard.create_line(150, 350, 450, 350, fill = "black", width=5)


board_line_centrex1 = gameboard.create_line(255, 345, 345, 255, fill = "red", width=5)
board_line_centrex2 = gameboard.create_line(255, 255, 345, 345, fill = "red", width=5)

board_line_lowerx1 = gameboard.create_line(155, 445, 245, 355, fill = "red", width=5)
board_line_lowerx2 = gameboard.create_line(155, 355, 245, 445, fill = "red", width=5)

board_line_upperx1 = gameboard.create_line(355, 155, 445, 245, fill = "red", width=5)
board_line_upperx2 = gameboard.create_line(355, 245, 445, 155, fill = "red", width=5)



#Update board_values to optimize computer moves as well as for checking for winner


def computer_move():
    player_move = "C"
    board_index = 0
    highest_val = 0
    best_move = 0
    
    if "I" in difficulty or "D" in difficulty:
            if max(board_values) == 2 and [1, 1] not in available_moves and "I" in difficulty:
                best_move = 0
            
            else:
                for vals in board_values:
                    if vals == 10:
                        highest_val = 14
                        best_move = board_index
                    elif vals == 4 and highest_val != 14:
                        highest_val = 13
                        best_move = board_index
                    elif vals > highest_val and vals not in (7, 9, 12):
                        highest_val = vals
                        best_move = board_index
                    board_index += 1
    print("BEST MOVE: " + str(best_move))
  #  return best_move
    
#def computer_move2(diff, comp_strat, boardvals):
#if "C" in difficulty:
 #   display_board(board_list)
    
    if "I" in difficulty or "D" in difficulty:
        #insert an "X" into the center of the board if it's empty
        if board_list[1][1] == "5":
            board_list[1][1] = "X"
            available_moves.remove([1, 1])
            update_values(5, "C")
            best_move = 5
            
        else:
            #insert an "X" into a row if it's the best move
            if best_move == 0:
                for number in range(0, 3):
                    if [0, number] in available_moves and player_move == "C":
                        board_list[0][number] = "X"
                        available_moves.remove([0, number])
                        best_move = (number + 1)
                        update_values(best_move, "C")
                        player_move = "P"
                        
            elif best_move == 1:
                for number in range(0, 3):
                    if [1, number] in available_moves and player_move == "C":
                        board_list[1][number] = "X"
                        available_moves.remove([1, number])
                        best_move = (3 + (number + 1))
                        update_values(best_move, "C")
                        player_move = "P"
                                 
            elif best_move == 2:
                for number in range(0, 3):
                    if [2, number] in available_moves and player_move == "C":
                        board_list[2][number] = "X"
                        available_moves.remove([2, number])
                        best_move = (6 + (number + 1))
                        update_values(best_move, "C")
                        player_move = "P"
                                  
            #insert an "X" into a column if it's the best move
            elif best_move == 3:
                for number in range(0, 3):
                    if [number, 0] in available_moves and player_move == "C":
                        board_list[number][0] = "X"
                        available_moves.remove([number, 0])
                        best_move = (number*3) + 1
                        update_values(best_move, "C")
                        player_move = "P"
                                  
            elif best_move == 4:
                for number in range(0, 3):
                    if [number, 1] in available_moves and player_move == "C":
                        board_list[number][1] = "X"
                        available_moves.remove([number, 1])
                        best_move = (number * 3) + 2
                        update_values(best_move, "C")
                        player_move = "P"
                                  
            elif best_move == 5:
                for number in range(0, 3):
                    if [number, 2] in available_moves and player_move == "C":
                        board_list[number][2] = "X"
                        available_moves.remove([number, 2])
                        best_move = (number*3) + 3
                        update_values(best_move, "C")
                        player_move = "P"
                                 
            #insert an "X" into the top-left to bottom-right diagonal if it's the best move                       
            elif best_move == 6:
                for number in range(3):
                    if [number, number] in available_moves and player_move == "C":
                        board_list[number][number] = "X"
                        available_moves.remove([number, number])
                        best_move = (number + 1) + (number * 3)
                        update_values(best_move, "C")
                        player_move = "P"
                                  
            else:
                for number in range(3):
                    if [number, (2 - number)] in available_moves and player_move == "C":
                        print([number, (2 - number)])
                        board_list[number][2 - number] = "X"
                        available_moves.remove([number, (2 - number)])
                        best_move = (number * 2) + 3
                        update_values(best_move, "C")
                        player_move = "P"
                                 
    else:
        new_move = random.choice(available_moves)
        available_moves.remove(new_move)
        board_list[new_move[0]][new_move[1]] = "X"
        best_move = (new_move[0]*3) + (new_move[1] + 1)
        update_values(best_move, "C")
        
    place_piece(best_move)
    if available_moves != []:
        game_text.config(text="Please take your turn.")

    if 6 in board_values:
        print(text = "Player wins! \n Play again?")
        play_again()
    elif available_moves == []:
        game_text.config(text = "Tie game! Play again?")
        play_again()
    elif 15 in board_values:
        game_text.config(text = "COMPUTER WINS YOU LOSE NOOB \n Play again?")
        play_again()
    
    return
    

root.mainloop()
