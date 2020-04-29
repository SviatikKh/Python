from tkinter import *

#seconds counter
counter = 0 
#sign of stopwatch work
enab = False
def Tim():
    global counter, enab
    if enab:
        counter += 1
        label["text"] = ShowTime(counter)
        label.after(1000, Tim)

#Convert seconds to a view time string "hh:mm:ss"
def ShowTime(sec):
    s = sec
    m = s // 60
    s = s % 60
    h = m // 60
    m = m % 60
    tm = ""
    if h < 10:
        tm += "0"
    tm += str(h) + ":"
    if m < 10:
        tm += "0"
    tm += str(m) + ":"
    if s < 10:
        tm += "0"
    tm += str(s) 
    return tm
#Stopwatch status control
def Stopwatch():
    global enab, counter
    tit = button["text"]
    if tit == "Turn on":
        button["text"] = "Turn off"
        enab = True
        Tim()
    else:
        button["text"] = "Turn on"
        enab = False
        label["text"] = "00:00:00"
        counter = 0

root = Tk()
root.title("Stopwatch")
root.geometry("250x125+400+100")
root.resizable(False, False)
label = Label(fg="blue", text = "00:00:00", font = ("Times New Roman", 36, "bold"))
label.pack(side = TOP, fill = X, padx = 5, pady = 3, ipadx = 3, ipady = 3)
button = Button(fg="red", text='Увімкнути', font = ("Times New Roman", 16, "bold"), command=Stopwatch)
button.pack(side = BOTTOM, fill = X, padx = 5, pady = 3, ipadx = 3, ipady = 3)
root.mainloop()
