from tkinter import *
import random
import customtkinter

root = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
root.title('XOX')
game_run = True
field = []
cross_count = 0
zero_count = 0
cross_wins = 0
zero_wins = 0
root. resizable(False, False)
root.wm_iconbitmap("s1.ico")

# Темная тема
root.configure(bg='#13181a')

def new_game():
    global game_run, cross_count, zero_count, cross_wins, zero_wins
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = '#13181a'
    game_run = True
    cross_count = 0
    zero_count = 0
    update_counters()

def click(row, col):
    global cross_count, zero_count
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            computer_move()
            check_win('O')

def check_win(smb):
    global game_run, cross_wins, zero_wins
    for n in range(3):
        if check_line(field[n][0], field[n][1], field[n][2], smb):
            game_run = False
            break
        if check_line(field[0][n], field[1][n], field[2][n], smb):
            game_run = False
            break
    if check_line(field[0][0], field[1][1], field[2][2], smb):
        game_run = False
    if check_line(field[2][0], field[1][1], field[0][2], smb):
        game_run = False

    if not game_run:
        if smb == 'X':
            cross_wins += 1
        elif smb == 'O':
            zero_wins += 1
        update_counters()

def check_line(a1, a2, a3, smb):
    global game_run, cross_count, zero_count
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'green'
        game_run = False
        if smb == 'X':
            cross_count += 1
        elif smb == 'O':
            zero_count += 1
        update_counters()

def can_win(a1, a2, a3, smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res

def computer_move():
    global cross_count, zero_count
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            zero_count += 1
            update_counters()
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            zero_count += 1
            update_counters()
            return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            zero_count += 1
            update_counters()
            break

for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ',width=4, height=2,
                        font=('Verdana', 30, 'bold'),
                        background='#13181a', foreground='white',
                        command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)

new_button =  customtkinter.CTkButton(master=root, text='new game', command=new_game)
new_button.grid(row=3, column=1,columnspan=3, sticky="ew")
#new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

cross_label = Label(root, text="Крестики: 0", font=('Verdana', 12), background='#1f2324', foreground='white')
cross_label.grid(row=4, column=0, columnspan=3, sticky='nsew')

zero_label = Label(root, text="Нолики: 0", font=('Verdana', 12), background='#1f2324', foreground='white')
zero_label.grid(row=5, column=0, columnspan=3, sticky='nsew')


def update_counters():
    cross_label.config(text="Крестики: " + str(cross_wins))
    zero_label.config(text="Нолики: " + str(zero_wins))

update_counters()

root.mainloop()
