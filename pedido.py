from tkinter import *
import random

root = Tk()
root.title("Quer namorar comigo?")
root.geometry("600x300")
root.resizable(False, False)
root.configure(bg = "#FFA8C2")

def move_button(event):
    x = random.randint(50, 350) 
    y = random.randint(50, 150)

    
    if (x < sim_button.winfo_x() - 50 or x > sim_button.winfo_x() + 50) or (y < sim_button.winfo_y() - 50 or y > sim_button.winfo_y() + 50):
        nao_button.place(x = x, y = y) 

def show_response(response):
    if response == "sim":
        label_response.config(text = "Você disse SIM :D", fg = "#00A6FF")
    elif response == "nao":
        label_response.config(text = "Você disse NÃO :(", fg = "#ED806D")

sim_button = Button(root, text = "SIM", width = 10, command = lambda:show_response("sim"))
nao_button = Button(root, text = "NÃO", width = 10, command = lambda:show_response("nao"))

sim_button.configure(bg = "#00A6FF", fg = "#FFFFFF", font = ('Helvetica', 12))
nao_button.configure(bg = "#ED806D", fg = '#FFFFFF', font = ('Helvetica', 12))

label_question = Label(root, text = "Quer namorar comigo?", font = ('Helvetica', 14), bg = ("#FFA8C2"))
label_response = Label(root, text = "", font = ('Helvetica', 14), bg = ("#F0F0F0"))

sim_button.place(x = 100, y = 75)
nao_button.place(x = 250, y = 75)
label_question.place(x = 50, y = 20)
label_question.place(x = 120, y = 130)

nao_button.bind("<Motion>", move_button)


root.mainloop()