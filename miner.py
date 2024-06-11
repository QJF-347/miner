from tkinter import *
import random
import time


def random_mine():
    mines = []
    for mine in range(MINES):
        a, b = random.randint(0, (ROWS - 1)), random.randint(0, (COLUMNS - 1))
        mines.append(a)
        mines.append(b)

    return mines


def is_safe(u, i):
    buttons[u][i].config(bg="green", state="disabled")
    global SCORE
    SCORE += 1
    score_label.config(text="score : {}".format(SCORE))


def new_game():
    global SCORE
    SCORE = 0
    score_label.config(text="score : {}".format(SCORE))
    for rowe in range(ROWS):
        for column in range(COLUMNS):
            buttons[rowe][column] = Button(button_frame, width=13, height=6,
                                          command=lambda s=rowe, l=column: is_safe(s, l))
            buttons[rowe][column].grid(row=rowe, column=column)
    d = 0
    mine_list = random_mine()
    for mines in range(MINES):
        x, y = mine_list[d], mine_list[(d + 1)]
        d += 2
        buttons[x][y].config(command=lambda r=x, m=y: is_mine(r, m))
        window.update()


def is_mine(c, d):
    buttons[c][d].config(bg="red", text="MINE", fg="black", font=("Aerial", 9, "bold"))
    for this in range(ROWS):
        for that in range(COLUMNS):
            buttons[this][that].config(state="disabled")



def mine_count(value):
    global MINES
    if MINES == 1 and value == -1:
        pass
    elif MINES == (COLUMNS * ROWS - 1) and value == 1:
        pass
    else:
        MINES += value
        mines_label.config(text="mines : {}".format(MINES))


SCORE = 0
ROWS = 5
COLUMNS = 5
MINES = 7

window = Tk()
window.config(bg="black")
frame = Frame(window, background="black")
frame.pack()
up_frame = Frame(frame, bg="black")

score_label = Label(up_frame, text="score : {}".format(SCORE), font=("Aerial", 23), bg='black', width=10, fg="#00ff00")
score_label.grid(row=0, column=0)

mine_frame = Frame(up_frame, bg="black")
mine_frame.grid(row=0, column=1)

up_frame.pack()

button_less = Button(mine_frame, text="_", font=("Aerial", 20, "bold"), padx=10,
                     command=lambda: mine_count(-1))
button_less.grid(row=0, column=0)

mines_label = Label(mine_frame, text="mines : {}".format(MINES), font=("Aerial", 20, "bold"), height=1, bg="black",
                    fg="#00ff00")
mines_label.grid(row=0, column=1)

button_more = Button(mine_frame, text="+", font=("Aerial", 20, "bold"), padx=10,
                     command=lambda: mine_count(1))
button_more.grid(row=0, column=2)

restart_button = Button(mine_frame, text="RESTART", font=("Aerial", 20, "bold"), padx=10,
                        command=new_game)
restart_button.grid(row=ROWS + 1, column=0)

button_frame = Frame(frame)
button_frame.pack()

mine_list = random_mine()
buttons = [xx := [0 for x in range(COLUMNS)] for rows in range(ROWS)]
for row in range(ROWS):
    for column in range(COLUMNS):
        buttons[row][column] = Button(button_frame, width=13, height=6,
                                      command=lambda s=row, l=column: is_safe(s, l))
        buttons[row][column].grid(row=row, column=column)
d = 0
for mines in range(MINES):
    x, y = mine_list[d], mine_list[(d + 1)]
    d += 2
    buttons[x][y].config(command=lambda r=x, m=y: is_mine(r, m))
    window.update()

window.mainloop()
