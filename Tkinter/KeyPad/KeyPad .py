from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *

#=====================Logic================================
#"ABC" Button Event Handler
def Caps():
      tit = bt_caps["text"]
      if tit == "ABC":
          bt_caps["text"] = "abc"
      else:
          bt_caps["text"] = "ABC"
      #deleting all widgets in the container  frame_out
      for child in frame_out.winfo_children(): child.destroy() 
      SetABC() 

#"ABC" Button Event Handler
def Lang():
      tit = bt_lung["text"]
      if tit == "УКР":
          bt_lung["text"] = "ENG"
      else:
          bt_lung["text"] = "УКР"
      for child in frame_out.winfo_children(): child.destroy() 
      SetABC()

#The function of entering letters in a text box
def GetChar(tit):
    caps = bt_caps["text"]
    if caps.isupper():
         capslock = 0
    else:
        capslock = 1
    text.insert(END, tit[capslock])
    text.focus()
    RowCol()

#The function of entering numbers and other non-alphabetic characters into a text field
def GetOther(tit):
     text.insert(END, tit)
     text.focus()
     RowCol()

#Function to customize the keyboard according to the language and case selected
def SetABC():
     caps = bt_caps["text"]
     if caps.isupper():
          capslock = 0
     else:
         capslock = 1
     #
     lang = bt_lung["text"]
     ls = []
     if lang == "УКР":
         ls = bt_uk
     else:
         ls = bt_en
     #Container for buttons with letters (internal)
     frame_abc = Frame(frame_out, width = 210)
     frame_abc.pack(side = LEFT, fill = Y,  padx = 1, pady = 0, ipadx = 3, ipady = 3)
     #
     x = 0
     y = 0
     count = 0
     for bt in ls:
         com = lambda x = bt:GetChar(x)
         Button(frame_abc, text = bt[capslock], command = com).place(x = x, y = y, width= 30, height = 25)
         count += 1;
         if count >= 7:
             x = 0
             y += 25
             count = 0
         else:
             x += 30

#Event handler of pressing the operation buttons
def GetSpec(tit):
   if tit == "Space":
       text.insert(END, " ")
   elif tit == "Enter":
       text.insert(END, "\n")
   elif tit == "Del":
       text.delete("end-2c")
   else:
       text.delete(1.0, END)
   RowCol()

#
def RowCol():
     line, column = text.index('insert').split('.')
     lb_row["text"] = line
     lb_col["text"] = column
#
def PosCursor(event):
   RowCol()
    
#Shift the cursor position to the left
def MoveLeft(event):
    root.event_generate("<<LEFT>>")
    #messagebox.showinfo("", "Not working yet")

#Shift the cursor position to the left
def MoveRight(event):
    root.event_generate("<<Next>>")
    #messagebox.showinfo("", "Not working yet")

#Shift the cursor to the beginning of the text
def MoveHome(event):
    root.event_generate("<<Home>>")
    #messagebox.showinfo("", "Not working yet")

#Shift the cursor to the end of the text
def MoveEnd(event):
    root.event_generate("<<End>>")
    #messagebox.showinfo("", "Not working yet")

#===Menu command event handlers===
#Event Handler Clicking button "Save To File"
def SaveToFile():
    file = asksaveasfile(defaultextension=".txt")
    try:
        file.write(text.get(1.0, END))
    except:
        messagebox.showinfo("", "File save operation \ nwas canceled")

#Event Handler Clicking button "Load from file"
def LoadFromFile():
    file = askopenfilename(filetypes = [('Text files', '.txt')])
    try:
        with open(file) as file:
            for i in file:
                 text.insert(END, i)
    except:
         messagebox.showinfo("", "The download operation \ nhas been canceled")

#Event Handler Clicking button "Delete Selection"
def DeleteSelection():
    try:
        content = text.selection_get()
        text.delete(SEL_FIRST, SEL_LAST)
    except:
        messagebox.showinfo("", "A piece of text should be selected")

#Event Handler Clicking button "Copy Selection"
def CopySelection():
    try:
        content = text.selection_get()
        text.clipboard_append(content)
    except:
        messagebox.showinfo("", "A piece of text should be selected")

#Event Handler Clicking button "Insert Selection"
def InsertSelection():
    s = text.clipboard_get()
    if len(s) > 0:
        text.focus
        text.insert(INSERT, s)
    else:
        messagebox.showinfo("", "The clipboard is empty")
    #messagebox.showinfo("Text editor", s)
    #text.tag_add("sel", SEL_FIRST, SEL_LAST)
    #s = text.tag_cget("sel")

#====================== WINDOW CREATION ==============================
#Window creation
root=Tk()
#Specify the size and position of the window on the screen
root.geometry("600x475+400+100")
#Assigning a window title
root.title("A text editor with its own keyboard")
#Assigning a window background
root["bg"] = "#999"
#Prohibition of windows resize
root.resizable(False, False)
#==================== MAIN MENU ================================
#Main menu
main_menu = Menu()
#Menu section "File"
file_menu = Menu()
#Pictures for the menu commands of the "File" section
im_new = PhotoImage(file="New.png")
im_import = PhotoImage(file="Import.png")
im_export = PhotoImage(file="Export.png")
im_save = PhotoImage(file="Save.png")
im_exit = PhotoImage(file="Exit.png")
#Menu commands of "File" section
file_menu.add_command(label = "Create", image = im_new, compound=LEFT, accelerator ='Ctrl+N', command = LoadFromFile)
file_menu.add_command(label = "Open", image = im_import, compound=LEFT, accelerator ='Ctrl+I', command = LoadFromFile)
file_menu.add_command(label = "Save", image = im_export, compound=LEFT, accelerator ='Ctrl+E', command = SaveToFile)
file_menu.add_command(label = "Save As...", image = im_save, compound=LEFT, accelerator ='Ctrl+S', command = SaveToFile)
file_menu.add_separator()
file_menu.add_command(label = "Exit", image =im_exit, compound=LEFT, accelerator ='Ctrl+Q', command = root.destroy)
#Menu section "Edit"
edit_menu = Menu()
#Pictures for menu commands in the "Edit" section
im_delete = PhotoImage(file="Delete.png")
im_copy = PhotoImage(file="Copy.png")
im_insert = PhotoImage(file="Insert.png")
#Menu commands of "Edit" section
edit_menu.add_command(label = "Delete Selection", image = im_delete, compound=LEFT, accelerator ='Ctrl+X', command = DeleteSelection)
edit_menu.add_command(label = "Copy Selection", image = im_copy, compound=LEFT, accelerator ='Ctrl+C',  command =CopySelection)
edit_menu.add_command(label = "Insert Selection", image = im_insert, compound=LEFT, accelerator ='Ctrl+V', command =InsertSelection)
#Adding sections to the main menu 
main_menu.add_cascade(label="File", menu = file_menu)
main_menu.add_cascade(label="Edit", menu = edit_menu)

#Container with multiline text box
frame_text = Frame(root)
frame_text.pack(side = TOP, fill = X, padx = 5, pady = 3, ipadx = 3, ipady = 3)
#Creating and positioning a text box
text = Text(frame_text, bg="white", fg='black', height = 18, wrap=WORD)
text.pack(side = TOP,   padx = 1, pady = 1, ipadx = 1, ipady = 1)
text.focus
text.bind('<Button-1>', PosCursor)
#Container - cursor position data
frame_cursor = Frame(root, bg = "black")
frame_cursor.pack(side = TOP, fill = X, padx = 5, pady = 3, ipadx = 3, ipady = 3)
Label(frame_cursor, text = "# of row", width = 10).pack(side = LEFT, fill = Y, padx = 3, pady = 3, ipadx = 3, ipady = 3)
lb_row = Label(frame_cursor, text = "1", width = 3)
lb_row.pack(side = LEFT, fill = Y, padx = 3, pady = 3, ipadx = 3, ipady = 3)
Label(frame_cursor, text = "# of symbol", width = 10).pack(side = LEFT, fill = Y, padx = 3, pady = 3, ipadx = 3, ipady = 3)
lb_col = Label(frame_cursor, text = "1", width = 3)
lb_col.pack(side = LEFT, fill = Y, padx = 3, pady = 3, ipadx = 3, ipady = 3)

#Container for buttons with letters (external)
frame_out = Frame(root, bg = "black", width = 210)
frame_out.pack(side = LEFT, fill = Y,  padx = 3, pady = 1, ipadx = 0, ipady = 0)
#Alphabets (Ukrainian and English)
bt_uk = (
               "Аа",	"Бб",	"Вв", "Гг", "Ґґ", "Дд", "Ее", "Єє", "Жж", "Зз",
               "Ии", "Іі", "Її",	"Йй", "Кк", "Лл", "Мм", "Нн",	"Оо", "Пп",
               "Рр", "Сс","Тт", "Уу", "Фф",	"Хх", "Цц", "Чч", "Шш", "Щщ",
               "Ьь", "Юю", "Яя"
              )
bt_en = (
               "Aa",	"Bb", "Cc", "Dd", "Ee", "Ff", "Gg", "Hh", "Ii", "Jj",
               "Kk", "Ll", "Mm", "Nn", "Oo", "Pp", "Qq", "Rr",	"Ss", "Tt",
               "Uu", "Vv","Ww", "Xx", "Yy", "Zz"
              )
########################################################
#Container for buttons to control the appearance of the keyboard for letters
frame_tools = Frame(root, width = 40)
frame_tools.pack(side = LEFT, fill = Y,  padx = 1, pady = 1, ipadx = 3, ipady = 3)
#Creating and Locationing the "ABC" button (CapsLock)
bt_caps = Button(frame_tools, text = "ABC", command = Caps)
bt_caps.place(x = 3, y = 0, width= 40, height = 50)
#Creating and positioning the "УКР" button (Language)
bt_lung = Button(frame_tools, text = "УКР", command = Lang)
bt_lung.place(x = 3, y = 50, width= 40, height = 50)
#Set the keyboard according to the default language and case
SetABC()
######################### doesn't work yet ###############################
#Container for buttons to move the text
frame_move = Frame(root, width = 45)
frame_move.pack(side = LEFT, fill = Y,  padx = 1, pady = 1, ipadx = 3, ipady = 3)
#Creating and positioning a button "←" ()
bt_left = Button(frame_move, text = "←", font = ("Times New Roman", 16, "bold"))
bt_left.place(x = 3, y = 0, width= 45, height = 25)
bt_left.bind('<Button-1>', MoveLeft)
#Creating and positioning a button "→" ()
bt_right = Button(frame_move, text = "→", font = ("Times New Roman", 16, "bold"))
bt_right.place(x = 3, y = 25, width= 45, height = 25)
bt_right.bind('<Button-1>', MoveRight)
#Creating and positioning a button "Home" ()
bt_home = Button(frame_move, text = "Home")
bt_home.place(x = 3, y = 50, width= 45, height = 25)
bt_home.bind('<Button-1>', MoveHome)
#Creating and positioning a button "End" ()
bt_end = Button(frame_move, text = "End")
bt_end.place(x = 3, y = 75, width= 45, height = 25)
bt_end.bind('<Button-1>', MoveEnd)

###########################################################################3
#Container for operating buttons 
frame_spec = Frame(root, width = 45)
frame_spec.pack(side = LEFT, fill = Y,  padx = 1, pady = 1, ipadx = 3, ipady = 3)
#List of operating button headers
bt_spec = ("Space", "Enter","Del", "Clear")
#Creating and positioning operating buttons
x = 0
y = 0
for bt in bt_spec:
    com = lambda x = bt:GetSpec(x)
    Button(frame_spec, text = bt, command = com).place(x = x, y = y, width= 45, height = 25)
    y += 25
##########################################################################
#Container for buttons with numbers and other non-alphabetic characters
frame_other = Frame(root, width = 210)
frame_other.pack(side = LEFT, fill = Y,  padx = 1, pady = 1, ipadx = 3, ipady = 3)
bt_other = (
                     "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                     "!", "?", ".", ",", ":", ";", "(", ")", "{", "}", 
                     "+", "-", "*", "/", "@", "#", "%", "&"
                  )
x = 0
y = 0
count = 0
for bt in bt_other:
    com = lambda x = bt:GetOther(x)
    Button(frame_other, text = bt, command = com).place(x = x, y = y, width= 30, height = 25)
    count += 1;
    if count >= 7:
        x = 0
        y += 25
        count = 0
    else:
        x += 30
#Setting focus to a text field
#text.focus()
#
##shortcut keys
#root.bind("<Control-n>", LoadFromFile)
#root.bind("<Control-I>", LoadFromFile)
#root.bind("<Control-E>", SaveToFile)
#root.bind("<Control-S>", SaveToFile)
#root.bind("<Control-X>", DeleteSelection)
#root.bind("<Control-C>", CopySelection)
#root.bind("<Control-V>", InsertSelection)
#Binding the main menu to the window
root.config(menu=main_menu)
#window display
root.mainloop()

