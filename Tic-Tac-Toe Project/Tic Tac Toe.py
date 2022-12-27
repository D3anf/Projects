#Resource used https://www.youtube.com/watch?v=xx0qmpuA-vM

#Basically importing everything from tkinter 
from tkinter import * 
from tkinter import messagebox

#Calling the class Tk
root = Tk()
#Setting the title and picture of my game
root.title("Tic-Tac_Toe by Dean Francis")
root.iconbitmap("wallpaper tree pink.ico")

# X starts so true
# We are initializing variables
#if True it's time for "X" to click if false it's "O"s turn to click
clicked = True 
count = 0 

#This function stops the buttons from being clicked
def disableAllButtons():
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)

#This function will see if someone has won
def checkifWon():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg = "pink")
        b2.config(bg = "pink")
        b3.config(bg = "pink")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Player 1 wins!")
        disableAllButtons()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg = "pink")
        b5.config(bg = "pink")
        b6.config(bg = "pink")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Player 1 wins!")
        disableAllButtons()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg = "pink")
        b8.config(bg = "pink")
        b9.config(bg = "pink")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Player 1 wins!")
        disableAllButtons()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg = "pink")
        b4.config(bg = "pink")
        b7.config(bg = "pink")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Player 1 wins!")
        disableAllButtons()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg = "pink")
        b5.config(bg = "pink")
        b8.config(bg = "pink")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Player 1 wins!")
        disableAllButtons()

    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg = "pink")
        b6.config(bg = "pink")
        b9.config(bg = "pink")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Player 1 wins!")
        disableAllButtons()

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg = "pink")
        b5.config(bg = "pink")
        b9.config(bg = "pink")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Player 1 wins!")
        disableAllButtons()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg = "pink")
        b5.config(bg = "pink")
        b7.config(bg = "pink")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Player 1 wins!")
        disableAllButtons()

        #### Check if O's win

    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg = "pink")
        b2.config(bg = "pink")
        b3.config(bg = "pink")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Player 2 wins!")
        disableAllButtons()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg = "pink")
        b5.config(bg = "pink")
        b6.config(bg = "pink")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Player 2 wins!")
        disableAllButtons()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg = "pink")
        b8.config(bg = "pink")
        b9.config(bg = "pink")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Player 2 wins!")
        disableAllButtons()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg = "pink")
        b4.config(bg = "pink")
        b7.config(bg = "pink")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Player 2 wins!")
        disableAllButtons()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg = "pink")
        b5.config(bg = "pink")
        b8.config(bg = "pink")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Player 2 wins!")
        disableAllButtons()

    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg = "pink")
        b6.config(bg = "pink")
        b9.config(bg = "pink")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Player 2 wins!")
        disableAllButtons()

    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg = "pink")
        b5.config(bg = "pink")
        b9.config(bg = "pink")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Player 2 wins!")
        disableAllButtons()

    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg = "pink")
        b5.config(bg = "pink")
        b7.config(bg = "pink")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","Player 2 wins!")
        disableAllButtons()
    #Checks if its a tie
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's a draw")
        disableAllButtons()


# Button clicked function
#So this funtion is saying that if a button is clicked that is empty and clicked is set to True, replace that button with a button with 
#an X and vice versa for O in it and set the value of clicked to False while incrementing the count variable and that is to track the number of moves because
#there are only 9 boxes so count has a range limit of 9, more than 9 moves you can't place any more X or O's which means it's a tie
#Personally I don't want to add an else statment as I don't want the program to make a big fuss over the player clicking the same block more than once
#But its just a nice feature
def b_click(b): 
    global clicked, count
    if b["text"] == " " and clicked == True: 
        b["text"] = "X"
        clicked = False
        count += 1  
        checkifWon()
    elif b["text"] == " " and clicked == False: 
        b["text"] = "O"
        clicked = True
        count += 1  
        checkifWon()
    else:
        messagebox.showerror("Tic Tac Toe", "That box has already been selected\nPick another box")    


def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0
    #Building our buttons
    #Basically we're building these buttons individually setting a function to a variable, "root" is the object of this function,
    #usually we set the values of parameters before we write the function but here we simply just write it inside the function
    b1 = Button(root, text = " ", font = ("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b1))
    b2 = Button(root, text = " ", font = ("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b2)) 
    b3 = Button(root, text = " ", font = ("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b3)) 

    b4 = Button(root, text = " ", font = ("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b4)) 
    b5 = Button(root, text = " ", font = ("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b5)) 
    b6 = Button(root, text = " ", font = ("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b6)) 

    b7 = Button(root, text = " ", font = ("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b7)) 
    b8 = Button(root, text = " ", font = ("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b8)) 
    b9 = Button(root, text = " ", font = ("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: b_click(b9)) 

    #Grid our buttons to the screen, this will be what seperates the buttons, its just easier for the user to see the buttons and where to click

    b1.grid(row = 0, column = 0)
    b2.grid(row = 0, column = 1)
    b3.grid(row = 0, column = 2)

    b4.grid(row = 1, column = 0)
    b5.grid(row = 1, column = 1)
    b6.grid(row = 1, column = 2)

    b7.grid(row = 2, column = 0)
    b8.grid(row = 2, column = 1)
    b9.grid(row = 2, column = 2)

#Creating a menu
#we're assigning the class Menu  
myMenu = Menu(root)
root.config(menu = myMenu)

#Create an Options menu
optionMenu = Menu(myMenu, tearoff=False)
myMenu.add_cascade(label = "Options", menu = optionMenu)
optionMenu.add_command(label = "Reset Game", command = reset)

reset() #Runs the program


#This method keeps the program running without it, the program will run and crash
root.mainloop()