from datetime import date
import calendar

class MyDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    # визначення назви місяця українською мовою 
    def month_name(self, i):
        lst = ['сiчня', 'лютого', 'березня', 'квiтня', 'травня', 'червня', 'липня', 'серпня', 'вересня', 'жовтня',
               'листопада', 'грудня']
        result = 0
        if 0 < i <= 12:
            result = lst[i - 1]
        return result
    #визначення назви місяця українською мовою 
    def dayofweek_name(self, i):
        return{
            0: ['понедiлок', 'ПН'],
            1: ['вiвторок', 'ВТ'],
            2: ['середа', 'СР'],
            3: ['червер', 'ЧТ'],
            4: ["п'ятниця",'ПТ'],
            5: ['субота', 'СБ'],
            6: ['недiля', 'НД']
            }[i]
    #визначення кількості днів у місяці
    def dayofmonth(self, i):
        if calendar.isleap(self.year):
            d = 29
        else:
            d = 28
        lst = [31, d, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        result = 0
        if 0 < i <= 12:
            result = lst[i - 1]
        return result
    #контроль коректності дати
    def isdate(self):
        yy = 1900 < self.year < 2100
        #ym = 0 < self.month <= 12
        ym = self.month_name(self.month) != ''
        #yd = 0 < self.day <= self.dayofmonth(self.month)
        yd = self.dayofmonth(self.month) != 0
        return yy and ym and yd

    #формування рядку дати з повними назвами місяця та дня тижня українською мовою
    def dateUK(self):
        s = ''
        if (self.isdate()):
            data = date(self.year, self.month, self.day)
            #dwnum = data.weekday()
            #dwstr = self.dayofweek_name(dwnum) 
            #s = str(self.day) + ' ' + self.month_name(self.month) + ' ' + str(self.year) + ' року, ' + dwstr[0]
            s = str(self.day) + ' ' + self.month_name(self.month) + ' ' + str(self.year) + ' року, ' + self.dayofweek_name(data.weekday())[0]
        return s
    #формування рядку дати з короткими назвами місяця та дня тижня українською мовою
    def dateUKshort(self):
        s = ''
        if (self.isdate()):
            data = date(self.year, self.month, self.day)
            #mon = self.month_name(self.month)[0:3].upper()
            #s = str(self.day) + ' ' + mon + ' ' + str(self.year) + ', ' + self.dayofweek_name(data.weekday())[0]
            s = str(self.day) + ' ' + self.month_name(self.month)[0:3].upper() + ' ' + str(self.year) + ', ' + self.dayofweek_name(data.weekday())[1]
        return s
    #формування календаря
    def myCalendar(self):
         data = date(self.year, self.month, 1)  #дата першого дня місяця
         dwnum = data.weekday()                 #номер дня тижня першого дня місяця
         #перший рядок
         mn = []                                #список списків днів по тижнях
         tn = []                                #список днів
         cur = 0                                #лічильник днів місяця
         for d in range(0, dwnum):
             tn.append(' ')
         for d in range(dwnum, 7):
             cur +=1
             tn.append(cur)             
         mn.append(tn)                          #додавання списку днів 1-го тижня в список тижнів календаря
         #формування списків повних тижнів
         lastday = self.dayofmonth(self.month)  #останній день місяця
         rest = lastday - cur                   #кількість днів місяця без 1-го тижня
         fullweek = rest // 7                   #кількість повних тижнів
         restweek = rest % 7                    #кількість днів місяця в останньому тижні
         #
         for w in range(0, fullweek):
             tn = [] 
             for d in range(0, 7):
                 cur += 1
                 tn.append(cur)
             mn.append(tn)
         rest = lastday - cur                   #кількість днів місяця останньго тижня
         if rest > 0:
             tn = []
             for d in range(0, rest):
                 cur += 1
                 tn.append(cur)
             for d in range(rest, 7):
                 tn.append(' ')
             mn.append(tn)
         return mn
    #виведення календаря
    def show_calendar(self):
        mon = self.myCalendar()                 #формування календаря
        weeks = len(mon)                         #кількість тижнів у місяці
        print('\n') 
        for n in range(0, 7):
            print('\t{0}'.format(self.dayofweek_name(n)[1]), end = '')
        print('\n')
        for t in range(0, weeks):
            tn = mon[t]
            for d in range(0, 7):
                print('\t{0}'.format(tn[d]), end = '')
            print('\n')    


        

dat = MyDate(2019,12,31)
strdat = dat.dateUK()
if strdat == '':
    print ('Дата некоректна')
else:
    print(dat.dateUK())
    print(dat.dateUKshort())
dat.show_calendar()