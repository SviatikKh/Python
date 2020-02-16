import os
#Class of single consultant
#start of work - 9:00
#end of work - 18:00
#term of service of single client - 30 minutes
class Consultant:
    def __init__(self, filename):
        self.filename = filename    #name of file that contains hours of customer records for appointment
        self.data = []              #list of the rows of file
    
    #Reading of the data from file filename to the list
    def ReadFromFile(self):            
        lst = []
        if os.path.isfile(self.filename) == False:
            print('File is missing')
        else:      
            with open(self.filename) as file:
                for it in file:
                    #entry in the list of strings from the file without '\n'
                    lst.append(it.rstrip('\n'))
        return lst
    
    #Entry in the file
    def WriteToFile(self, lst):
        frecord = open(self.filename, 'wt')
        for item in lst:
            frecord.write(item + '\n')
        frecord.close()

    #Defining of the appointment time of the client
    def NextClient(self):
        #reading of the hours of appointment from the file
        ls = self.ReadFromFile()
        #amount of file rows (clients)
        count = len(ls)
        #time of appointment of the next client
        tim = ''
        #if it's the first client (file is empty), 
        #then the time of begining of the consultant's work is appointed
        if count == 0:
            #the time of reception of the client
            tim = '9:00'
        #if the client is not the first
        else:
            #the time of reception of the last client is appointed
            tim = ls[count - 1]
            #hours and minutes are highlited separatly in the line of the time
            hx = tim.split(':')
            #if minutes - '00', then - change to - '30'
            if hx[1] == '00':
                hx[1] = '30'
                tim = hx[0] + ':' + hx[1]
            #if minutes - '30'
            else:
                #1 is added to the hour
                f = int(hx[0]) + 1
                #if the hour is equal to 18, then client's appointment ends up
                if f == 18:
                    tim = ''   #sign of the end of the appointment
                #if the hour isn't equal to 18, then minutes are changed to '30'
                else:
                    hx[0] = str(f)
                    hx[1] = '00'
                    tim = hx[0] + ':' + hx[1]
        #if sign of the end of the appointment is equal to False
        if tim != '':
           ls.append(tim)
           #adding the record to the file
           self.WriteToFile(ls)
        #the time of an appointment of the next client returns
        #or an empty row, if an appointment is finished
        return tim

    #Display of the result of the client's appointment for appointment with a consultant
    def Show(self):
        t = self.NextClient()
        if t == '':
            print ('The registration of the clients is finished')
        else:
            print('You have been assigned to an appointment with a consultant - ' + t)

#The class of the list with consultants
class Centr(Consultant):
     def __init__(self):
         self.list_files = []         #the list of the file name of the tests
        
     #The forming of the list of the file names of consultants
     def List_Consultant(self):
         #current directory
         dir = os.path.abspath(os.curdir)
         #the list of the files of current directory
         files = os.listdir(dir)
         #the list of the files with extention txt
         self.list_files = []
         for item in files:
             ext = os.path.splitext(item)[1]
             if ext == '.txt':
                 self.list_files.append(item)

     #Selecting menu with consultants
     def Menu(self):
         self.List_Consultant()
         k = len(self.list_files)
         m = 0
         if k == 0:
             print("The list of the consultants is empty")
         else:
             y = False
             while y == False:
               try:
                   num = 0
                   for item in self.list_files:
                      num += 1
                      print(str(num) + '.' + item)
                   m = int(input('Enter № of the consultant: '))
                   y = m >= 1 and m <= k
                   if y == False:
                     print('Uncorrect № of the consultant')
               except:
                   print('Uncorrect № of the consultant')
         return m
     
     #Determining the time of appointment of the client from the consultant's menu is selected
     def Client(self):
         ls = [0, '']
         m = self.Menu()
         if m > 0:
             ls[0] = m
             self.filename = self.list_files[m - 1]
             ls[1] = self.NextClient()
         return ls   

     #Output of the assigned time of customer service
     def Show(self):
         ls = self.Client()
         s = self.list_files[ls[0] - 1]
         if ls[0] > 0 and ls[1] != '':
             print('You have been assigned to an appointment {0} with the consultant "{1}"'.format(ls[1], s))
             self.Diagrama()
         else:
             print('The registration of the client for an appointment to the consultant "{0}" failed'.format(s))
             

     #Chart construction
     def Diagrama(self):
         self.List_Consultant()
         k = len(self.list_files)
         #the list of the records (rows) ammount in the consultants files
         #lsk = []
         if k == 0:
             print("The list of consultants is empty")
         else:            
             for item in self.list_files:
                 self.filename = item
                 ls = self.ReadFromFile()
                 m = len(ls)
                 s = ''
                 if m > 0:
                     s = 'I' * m
                 print('{0:<20s} {1} ({2})'.format(item, s, m))

#K = Consultant('Кабінет1.txt')
#K.Show()

C = Centr()
C.Show()
#C.Diagrama()

