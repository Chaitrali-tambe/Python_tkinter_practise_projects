from tkinter import *
from tkinter import messagebox

from arrow import get

root = Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")
root.config(bg="#E76161")

frame1 = Frame(root)
frame1 = Frame(bg="purple")
frame1.pack()

#title part
titlelabel = Label(frame1, text="Tic Tac Toe", font=("Fixedsys", 50), bg="#E76161", fg="#2D033B")
titlelabel.pack()

frame2 = Frame(root)
frame2.pack()

turn = "x"
count = 0

def disableButtons():
    button1.config(state = DISABLED)
    button2.config(state = DISABLED)
    button3.config(state = DISABLED)
    button4.config(state = DISABLED)
    button5.config(state = DISABLED)
    button6.config(state = DISABLED)
    button7.config(state = DISABLED)
    button8.config(state = DISABLED)
    button9.config(state = DISABLED)


#Check to see if someone win
def checkWin():
    global winner
    winner = False

    #first row
    if button1["text"] == button2["text"] == button3["text"] == "X":
        button1.config(bg="red")
        button2.config(bg="red")
        button3.config(bg="red")

        winner = True

        messagebox.showinfo("Tic tac toe", "X Won")
        disableButtons()

    if button1["text"] == button2["text"] == button3["text"] == "O":
        button1.config(bg="red")
        button2.config(bg="red")
        button3.config(bg="red")

        winner = True

        messagebox.showinfo("Tic tac toe", "O Won")
        disableButtons()

    #second row
    if button4["text"] == button5["text"] == button6["text"] == "X":
        button4.config(bg="red")
        button5.config(bg="red")
        button6.config(bg="red")

        winner = True

        messagebox.showinfo("Tic tac toe", "X Won")
        disableButtons()

    if button4["text"] == button5["text"] == button6["text"] == "O":
        button4.config(bg="red")
        button5.config(bg="red")
        button6.config(bg="red")

        winner = True

        messagebox.showinfo("Tic tac toe", "O Won")
        disableButtons()

    #third row
    if button7["text"] == button8["text"] == button9["text"] == "X":
        button7.config(bg="red")
        button8.config(bg="red")
        button9.config(bg="red")

        winner = True

        messagebox.showinfo("Tic tac toe", "X Won")
        disableButtons()

    if button7["text"] == button8["text"] == button9["text"] == "O":
        button7.config(bg="red")
        button8.config(bg="red")
        button9.config(bg="red")

        winner = True

        messagebox.showinfo("Tic tac toe", "O Won")
        disableButtons()

    #first Column
    if button1["text"] == button4["text"] == button7["text"] == "X":
        button1.config(bg="red")
        button4.config(bg="red")
        button7.config(bg="red")

        winner = True

        messagebox.showinfo("Tic tac toe", "X Won")
        disableButtons()

    if button1["text"] == button4["text"] == button7["text"] == "O":
        button1.config(bg="red")
        button4.config(bg="red")
        button7.config(bg="red")

        winner = True

        messagebox.showinfo("Tic tac toe", "O Won")
        disableButtons()

    #2nd column
    if button2["text"] == button5["text"] == button8["text"] == "X":
        button2.config(bg="red")
        button5.config(bg="red")
        button8.config(bg="red")

        winner = True

        messagebox.showinfo("Tic tac toe", "X Won")
        disableButtons()
    
    if button2["text"] == button5["text"] == button8["text"] == "O":
        button2.config(bg="red")
        button5.config(bg="red")
        button8.config(bg="red")

        winner = True

        messagebox.showinfo("Tic tac toe", "O Won")
        disableButtons()

    #3rd Column
    if button3["text"] == button6["text"] == button9["text"] == "X":
        button3.config(bg="red")
        button6.config(bg="red")
        button9.config(bg="red")

        winner = True

        messagebox.showinfo("Tic tac toe", "X Won")
        disableButtons()

    if button3["text"] == button6["text"] == button9["text"] == "O":
        button3.config(bg="red")
        button6.config(bg="red")
        button9.config(bg="red")

        winner = True

        messagebox.showinfo("Tic tac toe", "O Won")
        disableButtons()

    #diagonal1
    if button1["text"] == button5["text"] == button9["text"] == "X":
        button1.config(bg="red")
        button5.config(bg="red")
        button9.config(bg="red")

        winner = True

        messagebox.showinfo("Tic tac toe", "X Won")
        disableButtons()

    if button1["text"] == button5["text"] == button9["text"] == "O":
        button1.config(bg="red")
        button5.config(bg="red")
        button9.config(bg="red")

        winner = True

        messagebox.showinfo("Tic tac toe", "O Won")
        disableButtons()

    #diagonal2
    if button3["text"] == button5["text"] == button7["text"] == "X":
        button3.config(bg="red")
        button5.config(bg="red")
        button7.config(bg="red")

        winner = True

        messagebox.showinfo("Tic tac toe", "X Won")
        disableButtons()
    
    if button3["text"] == button5["text"] == button7["text"] == "O":
        button3.config(bg="red")
        button5.config(bg="red")
        button7.config(bg="red")

        winner = True

        messagebox.showinfo("Tic tac toe", "O Won")
        disableButtons()

#Function for button
def play(b):
    
    global turn, count
    

    if b["text"] == " " and turn == "x":
        b["text"] = "X"
        turn = "o"
        count += 1
        checkWin()

    elif b["text"] == " " and turn == "o":
        b["text"] = "O"
        turn = "x"
        count += 1
        checkWin()

    else:
        messagebox.showerror("Tic Tac Toe", "HEYYY! That box has already been selected\nPick another box...")

    #button["text"] = "X"

#tic tac toe board

#first row
button1 = Button(frame2, text=" ", width="4", height="2", font=("Arial", 35), bg="#FFF8EA", command=lambda: play(button1))
button1.grid(row=0, column=0)


button2 = Button(frame2, text=" ", width="4", height="2", font=("Arial", 35), bg="#FFF8EA", command=lambda: play(button2))
button2.grid(row=0, column=1)


button3 = Button(frame2, text=" ", width="4", height="2", font=("Arial", 35), bg="#FFF8EA", command=lambda: play(button3))
button3.grid(row=0, column=2)


#second row
button4 = Button(frame2, text=" ", width="4", height="2", font=("Arial", 35), bg="#FFF8EA", command=lambda: play(button4))
button4.grid(row=1, column=0)


button5 = Button(frame2, text=" ", width="4", height="2", font=("Arial", 35), bg="#FFF8EA", command=lambda: play(button5))
button5.grid(row=1, column=1)


button6 = Button(frame2, text=" ", width="4", height="2", font=("Arial", 35), bg="#FFF8EA", command=lambda: play(button6))
button6.grid(row=1, column=2)
#button6.bind("<Button-6>", play)

#third row
button7 = Button(frame2, text=" ", width="4", height="2", font=("Arial", 35), bg="#FFF8EA", command=lambda: play(button7))
button7.grid(row=2, column=0)
#button7.bind("<Button-7>", play)

button8 = Button(frame2, text=" ", width="4", height="2", font=("Arial", 35), bg="#FFF8EA", command=lambda: play(button8))
button8.grid(row=2, column=1)
#button8.bind("<Button-8>", play)

button9 = Button(frame2, text=" ", width="4", height="2", font=("Arial", 35), bg="#FFF8EA", command=lambda: play(button9))
button9.grid(row=2, column=2)
#button9.bind("<Button-9>", play)

root.mainloop()
