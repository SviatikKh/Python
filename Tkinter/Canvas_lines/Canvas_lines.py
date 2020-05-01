from tkinter import *
root = Tk()
root.title("Rainbow")
root.geometry("405x250+400+100")
bg = "white"
root.resizable(False, False)
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
cg = Canvas(root, width=200, height=250, bg="white")
cg.pack(side = LEFT)
#creating a canvas for vertical lines, location on the right
cv = Canvas(root, width=200, height=250, bg="grey")
cv.pack(side = RIGHT)
y = 20      #start vertical reference for horizontal lines
x = 16      #start horizontal reference for vertical lines
#drawing lines with colors from the list clr, width - line thickness
#the first four parameters are the coordinates of the left upper and right lower corners of the line image
for item in clr:
    num, name = item.split(":")
    cg.create_line(5, y, 200, y, width = 30,  fill = num)
    cv.create_line(x, 0, x, 250, width = 25,  fill = num)
    #cg.create_text(100, y, text = name, justify=CENTER, font="Verdana 14")
    y += 35
    x += 28
#drawing of arrows 
cg.create_line(100, 240, 100, 10, fill='black', width=10, arrow=LAST, dash=(10, 2), activefill='grey', arrowshape="10 30 10")
cv.create_line(10, 120, 190, 120, fill='black', width=10, arrow=LAST, activefill='grey', arrowshape="10 10 10")
  
root.mainloop()
