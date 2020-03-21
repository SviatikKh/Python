import os
#The class of single test
class ListCompare:
    def __init__(self):
        self.filenames = []            #the list of files
        self.voc = {}                   #dictionary results of comparing list items
        self.count_list = 0            #the number of files with the lists
        self.count_item = 0          #the number of items in the summary list
 
      #Forming a list of list files
    def List_Files(self):
        #current directory
        dir = os.path.abspath(os.curdir)
        #a list of the files of the current directory
        files = os.listdir(dir)
        #the list of the files with an extension txt
        for item in files:
            ext = os.path.splitext(item)[1]
            if ext == '.txt':
                self.filenames.append(item)
        self.count_list = len(self.filenames)
        return self.filenames
    
    #Reading data from a filename file into a list
    def ReadFromFile(self, filename):            
        lst = []
        if os.path.isfile(filename) == False:
            print('File is missing')
        else:      
            with open(filename) as file:
                for it in file:
                    #entry in the list of strings from the file without newline
                    lst.append(it.rstrip('\n'))
        return lst

    #Modeling of a dictionary from all items lists
    def FillVoc(self):
        #modelling of the files list 
        self.List_Files()
        #in the cycle by items in the file list
        for file in self.filenames:
            #reading the list of file 'file'
            lst = self.ReadFromFile(file)
            #in the cycle by the elements of the downloaded list
            for item in lst:
                #if the list item is already in the dictionary
                if item in self.voc:
                    #a file name is added to the list of the valuses of key 
                    ls = self.voc[item]
                    ls.append(file)
                #if the list item is not in the dictionary
                else:
                    ls = []
                    ls.append(file)
                    self.voc[item] = ls
        self.count_item = len(self.voc)
        return self.voc

    #Dictionary output
    def ShowVoc(self):
        lk = list(self.voc.keys())
        lk.sort()
        for item in lk:
            print('{0:<20s}{1}'.format(item, self.voc[item]))
    
    #Displaying dictionary items with a filter  
    def ShowVocFiltr(self, f):
        lk = list(self.voc.keys())
        lk.sort()
        count = 0
        for item in lk:
            if len(self.voc[item]) == f:
                print('{0:<20s}{1}'.format(item, self.voc[item]))
                count += 1
        return count

    #Searching of an item in the lists
    def Find(self, name):
        lk = list(self.voc.keys())
        if name in  list(self.voc.keys()):
            print(self.voc[name])
        else:
            print("Item" + name + "is not on any of the lists")
    
    #Making comparisons of the list items
    def Execute(self):
        self.FillVoc()
        print("Number of lists - " + str(self.count_list))
        print("Dictionary with the list items (without repetition)")
        self.ShowVoc()
        print("The dictionary items, which are contained in the only one of the lists")
        self.ShowVocFiltr(1)
        print("The dictionary items, which are contained simultaneously in all lists")
        self.ShowVocFiltr(self.count_list)
        while True:
            el = input("Search an item (Enter - exit): ")
            if el == "":
                break
            else:
                self.Find(el)

#Creating a class instance
LC = ListCompare()
#Calling a method of the performing operations in the lists
LC.Execute()