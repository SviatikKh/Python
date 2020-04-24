from tkinter import *
from tkinter import messagebox

#Window creation
root=Tk()
#Assigning the size and position of the window on the screen
root.geometry("250x125+500+200")
#Window Title Assignment
root.title("Button colors")
#Window Background Assignment
root["bg"] = "#125"
#Prevent window resizing
root.resizable(False, False)
#
def GetColorButton(tit):
    ls = tit.split(':')
    lb1["fg"] =  ls[0]
    lb1["text"] = ls[0]
    lb2["fg"] =  ls[0]
    lb2["text"] =ls[1]
    #messagebox.showinfo("Button colors", tit)

btns = (
               "#ff0000:red", 
               "#ff7d00:orange",
               "#ffff00:yellow",
               "#00ff00:green",
               "#007dff:dodger blue", 
                "#0000ff:blue",
                "#7d00ff:purple"
               )

lb1 = Label(bg = "#FFF", height = 2, font = ("Times New Roman", 10, "bold"))
lb1.pack(side = TOP, fill = X, padx = 5, pady = 3)
lb2 = Label(bg = "#FFF", height = 2, font = ("Times New Roman", 10, "bold"))
lb2.pack(side = TOP, fill = X, padx = 5, pady = 3)
fr = Frame()
fr.pack(side = TOP, padx = 1, pady = 1)
for bt in btns:
    ls = bt.split(':')
    com = lambda x = bt:GetColorButton(x)
    Button(fr, bg = ls[0], width= 3, command = com).pack(side = LEFT, padx = 1, pady = 3)

root.mainloop()
