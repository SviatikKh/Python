from tkinter import *
root = Tk()
root.title("Rainbow")
root.geometry("400x250+400+100")
bg = "white"
#root.resizable(False, False)
#Rainbow colors
clr = (
               "#ff0000:red", 
               "#ff7d00:orange",
               "#ffff00:yellow",
               "#00ff00:green",
               "#007dff:dodger blue", 
                "#0000ff:blue",
                "#7d00ff:purple"
               )

#creating a canvas for horizontal lines, location on the left
cg = Canvas(width=200, height=250, bg="white")
cg.pack(side = LEFT)
#creating a canvas for vertical lines, location on the right
cv = Canvas(width=200, height=250, bg="grey")
cv.pack(side = RIGHT)
#
x1 = 10
y1 = 10
x2 = 190
y2 = 240

for item in clr:
    num, name = item.split(":")
    cg.create_rectangle(x1, y1, x2, y2,  fill=num, outline='black',  width=1, activedash=(1, 4))
    cv.create_oval(x1, y1, x2, y2,  fill=num, outline='black',  width=1, activedash=(1, 1))
    cv.create_oval(x1, y1, x2, y2,  fill=num, outline='black',  width=1, activedash=(1, 1))
    x1 += 10
    y1 += 10
    x2 -= 10
    y2 -= 10


root.mainloop()
