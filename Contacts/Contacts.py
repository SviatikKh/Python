import os
# Contacts class on your phone
class Kont:
    def __init__(self):
        self.data = {}             #file line list
        self.count = 0
       
    #Reading data from '' Kontaktu.txt '' file into data dictionary
    def ReadFromFile(self):            
        if os.path.isfile('Kontaktu.txt') == False:
            print('File is missing')
        else:      
            with open('Kontaktu.txt') as file:
                for it in file:
                    #Recording to the list of rows from the file without line translation character
                    s = it.rstrip('\n')
                    ls = s.split(':')
                    self.data[ls[0]] = ls[1]
            self.count = len(self.data)
        return self.data

     #Data recording to file '' Kontaktu.txt '' from data dictionary 
    def WriteToFile(self):
        frecord = open('Kontaktu.txt', 'wt')
        for item in self.data.keys():
            frecord.write(item + ':' + self.data[item] + '\n')
        frecord.close() 

    #Displaying of the contacts
    def Show(self):
        print("The list of contacts")
        n = 0
        for item in self.data.keys():
            n += 1
            print('{0:<3d}{1:<20s}{2:<20s}'.format(n, item, self.data[item]))
        print('Number of entries - ' + str(self.count))

    #Searching the phone number by name (key)
    def FindKey(self, name):
        phone = ''
        #ls = self.data.keys()
        if name in self.data.keys():
            phone = self.data[name]
        return phone

    #Searching a name by phone number
    def FindValue(self, phone):
        name = ''
        for item in self.data.keys():
             if (self.data[item] == phone):
                 name = item
                 break
        return name

    ## Adding/changing contact
    def AddKontakt(self):
        y = "+"
        name  = input("Name:        ")
        if name in self.data.keys():
            y = input("Name " + name + " already in contact list! Replace (+/-)")
        if y == "+":
            phone = input("Phone: ")
            self.data[name] = phone
            self.count += 1
            print("Contact " + name + " : " + phone + " added")
            self.WriteToFile()

    #Removing contact
    def DelKontakt(self):
         name  = input("Name:        ")
         if name in self.data.keys():
            y = input("Remove the contact " + name + " ? (+/-)")
            if y == "+":
                phone = self.data[name]
                del self.data[name]
                self.count -= 1
                print("Contact " + name + " : " + phone + " removed")
                self.WriteToFile()
            else:
                print("Removing of the contact" + name + " cancelled")
         else:
            print("Contact is missing!")
    
    #Menu
    def Menu(self):
        m = 0
        print(30*"=")
        print("1.Show the contacts")
        print("2.Add contact")
        print("3.Remove contact")
        print("4.Find phone № by name")
        print("5.Find a name by phone № ")
        print("6.Turn off the phone")
        print(30*"=")
        op = False
        while op == False:
            num = input("Enter option №: ")
            if num.isdigit() == True:
                if int(num) > 0 and int(num) < 7:
                    m = int(num)
                    op = True
                else:
                    print("Option № value is incorrect ")
            else:
                print("Option № format is incorrect ")
        return m

    #Executing of options in contacts
    def Execute(self):
        self.ReadFromFile()
        while True:
                m = self.Menu()
                if m == 1:
                     self.Show()
                elif m == 2:
                    print("New subscriber")
                    self.AddKontakt()
                elif m == 3:
                    print("Removing subscriber")
                    self.DelKontakt()
                elif m == 4:
                    print("Search for a phone number by caller name")
                    phone = self.FindKey(input("Name: "))
                    if phone == "":
                        print("Subscriber is not in the contact list")
                    else:
                        print("phone number- " + phone)
                elif m == 5:
                    print("Search for a subscriber's name by phone number")
                    name = self.FindValue(input("Phone: "))
                    if name == "":
                        print("The subscriber is not in the contact list")
                    else:
                        print("The name of subscriber - " + name)
                else:
                    print("Goodbye!")
                    break

K = Kont()
K.Execute()

            
