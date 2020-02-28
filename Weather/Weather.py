import os
#клас одноразової реєстрації метеорологічних показників
class MetHour:    
    #Конструктор класу MetHour
    def __init__(self):
        self.temp = 0          #температура повітря
        self.press = 0         #атмосферний тиск
        self.humid = 0         #вологість повітря
        self.precip = 0        #ймовірність опадів
        self.speed_wind = 0    #швидкість вітру
        self.direct_wind = ['південний', 'північний', 'східний', 'західний']
   
    #Визначення напряму вітру
    def Wind(self):
        s = ''      #найменування напряму вітру
        n = int(input('Напрям вітру (південний (1), північний (2), східний (3), західний (4)): '))
        if n == 1 or n == 2 or n == 3 or n == 4:
            s = self.direct_wind[n - 1]
        else:
            print('Напрям вітру не визначено')
        return s

    #Формування кортежу даних про метеорологічні прказники
    def EnterData(self):
        self.temp   =      input('Температура повітря (град):   ')          
        self.press  =      input('Атмосферний тиск (мм.рт.ст.): ')
        self.humid  =      input('Вологість повітря (%):        ')         
        self.precip =      input('Ймовірність опадів (%):       ')        
        self.speed_wind  = input('Швидкість вітру (м/сек): ')   
        #визначення напряму вітру
        x = ''
        while x == '':
            x = self.Wind()
        #запис даних у кортеж
        data = []
        data.append(self.temp)          #(0-Температура повітря (град))
        data.append(self.press)         #(1-Атмосферний тиск (мм.рт.ст.))
        data.append(self.humid)         #(2-Вологість повітря (%))
        data.append(self.precip)        #(3-Ймовірність опадів (%))
        data.append(self.speed_wind)    #(4-Швидкість вітру (м/сек))
        data.append(x)                  #(5-Напрям вітру)
        return data
    
    #Виведення найменувань метеорологічних показників
    def ShowHead(self):
         print('{0:20s}'.format('Температура'), end = '')
         print('{0:20s}'.format('Атмосферний'), end = '')
         print('{0:20s}'.format('Вологість'), end = '')
         print('{0:20s}'.format('Ймовірність'), end = '')
         print('{0:20s}'.format('Швидкість'), end = '')
         print('{0:20s}'.format('Напрям'), end = '')
         print('{0:20s}'.format('повітря (град)'), end = '')
         print('{0:20s}'.format('тиск (мм.рт.ст.)'), end = '')
         print('{0:20s}'.format('повітря (%)'), end = '')
         print('{0:20s}'.format('опадів (%)'), end = '')
         print('{0:20s}'.format('вітру (м/сек)'), end = '')
         print('{0:20s}'.format('вітру'), end = '')

    #Виведення метеорологічних показників
    def ShowData(self, indicators):
        for i in range(6):
            print('{0:20s}'.format(str(indicators[i])), end = '')
        #print('\n')

    #Виконання операції реєстрації метеорологічних показників та їх виведення на екран
    def Execute(self):
        induc = self.EnterData()
        if len(induc) > 0:
            self.ShowHead()
            self.ShowData(induc)
        else:
            print('Помилки у вхідних даних')
        
#клас реєстрації метеорологічних показників за день
class MetDay(MetHour):    
    #Конструктор класу MetDay
    def __init__(self):
        self.count = 1     #кількість реєстрацій метеорологічних показників за день
        self.dic = {}      #словник метеорологічних показників за день
        #self.direct_wind = ['південний', 'північний', 'східний', 'західний']
        super().__init__()

    #Формування ключів словника - годин реєстрації метеорологічних показників за день
    def Hours(self):
        self.dic = {}      #список годин реєстрації метеорологічних показників за день
        n = int(input('Кількість реєстрацій метеорологічних показників за день (1, 2, 4, 6, 12, 24)'))
        if n == 1 or n == 2 or n == 4 or n == 6 or n == 12 or n == 24:
            step = 24 // n
            x = 0
            self.dic[x] = []
            for i in range(n - 1):
                x += step
                self.dic[x] = []
        else:
            print('Значення невірне')
        return self.dic

    #Формування списків метеорологічних показників за день
    def ListMet(self):
        m = len(self.Hours())
        if m > 0:
            list_keys = self.dic.keys()
            for key in list_keys:
                print(key)
                self.dic[key] = self.EnterData()
        return self.dic

    #Виведення метеорологічних показників за день
    def ShowDic(self):
        self.ShowHead()
        list_keys = self.dic.keys() 
        for key in list_keys:
            lst = self.dic[key]
            self.ShowData(lst)

    #Перевизначений метод
    #Виконання операції реєстрації метеорологічних показників у визначені години та їх виведення на екран
    def Execute(self):
        self.ListMet()
        print('\n')
        self.ShowDic()




#Перевірка роботи методів класу MetHour 
#H = MetHour()
#H.Execute()
#Перевірка роботи методів класу MetDay 
D = MetDay()
D.Execute()

