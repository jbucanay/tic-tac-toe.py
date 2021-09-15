from tkinter import *
from tkinter import messagebox

## 1. tic tac toe title

root = Tk()
root.title("Tic Tac Toe")
## disable all buttons

winner = False

def checkIfWon():
    global winner
    winner = False

    ## X WINNING TOP TO BUTTOM
    if b1["text"] == "X" and b2["text"] =="X" and b3["text"] == "X":
        b1.config(fg="red")
        b2.config(fg="red")
        b3.config(fg="red")
        messagebox.showinfo(title="X Wins!", message="X Wins!")
        winner = True
        disable_all_buttons()

    elif b4["text"] == "X" and b5["text"] =="X" and b6["text"] == "X":
        b1.config(fg="red")
        b2.config(fg="red")
        b3.config(fg="red")
        messagebox.showinfo(title="X Wins!", message="X Wins!")
        winner = True
        disable_all_buttons()

    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b1.config(fg="red")
        b2.config(fg="red")
        b3.config(fg="red")
        messagebox.showinfo(title="X Wins!", message="X Wins!")
        winner = True
        disable_all_buttons()

    #LEFT TO RIGHT b1,b4,b7
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(fg="red")
        b2.config(fg="red")
        b3.config(fg="red")
        messagebox.showinfo(title="X Wins!", message="X Wins!")
        winner = True
        disable_all_buttons()
    #b2,b5,b8
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b1.config(fg="red")
        b2.config(fg="red")
        b3.config(fg="red")
        messagebox.showinfo(title="X Wins!", message="X Wins!")
        winner = True
        disable_all_buttons()
    #3,6,9
    elif b3["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b1.config(fg="red")
        b2.config(fg="red")
        b3.config(fg="red")
        messagebox.showinfo(title="X Wins!", message="X Wins!")
        winner = True
        disable_all_buttons()
    #1,5,9
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(fg="red")
        b2.config(fg="red")
        b3.config(fg="red")
        messagebox.showinfo(title="X Wins!", message="X Wins!")
        winner = True
        disable_all_buttons()
    #3,5,7
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b1.config(fg="red")
        b2.config(fg="red")
        b3.config(fg="red")
        messagebox.showinfo(title="X Wins!", message="X Wins!")
        winner = True
        disable_all_buttons()

## END OF X WINNING

## START OF O WINNING
    if b1["text"] == "O" and b2["text"] =="O" and b3["text"] == "O":
        b1.config(fg="red")
        b2.config(fg="red")
        b3.config(fg="red")
        messagebox.showinfo(title="O Wins!", message="O Wins!")
        winner = True
        disable_all_buttons()

    elif b4["text"] == "O" and b5["text"] =="O" and b6["text"] == "O":
        b1.config(fg="red")
        b2.config(fg="red")
        b3.config(fg="red")
        messagebox.showinfo(title="O Wins!", message="O Wins!")
        winner = True
        disable_all_buttons()

    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b1.config(fg="red")
        b2.config(fg="red")
        b3.config(fg="red")
        messagebox.showinfo(title="O Wins!", message="O Wins!")
        winner = True
        disable_all_buttons()

    #LEFT TO RIGHT b1,b4,b7
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(fg="red")
        b2.config(fg="red")
        b3.config(fg="red")
        messagebox.showinfo(title="O Wins!", message="O Wins!")
        winner = True
        disable_all_buttons()
    #b2,b5,b8
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b1.config(fg="red")
        b2.config(fg="red")
        b3.config(fg="red")
        messagebox.showinfo(title="O Wins!", message="O Wins!")
        winner = True
        disable_all_buttons()
    #3,6,9
    elif b3["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b1.config(fg="red")
        b2.config(fg="red")
        b3.config(fg="red")
        messagebox.showinfo(title="O Wins!", message="O Wins!")
        winner = True
        disable_all_buttons()
    #1,5,9
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(fg="red")
        b2.config(fg="red")
        b3.config(fg="red")
        messagebox.showinfo(title="O Wins!", message="O Wins!")
        winner = True
        disable_all_buttons()
    #3,5,7
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b1.config(fg="red")
        b2.config(fg="red")
        b3.config(fg="red")
        messagebox.showinfo(title="O Wins!", message="O Wins!")
        winner = True
        disable_all_buttons()

##END OF O WINNING


## button click, change text to "x", change button to false
clicked = True
count = 0

def b_click(b):
    global count, clicked
    if b["text"] ==" " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkIfWon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1



## define who the winner is


def disable_all_buttons():
    global count, winner
    if winner == True or count >= 9:
        b1.config(state = DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
        try:
            response = messagebox.askquestion(title="Play again", message="Play again" )
            print(response)
            if response == 'yes':
                count = 0
                clicked = True
                winner = False
                b1.config(text=' ', state=NORMAL)
                b2.config(text=' ', state=NORMAL)
                b3.config(text=' ', state=NORMAL)
                b4.config(text=' ', state=NORMAL)
                b5.config(text=' ', state=NORMAL)
                b6.config(text=' ', state=NORMAL)
                b7.config(text=' ', state=NORMAL)
                b8.config(text=' ', state=NORMAL)
                b9.config(text=' ', state=NORMAL)
            else:
                root.destroy().pack()
        except:
            print('what happened?')




##buttons

b1 = Button(root, text= " ", height=6, width=6,bg='black',command= lambda: b_click(b1))
b2 = Button(root, text= " ", height=6, width=6,  command= lambda: b_click(b2))
b3 = Button(root, text= " ", height=6, width=6,  command= lambda: b_click(b3))

b4 = Button(root, text= " ", height=6, width=6,  command= lambda: b_click(b4))
b5 = Button(root, text= " ", height=6, width=6,  command= lambda: b_click(b5))
b6 = Button(root, text= " ", height=6, width=6,  command= lambda: b_click(b6))

b7 = Button(root, text= " ", height=6, width=6,  command= lambda: b_click(b7))
b8 = Button(root, text= " ", height=6, width=6,  command= lambda: b_click(b8))
b9 = Button(root, text= " ", height=6, width=6, command= lambda: b_click(b9))

##reset button
b10 = Button(root, text="Reset")
## buttons on grids
b1.grid(row=0, column = 0)
b2.grid(row=0, column = 1)
b3.grid(row=0, column = 2)

b4.grid(row=1, column = 0)
b5.grid(row=1, column = 1)
b6.grid(row=1, column = 2)

b7.grid(row=2, column = 0)
b8.grid(row=2, column = 1)
b9.grid(row=2, column = 2)

#reset button








root.mainloop()