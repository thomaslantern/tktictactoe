# TK-TIC-TAC-TOE:
# A one-player game of tic-tac-toe, using tkinter
#
# Copyright (c) 2020 Thomas Wesley Scott
# Author: Thomas Wesley Scott


import random
import tkinter as tk
from tkinter import ttk


board_list = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
move_avail = [[0, 0], [0, 1], [0, 2],
                   [1, 0], [1, 1], [1, 2],
                   [2, 0], [2, 1], [2, 2]]
turn = ""
player_move = ""
difficulty = []
drawing_list = []

# Set value for rows, columns, and diagonals for computer moves
board_vals = [0, 0, 0, 0, 0, 0, 0, 0]


# Update screen for choosing difficulty
def reload_game():
    player_first.grid_forget()
    computer_first.grid_forget()
    play_again_yes.grid_forget()
    play_again_no.grid_forget()
    easy.config(image=easypic)
    easy.grid(row = 2, column = 0)
    difficult.config(image=diffpic)
    difficult.grid(row = 3, column = 0)
    impossible.config(image=impopic, state = "active", bd = 2)
    
    game_text.config(image=difflvl)

    for tiles in drawing_list:
        board.delete(tiles)
    board_list.clear()
    for list_items in [["1", "2", "3"],
                       ["4", "5", "6"],
                       ["7", "8", "9"]]:
        board_list.append(list_items)
    move_avail.clear()
    for avail_items in [[0, 0], [0, 1], [0, 2],
                        [1, 0], [1, 1], [1, 2],
                        [2, 0], [2, 1], [2, 2]]:
        move_avail.append(avail_items)
    difficulty.clear()
    drawing_list.clear()
    for values in range(8):
        board_vals[values] = 0


# Cleans up screen/board for new game
def start_game(player):    
    player_first.config(image=blankpic, state = "disabled", bd=0)
    computer_first.config(image=blankpic, state = "disabled", bd=0)
    game_text.configure(image=gdlk)
    board.delete(board_x3)
    board.delete(board_x4)
    board.delete(board_x5)
    board.delete(board_x6)
    board.delete(board_x7)
    board.delete(board_x8)

    if player == "P":
        game_text.config(text="Please take your turn.")
    else:
        computer_move()


# Hide difficulty settings, show settings to choose who goes first
def set_difficulty(diff):
    easy.grid_forget()
    difficult.grid_forget()
    impossible.configure(image=blankpic, state="disabled", bd = 0)
    player_first.config(image=playpic, state="active", bd = 2)
    computer_first.config(image=compic, state="active", bd = 2)
    player_first.grid(row=2, column=0)
    computer_first.grid(row=3, column=0)
    game_text.config(image=gofirst)

    # Create bindings for number keys and mouse clicks for input    
    for numkeys in range (9):
        root.bind((numkeys + 1), place_piece)

    root.bind("<Button-1>", place_piece)
    

    return diff


def update_values(move, active_player):
    choice = int(move)
    
   
    if active_player == "P":
        amount = 2
    else:
        amount = 5

    if choice == 1:
        board_vals[0] += amount
        board_vals[3] += amount
        board_vals[6] += amount
    elif choice == 2:
        board_vals[0] += amount
        board_vals[4] += amount
    elif choice == 3:
        board_vals[0] += amount
        board_vals[5] += amount
        board_vals[7] += amount
    elif choice == 4:
        board_vals[1] += amount
        board_vals[3] += amount
    elif choice == 5:
        board_vals[1] += amount
        board_vals[4] += amount
        board_vals[6] += amount
        board_vals[7] += amount
    elif choice == 6:
        board_vals[1] += amount
        board_vals[5] += amount
    elif choice == 7:
        board_vals[2] += amount
        board_vals[3] += amount
        board_vals[7] += amount
    elif choice == 8:
        board_vals[2] += amount
        board_vals[4] += amount
    elif choice == 9:
        board_vals[2] += amount
        board_vals[5] += amount
        board_vals[6] += amount
 
         
def place_piece(event):
        
    if type(event) == tk.Event and "your" in game_text.cget('text'):
        
        if str(event.type) == 'KeyPress':
            board_row = int((int(event.char) - 1)/3)
            board_col = (int(event.char) - 1) % 3
            move_choice = int(event.char)
        elif str(event.type) == 'ButtonPress':
            board_col = int((event.x - 50)/100)
            board_row = int((event.y - 30)/100)
            move_choice = (board_row * 3) + (board_col + 1)
        if [board_row, board_col] in move_avail:
            move_avail.remove([board_row, board_col])

                     
            if move_choice < 4:
                y1 = 25
                x1 = (move_choice *100) - 45
                x2 = x1 + 90
                y2 = 115
            elif 4 <= move_choice <= 6:
                y1 = 125
                x1 = ((move_choice - 3) * 100) - 45
                x2 = x1 + 90
                y2 = 215
            else:
                y1 = 225
                x1 = ((move_choice - 6) * 100) - 45
                x2 = x1 + 90
                y2 = 315
                
            drawing_list.append(board.create_line(x1, y1,
                                                  x2, y2,
                                                  width=5,
                                                  fill="blue"))
            drawing_list.append(board.create_line(x1, y2,
                                                  x2, y1,
                                                  width=5,
                                                  fill="blue"))
            game_text.config(text = "Computer's turn.")
            board_list[board_row][board_col] = "X"
            update_values(move_choice, "P")
        

            if 6 in board_vals:
                game_text.config(image=winpic)
                play_again()
                
            elif move_avail == []:
                game_text.config(image=tiepic)
                play_again()
                
            elif 15 in board_vals:
                game_text.config(image=losepic)
                play_again()


            else:
                computer_move()
               

        
    elif type(event) == int:
        board_row = int((event - 1)/3)
        board_col = (event - 1) % 3
        x1 = int(event)
        y1 = 0
        
        if x1 < 4:
            y1 = 25
            x1 = (x1 * 100) - 45
            x2 = x1 + 90
            y2 = 115
        elif 4 <= x1 <= 6:
            y1 = 125
            x1 = ((x1 - 3) * 100) - 45
            x2 = x1 + 90
            y2 = 215
        else:
            y1 = 225
            x1 = ((x1 - 6) * 100) - 45
            x2 = x1 + 90
            y2 = 315

        drawing_list.append(board.create_circle(x1 + 45,
                                                y1 + 45,
                                                40, width=5,
                                                outline="red")) 
        
        
        if 6 in board_vals:
            game_text.config(image=winpic)
            play_again()            
        elif 15 in board_vals:
            game_text.config(image=losepic)
            play_again()
        elif move_avail == []:
            game_text.config(image=tiepic)
            play_again()

    

def play_again():
    play_again_yes.grid(row=2, column=0)
    play_again_yes.config(bd=4)
    play_again_no.grid(row=3, column=0)
    play_again_no.config(bd=3)
    game_text.config(text="Play again?")


def computer_move():
    player_move = "C"
    board_index = 0
    highest_val = 0
    best_move = 0
    
    if "I" in difficulty or "D" in difficulty:           
        no_mid = ((max(board_vals) == 2) and ([1, 1] not in move_avail))
        if no_mid and "I" in difficulty:
            best_move = 0
        
        else:
            for vals in board_vals:
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

            # Only one spot left on board that doesn't either
            # win or prevent a win
            if best_move == 0 and min(board_vals) == 7:
                best_move = move_avail[0][0]
                                
            
    
        # Insert an "O" into the center of the board if it's empty
        if board_list[1][1] == "5":
            board_list[1][1] = "X"
            move_avail.remove([1, 1])
            update_values(5, "C")
            best_move = 5
            
        else:
            # Insert an "O" into a row if it's the best move
            if best_move == 0:
                for number in range(0, 3):
                    if [0, number] in move_avail and player_move == "C":
                        board_list[0][number] = "O"
                        move_avail.remove([0, number])
                        best_move = (number + 1)
                        update_values(best_move, "C")
                        player_move = "P"
                        
            elif best_move == 1:
                for number in range(0, 3):
                    if [1, number] in move_avail and player_move == "C":
                        board_list[1][number] = "O"
                        move_avail.remove([1, number])
                        best_move = (3 + (number + 1))
                        update_values(best_move, "C")
                        player_move = "P"
                                 
            elif best_move == 2:
                for number in range(0, 3):
                    if [2, number] in move_avail and player_move == "C":
                        board_list[2][number] = "O"
                        move_avail.remove([2, number])
                        best_move = (6 + (number + 1))
                        update_values(best_move, "C")
                        player_move = "P"
                                  
            # Insert an "O" into a column if it's the best move
            elif best_move == 3:
                for number in range(0, 3):
                    if [number, 0] in move_avail and player_move == "C":
                        board_list[number][0] = "X"
                        move_avail.remove([number, 0])
                        best_move = (number*3) + 1
                        update_values(best_move, "C")
                        player_move = "P"
                                  
            elif best_move == 4:
                for number in range(0, 3):
                    if [number, 1] in move_avail and player_move == "C":
                        board_list[number][1] = "O"
                        move_avail.remove([number, 1])
                        best_move = (number * 3) + 2
                        update_values(best_move, "C")
                        player_move = "P"
                                  
            elif best_move == 5:
                for number in range(0, 3):
                    if [number, 2] in move_avail and player_move == "C":
                        board_list[number][2] = "O"
                        move_avail.remove([number, 2])
                        best_move = (number*3) + 3
                        update_values(best_move, "C")
                        player_move = "P"
                                 
            # Insert an "O" into the top-left to bottom-right diagonal
            # if it's the best move                       
            elif best_move == 6:
                for number in range(3):
                    if [number, number] in move_avail and player_move == "C":
                        board_list[number][number] = "O"
                        move_avail.remove([number, number])
                        best_move = (number + 1) + (number * 3)
                        update_values(best_move, "C")
                        player_move = "P"
            #   Bottom-left to top-right diagonal             
            else:
                for number in range(3):
                    if [number, (2 - number)] in move_avail and player_move == "C":
                        board_list[number][2 - number] = "O"
                        move_avail.remove([number, (2 - number)])
                        best_move = (number * 2) + 3
                        update_values(best_move, "C")
                        player_move = "P"
                                 
    else:
        new_move = random.choice(move_avail)
        move_avail.remove(new_move)
        board_list[new_move[0]][new_move[1]] = "O"
        best_move = (new_move[0]*3) + (new_move[1] + 1)
        update_values(best_move, "C")
        
    place_piece(best_move)
    if move_avail != []:
        game_text.config(text="Please take your turn.")

    if 6 in board_vals:
        game_text.config(image=winpic)
        play_again()
    elif 15 in board_vals:
        game_text.config(image=losepic)
        play_again()
    elif move_avail == []:
        game_text.config(image=tiepic)
        play_again()
    
    
    return


root = tk.Tk()
root.title("Tic Tac Toe")



# Method for drawing circles on tkinter canvas
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

        
canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()


# Loading images for game
difflvl = tk.PhotoImage(file="images\difficultylvl.png")
gofirst = tk.PhotoImage(file="images\goesfirst.png")
    
game_text = tk.Label(canvas, image=difflvl)
game_text.grid(row = 1, column = 0)

easypic = tk.PhotoImage(file="images/easy.png")
diffpic = tk.PhotoImage(file="images/difficult.png")
impopic = tk.PhotoImage(file="images/impossible.png")

playpic = tk.PhotoImage(file="images/player.png")
compic = tk.PhotoImage(file="images/computer.png")
winpic = tk.PhotoImage(file="images/winner.png")
losepic = tk.PhotoImage(file="images/loser.png")
tiepic = tk.PhotoImage(file="images/tie.png")
yespic = tk.PhotoImage(file="images/yes.png")
nopic = tk.PhotoImage(file="images/no.png")
gdlk = tk.PhotoImage(file="images/gdluck.png")

blankpic = tk.PhotoImage(file="images/blankimp.png")

# Buttons for choosing difficulty
easy = tk.Button(canvas, image=easypic, command =
                 lambda: difficulty.append(set_difficulty("E")))
easy.grid(row=2, column=0)

difficult = tk.Button(canvas, image=diffpic, command =
                      lambda: difficulty.append(set_difficulty("D")))
difficult.grid(row=3, column=0)

impossible = tk.Button(canvas, image=impopic, command =
                       lambda: difficulty.append(set_difficulty("I")))
impossible.grid(row=4, column=0)


# Buttons for choosing who plays first
player_first = tk.Button(canvas, image = playpic, text = "Player",
                         command = lambda: start_game("P"))
computer_first = tk.Button(canvas, image=compic, text = "Computer",
                           command = lambda: start_game("C"))


# Buttons for asking player whether to play again
play_again_yes = tk.Button(canvas, image = yespic, text = "Yes",
                           command = lambda: reload_game())
play_again_no = tk.Button(canvas, image = nopic, text = "No",
                          command = lambda:root.destroy())


# Draw the board
board = tk.Canvas(canvas, width = 400, height = 600)
board.grid(row=5, column=0)

gametitle = tk.PhotoImage(file="images/title.png")
game_title = tk.Label(canvas, image = gametitle)
game_title.grid(row=0, column=0)

# Drawing on title screen
board_y = board.create_line(150, 20, 150, 320, fill = "black", width=5)
board_y2 = board.create_line(250, 20, 250, 320, fill = "black", width=5)
board_x = board.create_line(50, 120, 350, 120, fill = "black", width=5)
board_x2 = board.create_line(50, 220, 350, 220, fill = "black", width=5)
board_x3 = board.create_line(155, 215, 245, 125, fill = "red", width=5)
board_x4 = board.create_line(155, 125, 245, 215, fill = "red", width=5)
board_x5 = board.create_line(55, 315, 145, 225, fill = "red", width=5)
board_x6 = board.create_line(55, 225, 145, 315, fill = "red", width=5)
board_x7 = board.create_line(255, 25, 345, 115, fill = "red", width=5)
board_x8 = board.create_line(255, 115, 345, 25, fill = "red", width=5)

root.mainloop()
