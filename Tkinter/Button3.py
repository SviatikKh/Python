from tkinter import *
#from tkinter import messagebox

#window sizes
h_win = 400
w_win = 400
size = str(h_win) +"x" +str(w_win)
#fixed button dimensions
h_btn1 = 30
w_btn1 = 120
#coordinates of the fixed button for its location in the center of the window
x_btn1 = (w_win - w_btn1) //2
y_btn1 = (h_win - h_btn1) //2
#movable button sizes
h_btn2 = 30
w_btn2 = 100
#coordinates of the movable button
x_btn2 = 10
y_btn2 = 10
#button direction:
#0 - left along the upper border of the window, 
#1 - down along the right border of the window,
#2 - to the right along the lower border of the window,
#3 - up along the left border of the window
direct = 0
#fixed button label
def CaptionBtn1():
     global direct
     cap = ''
     if direct == 0:
         cap = "Left movement"
     elif direct == 1:
         cap = "Downward movement"
     elif direct == 2:
         cap = "Right movement"
     else:
         cap = "Upward movement"
     return cap
#movable button label
def CaptionBtn2():
    global x_btn2, y_btn2 
    return "x = " + str(x_btn2) + " y = " + str(y_btn2)
#ensuring the button moves to the left
def MoveLeft():
    global x_btn2, y_btn2
    if (x_btn2 + w_btn2) < (w_win - 10):
        x_btn2 += 10
    else:
       #change of direction
        direct = 1
#ensuring the button moves down
def MoveBottom():
     global x_btn2, y_btn2
     if (y_btn2 + h_btn2) < (h_win - 10):
        y_btn2 += 10
     else:
       direct = 2
 #ensuring the button moves to the right
def MoveRight():
    global x_btn2, y_btn2, direct
    if x_btn2  > 10:
        x_btn2 -= 10
    else:
       direct = 3
#ensuring the button moves up
def MoveTop():
     global x_btn2, y_btn2, direct
     if y_btn2 > 10:
        y_btn2 -= 10
     else:
       direct = 0
#button motion control
def Click_button():
    global x_btn2, y_btn2, direct
    #
    if direct == 0:
        MoveLeft()
    elif direct == 1:
        MoveBottom()
    elif direct == 2:
        MoveRight()
    else:
       MoveTop()
    #location of the movable button in a new window position
    btn2.place(x = x_btn2, y = y_btn2)
    #change the label on the movable button
    btn2.config(text =CaptionBtn2())
    #change the label on the fixed button
    btn1.config(text =CaptionBtn1())

#creating an instance of the class tkinter
root = Tk() 
#setting the window title
root.title('Project "Two buttons"' )
#definition of the window size
#root.geometry("400x400")
root.geometry(size)
#fixed button creation
btn1 = Button (
                        text = CaptionBtn1(), 
                        bg = "#555", fg = "#fff", 
                        padx = "3", pady = "3", 
                        font = ("Times New Roman", 10, "bold"), 
                        command = Click_button
                       )
btn1.place(x = x_btn1, y = y_btn1, width = w_btn1, height = h_btn1)
#movable button creation
btn2 = Button (
                        text = CaptionBtn2(), 
                        bg = "#ff0000", fg = "#fff", 
                        padx = "5", pady = "5", 
                        font=("Times New Roman", 8)
                       )
btn2.place(x = x_btn2, y = y_btn2, width = w_btn2, height = h_btn2)
 
#window display
root.mainloop()

