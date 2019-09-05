import tkinter as tk
from tkinter import messagebox

def callback(r, c):
    global player
    if player == 'X' and states[r][c] == 0 and stop_game==False:
        b[r][c].configure(text='X', fg='blue', bg='white')
        states[r][c] = 'X'
        player = 'O'
    if player == 'O' and states[r][c] == 0 and stop_game==False:
        b[r][c].configure(text='O', fg='orange', bg='black')
        states[r][c] = 'O'
        player = 'X'




root = tk.Tk()
root.title('TIC_TAC_TOE')
b = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

states = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(3):
    for j in range(3):
        b[i][j] = tk.Button(font=('Arial', 60), width=4, bg='powder blue',
                            command=lambda r=i, c=j: callback(r, c))
        b[i][j].grid(row=i, column=j)

player = 'X'
stop_game = False
root.mainloop()