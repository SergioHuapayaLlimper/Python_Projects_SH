import tkinter as tk
from tkinter import messagebox

#Sergio Rodrigo Huapaya Llimper

#Variables del juego
player = 'X'
game_over = False

#Función para verificar si hay un ganador
def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return True
    return False

#Función clicadora
def button_click(row, col):
    global player, game_over
    if buttons[row][col]['text'] == '' and not game_over:
        buttons[row][col]['text'] = player
        buttons[row][col]['bg'] = '#37474F' if player == 'X' else '#455A64'
        if check_winner():
            messagebox.showinfo('Tic Tac Toe', f'Jugador {player} gana!')
            game_over = True
        elif all(buttons[row][col]['text'] != '' for row in range(3) for col in range(3)):
            messagebox.showinfo('Tic Tac Toe','¡Es un empate!')
        else:
            player = 'O' if player == 'X' else 'X'

#Función para reiniciar el juego
def reset_game():
    global player, game_over
    player = 'X'
    game_over = False
    for row in range(3):
        for col in range(3):
            buttons[row][col]['text'] = ''
            buttons[row][col]['bg'] = '#263238'

root = tk.Tk()
root.title('Tic Tac Toe')
root.geometry('400x450')
root.configure(bg='#263238')

frame = tk.Frame(root, bg='#263238')
frame.place(relx=0.5, rely=0.5, anchor='center')

buttons = [[tk.Button(frame, text='', font='normal 20 bold', width=5, height=2, bg='#263238', fg='white',
            command=lambda row=row, col=col: button_click(row, col)) for col in range(3)] for row in range(3)]

for row in range(3):
    for col in range(3):
        buttons[row][col].grid(row=row, column=col, padx=5, pady=5)

reset_button = tk.Button(root, text='Reiniciar Juego', font='normal 15 bold', command=reset_game, bg='#546E7A', fg='white')
reset_button.place(relx=0.5, rely=0.9, anchor='center')

root.mainloop()

