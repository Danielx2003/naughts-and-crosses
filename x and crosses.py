import tkinter as tk
from tkinter import *
import random
import tkinter.messagebox
fontType = ("Arial", 9)

class window(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.label = Label(master, text="no player")
        self.label.place(x=60,y=255)

        self.b1 = tk.Button(master, width=9, height=4, justify='center')
        self.b1.place(x=10, y=10)
        self.b2 = tk.Button(master, width=9, height=4, justify='center')
        self.b2.place(x=90, y=10)
        self.b3 = tk.Button(master, width=9, height=4, justify='center')
        self.b3.place(x=170, y=10)
        self.b4 = tk.Button(master, width=9, height=4, justify='center')
        self.b4.place(x=10, y=90)
        self.b5 = tk.Button(master, width=9, height=4, justify='center')
        self.b5.place(x=90, y=90)
        self.b6 = tk.Button(master, width=9, height=4, justify='center')
        self.b6.place(x=170, y=90)
        self.b7 = tk.Button(master, width=9, height=4, justify='center')
        self.b7.place(x=10, y=170)
        self.b8 = tk.Button(master, width=9, height=4, justify='center')
        self.b8.place(x=90, y=170)
        self.b9 = tk.Button(master, width=9, height=4, justify='center')
        self.b9.place(x=170, y=170)

        Game(self)

class Game(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        ran = random.randint(1, 2)
        self.whatPlayer(ran)


    def whatPlayer(self, count):
        if count % 2 != 0:
            self.master.label.configure(text="Player 1's Turn", font=fontType)
            self.player1(count)
        else:
            self.master.label.configure(text="Player 2's Turn", font=fontType)
            self.player2(count)

        if count > 11:
            root.destroy()

    def gameOver(self):
        if self.master.b1['bg'] == "red" and self.master.b2['bg'] == "red" and self.master.b3['bg'] == "red":
            tkinter.messagebox.showinfo("Game Over", "Red Wins")
            root.destroy()
        elif self.master.b1['bg'] == "red" and self.master.b4['bg'] == "red" and self.master.b7['bg'] == "red":
            tkinter.messagebox.showinfo("Game Over", "Red Wins")
            root.destroy()

        elif self.master.b1['bg'] == "red" and self.master.b5['bg'] == "red" and self.master.b9['bg'] == "red":
            tkinter.messagebox.showinfo("Game Over", "Red Wins")
            root.destroy()
        elif self.master.b2['bg'] == "red" and self.master.b5['bg'] == "red" and self.master.b8['bg'] == "red":
            tkinter.messagebox.showinfo("Game Over", "Red Wins")
            root.destroy()
        elif self.master.b4['bg'] == "red" and self.master.b5['bg'] == "red" and self.master.b6['bg'] == "red":
            tkinter.messagebox.showinfo("Game Over", "Red Wins")
            root.destroy()
        elif self.master.b7['bg'] == "red" and self.master.b8['bg'] == "red" and self.master.b9['bg'] == "red":
            tkinter.messagebox.showinfo("Game Over", "Red Wins")
            root.destroy()
        elif self.master.b3['bg'] == "red" and self.master.b6['bg'] == "red" and self.master.b9['bg'] == "red":
            tkinter.messagebox.showinfo("Game Over", "Red Wins")
            root.destroy()
        elif self.master.b1['bg'] == "blue" and self.master.b2['bg'] == "blue" and self.master.b3['bg'] == "blue":
            tkinter.messagebox.showinfo("Game Over", "Blue Wins")
            root.destroy()
        elif self.master.b1['bg'] == "blue" and self.master.b4['bg'] == "blue" and self.master.b7['bg'] == "blue":
            tkinter.messagebox.showinfo("Game Over", "Blue Wins")
            root.destroy()
        elif self.master.b1['bg'] == "blue" and self.master.b5['bg'] == "blue" and self.master.b9['bg'] == "blue":
            tkinter.messagebox.showinfo("Game Over", "Blue Wins")
            root.destroy()
        elif self.master.b2['bg'] == "blue" and self.master.b5['bg'] == "blue" and self.master.b8['bg'] == "blue":
            tkinter.messagebox.showinfo("Game Over", "Blue Wins")
            root.destroy()
        elif self.master.b4['bg'] == "blue" and self.master.b5['bg'] == "blue" and self.master.b6['bg'] == "blue":
            tkinter.messagebox.showinfo("Game Over", "Blue Wins")
            root.destroy()
        elif self.master.b7['bg'] == "blue" and self.master.b8['bg'] == "blue" and self.master.b9['bg'] == "blue":
            tkinter.messagebox.showinfo("Game Over", "Blue Wins")
            root.destroy()
        elif self.master.b3['bg'] == "blue" and self.master.b6['bg'] == "blue" and self.master.b9['bg'] == "blue":
            tkinter.messagebox.showinfo("Game Over", "Blue Wins")
            root.destroy()
        else:
            return None


    def player1(self, count):
        colour = "red"
        count += 1
        text = "X"

        self.master.b1.configure(command=lambda: (self.insert(1, colour, text), self.whatPlayer(count)))
        self.master.b2.configure(command=lambda: (self.insert(2, colour, text), self.whatPlayer(count)))
        self.master.b3.configure(command=lambda: (self.insert(3, colour, text), self.whatPlayer(count)))
        self.master.b4.configure(command=lambda: (self.insert(4, colour, text), self.whatPlayer(count)))
        self.master.b5.configure(command=lambda: (self.insert(5, colour, text), self.whatPlayer(count)))
        self.master.b6.configure(command=lambda: (self.insert(6, colour, text), self.whatPlayer(count)))
        self.master.b7.configure(command=lambda: (self.insert(7, colour, text), self.whatPlayer(count)))
        self.master.b8.configure(command=lambda: (self.insert(8, colour, text), self.whatPlayer(count)))
        self.master.b9.configure(command=lambda: (self.insert(9, colour, text), self.whatPlayer(count)))

    def player2(self, count):
        colour = "blue"
        text = "O"
        count += 1

        self.master.b1.configure(command=lambda: (self.insert(1, colour, text), self.whatPlayer(count)))
        self.master.b2.configure(command=lambda: (self.insert(2, colour, text), self.whatPlayer(count)))
        self.master.b3.configure(command=lambda: (self.insert(3, colour, text), self.whatPlayer(count)))
        self.master.b4.configure(command=lambda: (self.insert(4, colour, text), self.whatPlayer(count)))
        self.master.b5.configure(command=lambda: (self.insert(5, colour, text), self.whatPlayer(count)))
        self.master.b6.configure(command=lambda: (self.insert(6, colour, text), self.whatPlayer(count)))
        self.master.b7.configure(command=lambda: (self.insert(7, colour, text), self.whatPlayer(count)))
        self.master.b8.configure(command=lambda: (self.insert(8, colour, text), self.whatPlayer(count)))
        self.master.b9.configure(command=lambda: (self.insert(9, colour, text), self.whatPlayer(count)))



    def insert(self, num, colour, text):

        if num == 1:
            self.master.b1.configure(bg=colour, text=text, font=fontType)
        if num == 2:
            self.master.b2.configure(bg=colour, text=text, font=fontType)
        if num == 3:
            self.master.b3.configure(bg=colour, text=text, font=fontType)
        if num == 4:
            self.master.b4.configure(bg=colour, text=text, font=fontType)
        if num == 5:
            self.master.b5.configure(bg=colour, text=text, font=fontType)
        if num == 6:
            self.master.b6.configure(bg=colour, text=text, font=fontType)
        if num == 7:
            self.master.b7.configure(bg=colour, text=text, font=fontType)
        if num == 8:
            self.master.b8.configure(bg=colour, text=text, font=fontType)
        if num == 9:
            self.master.b9.configure(bg=colour, text=text, font=fontType)

        self.gameOver()










root = tk.Tk()
app = window(root)
root.geometry("250x300")
root.mainloop()