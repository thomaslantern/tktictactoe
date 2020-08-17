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


def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)

tk.Canvas.create_circle = _create_circle

def reload_game():
    easy.grid(row=2, column=0)
    difficult.grid(row=3, column=0)
    impossible.grid(row=4, column=0)
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
    player_first.config(image=blankpic, state = "disabled")
    computer_first.config(image=blankpic, state = "disabled")
  
    
    
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


'''root.columnconfigure(2, weight=1)
l1.grid(row=1, column=1, columnspan=2, sticky="ew")
l2.grid(row=1, column=3, sticky="ew")
l3.grid(row=2, column=1, sticky="ew")
l4.grid(row=2, column=3, sticky="ew")'''


def set_difficulty(diff):
   
    easy.grid_forget()
    difficult.grid_forget()
    impossible.configure(image=blankpic, state="disabled", bd=0)
    player_first.grid(row=2, column=0)
    computer_first.grid(row=3, column=0)
    game_text.config(image=gofirst)
    
    for numkeys in range (9):
        root.bind((numkeys + 1), place_piece)
    return diff
    
def update_values(move, active_player):
    choice = int(move)
    #default amount to add; 2 for player, 5 for computer
    amount = 0
    

    if active_player == "P":
        amount = 2
    else:
        amount = 5

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
                y1 = 25
                x1 = (x1 *100) - 45
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
                y2 = 345
                
            drawing_list.append(gameboard.create_line(x1, y1, x2, y2, width=5, fill="blue"))
            drawing_list.append(gameboard.create_line(x1, y2, x2, y1, width=5, fill="blue"))
            game_text.config(text = "Computer's turn.")
            board_list[board_row][board_col] = "O"
            update_values(event.char, "P")
        

            if 6 in board_values:
                game_text.config(image=winpic)
                play_again()
                
            elif available_moves == []:
                game_text.config(text = "Tie game! \n Play again?")
                play_again()
                
            elif 15 in board_values:
                game_text.config(image=losepic)
                play_again()


            else:
                computer_move()
               

        
    elif type(event) == int:
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

        drawing_list.append(gameboard.create_circle(x1 + 45, y1 + 45, 40, width=5, outline="red"))   
        #drawing_list.append(gameboard.create_line(x1, y1, x2, y2, width=5, fill="red"))
        #drawing_list.append(gameboard.create_line(x1, y2, x2, y1, width=5, fill="red"))

        
        if 6 in board_values:
            game_text.config(image=winpic)
            play_again()
            
        elif available_moves == []:
            game_text.config(text = "Tie game! \n Play again?")
            play_again()
            
        elif 15 in board_values:
            game_text.config(image=losepic)
            play_again()


def play_again():
    play_again_yes.grid(row=2, column=0)
    play_again_no.grid(row=3, column=0)
    
        
canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()
canvas.grid_rowconfigure(0, weight = 0)
canvas.grid_rowconfigure(1, weight = 0)
canvas.grid_rowconfigure(2, weight = 0)
canvas.grid_rowconfigure(3, weight = 0)
canvas.grid_rowconfigure(4, weight = 0)



difflvl = tk.PhotoImage(file="difficultylvl.png")
gofirst = tk.PhotoImage(file="goesfirst.png")
    
game_text = tk.Label(canvas, image=difflvl)
game_text.grid(row = 1, column = 0)

easypic = tk.PhotoImage(file="easy.png")
diffpic = tk.PhotoImage(file="difficult.png")
impopic = tk.PhotoImage(file="impossible.png")

playpic = tk.PhotoImage(file="player.png")
compic = tk.PhotoImage(file="computer.png")
winpic = tk.PhotoImage(file="winner.png")
losepic = tk.PhotoImage(file="loser.png")
yespic = tk.PhotoImage(file="yes.png")
nopic = tk.PhotoImage(file="no.png")

blankpic = tk.PhotoImage(file="blankimp.png")

easy = ttk.Button(canvas, image=easypic, command = lambda: difficulty.append(set_difficulty("E")))
easy.grid(row=2, column=0)

difficult = ttk.Button(canvas, image=diffpic, command = lambda: difficulty.append(set_difficulty("D")))
difficult.grid(row=3, column=0)

impossible = tk.Button(canvas, image=impopic, command = lambda: difficulty.append(set_difficulty("I")))
impossible.grid(row=4, column=0)

player_first = ttk.Button(canvas, image = playpic, text = "Player", command = lambda: player_turn("P"))


computer_first = ttk.Button(canvas, image=compic, text = "Computer", command = lambda: player_turn("C"))

play_again_yes = ttk.Button(canvas, image = yespic, text = "Yes", command = lambda: reload_game())
play_again_no = ttk.Button(canvas, image = nopic, text = "No", command = lambda:root.destroy())


gameboard = tk.Canvas(canvas, width = 400, height = 600)
gameboard.grid(row=5, column=0)

gametitle = tk.PhotoImage(file="title.png")
game_title = tk.Label(canvas, image = gametitle)
game_title.grid(row=0, column=0)


board_line_y = gameboard.create_line(150, 20, 150, 320, fill = "black", width=5)
board_line_y2 = gameboard.create_line(250, 20, 250, 320, fill = "black", width=5)
board_line_x = gameboard.create_line(50, 120, 350, 120, fill = "black", width=5)
board_line_x2 = gameboard.create_line(50, 220, 350, 220, fill = "black", width=5)


board_line_centrex1 = gameboard.create_line(155, 215, 245, 125, fill = "red", width=5)
board_line_centrex2 = gameboard.create_line(155, 125, 245, 215, fill = "red", width=5)

board_line_lowerx1 = gameboard.create_line(55, 315, 145, 225, fill = "red", width=5)
board_line_lowerx2 = gameboard.create_line(55, 225, 145, 315, fill = "red", width=5)

board_line_upperx1 = gameboard.create_line(255, 25, 345, 115, fill = "red", width=5)
board_line_upperx2 = gameboard.create_line(255, 115, 345, 25, fill = "red", width=5)



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
        game_text.config(image=winpic)
        play_again()
    elif available_moves == []:
        game_text.config(text = "Tie game! Play again?")
        play_again()
    elif 15 in board_values:
        game_text.config(image=losepic)
        play_again()
    
    return
    

root.mainloop()
