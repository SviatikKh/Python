from tkinter import *
root = Tk()
root.title("Rainbow")
root.geometry("430x430+400+100")
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
cnv = Canvas(width=403, height=403, bg="white")
cnv.pack(padx = 5, pady = 5)

cnv.create_oval(3, 3, 403, 403,  fill= "white", outline='black',  width=1, activedash=(1, 1))

beg = 0
coner = 15
index = 0

for i in range(24):
    num, name = clr[index].split(":")
    cnv.create_arc(3, 3, 403, 403, start = beg, extent = coner, fill = num, outline = num)
    beg += coner
    index += 1
    if index > 6:
        index = 0


root.mainloop()


