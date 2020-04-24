from tkinter import *
from tkinter import messagebox
#from tkinter.filedialog import *

 #handler pressing letter buttons 
def GetChar(tit):
    if tit.isdigit():
        capslock = 0
    else:
        caps = bt_caps["text"]
        #messagebox.showinfo("Text editor", tit)
        if caps.isupper():
             capslock = 0
        else:
            capslock = 1
    text.insert(END, tit[capslock])
#pressing operation buttons handler
def GetSpec(tit):
   if tit == "Space":
       text.insert(END, " ")
   elif tit == "Enter":
       text.insert(END, "\n")
   elif tit == "Del":
       text.delete("end-2c")
   else:
       text.delete(1.0, END)
#handler of pressing "ABC" buttons
def Caps():
      tit = bt_caps["text"]
      if tit == "ABC":
          bt_caps["text"] = "abc"
      else:
          bt_caps["text"] = "ABC"

#Window creation
root=Tk()
#Assigning the size and position of the window on the screen
root.geometry("400x510+400+100")
#Window Title Assignment
root.title("Text editor")
#Window Background Assignment
root["bg"] = "#333"
#Prevent window resizing
root.resizable(False, False)
#Container with the heading "Text"
ft = LabelFrame(root, text = "Text", height = 335)
ft.pack(side = TOP, fill = X, padx = 5, pady = 3, ipadx = 3, ipady = 3)
#Container with the headline "Keyboard"
fl = LabelFrame(root, text = "Keyboard", height = 200)
fl.pack(side = BOTTOM, fill = X, padx = 5, pady = 3, ipadx = 3, ipady = 3)
#List of symbolic button headers
bt_char = (

               "Аа",	"Бб",	"Вв", "Гг", "Ґґ", "Дд", "Ее", "Єє", "Жж", "Зз",
               "Ии", "Іі", "Її",	"Йй", "Кк", "Лл", "Мм", "Нн",	"Оо", "Пп",
               "Рр", "Сс","Тт", "Уу", "Фф",	"Хх", "Цц", "Чч", "Шш", "Щщ",
               "Ьь", "Юю", "Яя", "!?",".,",":;","({",")}","+-","*/",
               "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
           )
#Creating and placing symbol buttons
x = 0
y = 0
count = 0
for bt in bt_char:
    com = lambda x = bt:GetChar(x)
    Button(fl, text = bt, command = com).place(x = x, y = y, width= 30, height = 25)
    count += 1;
    if count >= 10:
        x = 0
        y += 25
        count = 0
    else:
        x += 30
#List of operating buttons headers
bt_spec = ("Space", "Enter","Del", "Clear")
#Creating and placing operating buttons
x = 300
y = 0
for bt in bt_spec:
    com = lambda x = bt:GetSpec(x)
    Button(fl, text = bt, command = com).place(x = x, y = y, width= 60, height = 25)
    y += 25
#Creation and placement of "ABC" button (CapsLock)
bt_caps = Button(fl, text = "ABC", command = Caps)
bt_caps.place(x = x, y = y, width= 60, height = 25)

#Creation and the arrangement of the text field
text = Text(ft, bg="#333", fg='white', height = 20, wrap=WORD)
text.pack(side = LEFT, fill = Y,  padx = 1, pady = 1, ipadx = 1, ipady = 1)

#Window display
root.mainloop()
