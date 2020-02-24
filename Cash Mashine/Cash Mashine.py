
#  *************    ATM    ********** #

class Operations:
    def __init__(self):
        self.data = {}            #dictionary - banknotes at similar ATMs
        self.count = 0            #the amount of money in an ATM
        self.state = False        #ATM status
        self.card = ''            #№ of customer card - test
        self.money = 0            #the amount ordered by the customer

    #Calculating the amount of money in an ATM
    def CalkMoney(self):
        self.count = 0
        lst = self.data.keys()
        for item in lst:
            x = self.data[item]
            self.count += item * x
        return self.count

    #Status determination of ATM
    def IsReady(self):
        self.state = self.count > 0
        if self.state == False:
            print("The banknote deposit is empty")
        return self.state
    
    #Replenishment of ATM deposit with banknotes
    def EnterData(self):
        self.data = {}
        x = int(input("1000 - "))
        self.data[1000] = x
        x = int(input("500  - "))
        self.data[500] = x
        x = int(input("200  - "))
        self.data[200] = x
        x = int(input("100  - "))
        self.data[100] = x
        self.count = self.CalkMoney()
        return self.data

    #Data output about the current status of money in an ATM
    def Show(self):
        print('The amount of money in an ATM - ' + str(self.count))
        lst = self.data.keys()
        for item in lst:
            print ('amount of denominations of {0} UAH  - {1}'.format(item, self.data[item]))
        self.IsReady()

    #Determination of the denominations and the number of notes in the amount ordered by the client
    def Banknotes(self):
        lst = self.data.keys()      #denominations of notes - dictionary keys
        sum = {}                    #dictionary - the number of denominations of each of the denominations in the sum
        mon = self.money            #working variable - the amount of money ordered by the client that will change in the cycle
        for item in lst:            #cycle at denominations of ATM deposit bills
            x = mon // item         #required number of banknotes of denomination item 
            y = self.data[item]     # the number of denominations of banknotes available in the ATM store of item
            if x > y:               #If the required number of notes exceeds available, then
                x = y               #the amount of banknotes available in the ATM storage is included in the amount
            sum[item] = x           #entry in the dictionary of the number of denominations of item in the amount of the client
            mon -= x * item         #the balance of the amount
        if mon > 0:                 #if the amount ordered by the customer was not collected then
            print('Missing denominations of the required banknotes in the ATM store')
            sum.clear()             #an empty dictionary will return
        else:
            for item in lst:
                self.data[item] -= sum[item]    #reducing the number of notes in the ATM store
                self.count = self.CalkMoney()
        return sum
    
    #Dialogue with the client
    def EnterSum(self):
        self.money = 0
        y = False
        while y == False:
             try:
                 mon = int(input('Enter the desired amount: '))
                 if mon > self.count:
                    print('There is not enough money in the ATM storage. There is ' + str(self.count) + 'UAH')
                 elif mon % 100 != 0:
                    print('The amount must be a multiple of 100')
                 else:
                     self.money = mon
                     y = True
             except:
                 print('Incorrect data format')
        return self.money
 
    #Customer service
    def Client(self):
        self.EnterSum()
        sum_client = self.Banknotes()
        if len(sum_client) > 0:
            s = 'Issued amount = '
            for item in sum_client.keys():
                if sum_client[item] > 0:
                    s += str(item) + '*' + str(sum_client[item]) + '+'
            s = s[0: len(s) - 1]
            s += "=" + str(self.money)
            print(s)

class WorkBankomat(Operations):

    def Execute(self):
        self.IsReady()
        if self.state == False:
            self.EnterData()
            print('****in the ATM storage - ' + str(self.count) + 'UAH')
            self.IsReady()
        while self.state == True:
             y = input('Insert the card (k) / Turn off the ATM (v) ')
             if y == 'k':
                self.Client() 
                print('****in the ATM storage - ' + str(self.count) + 'UAH')
                self.IsReady()
             else:
                break

#Op = Operations()
#Op.EnterData()
#Op.Show()
#Op.Client()
#Op.Show()

W = WorkBankomat()
W.Execute()

