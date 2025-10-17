import tkinter as tk
from tkinter import messagebox

def check_winner():
    for c in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[c[0]]["text"] == buttons[c[1]]["text"] ==  buttons[c[2]]["text"] !="":
            buttons[c[0]].config(bg="green")
            buttons[c[1]].config(bg="green")
            buttons[c[2]].config(bg="green")

            messagebox.showinfo("Tic Tac Toe",f"Player {buttons[c[1]]["text"]} Win's THE GAME!!!")
            root.quit()

def button_check(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        toggle_player()

def toggle_player():
    global current_player
    current_player = "X"  if current_player == "O" else "O"
    label.config(text = f"PLAYER {current_player} 's ")

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [tk.Button(root, text="", font=("normal",25),width=6,height=2, command = lambda i=i: button_check(i)) for i in range(9)]

for i,button in enumerate(buttons):
    button.grid(row=i//3 , column=i%3)

current_player = "X"
winner =  False
label=tk.Label(root , text = f"PLAYER {current_player} 's turn's",font=("normal",20)) 
label.grid(row=3,column=0,columnspan=3)

root.mainloop()