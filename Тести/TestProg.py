import os
#Клас одного тесту
class Test:
    def __init__(self, filename):
        self.filename = filename    #ім'я файлу
        self.data = []              #список рядків файлу
        self.result = ''            #літери правильних відповідей
        self.custom = ''            #літери відповідей користувача  
        self.isWrong = True         #результат виконання тесту
    #Читання даних з файлу filename в список
    def ReadFromFile(self):            
        lst = []

        if os.path.isfile(self.filename) == False:
            print('Файл відсутній')
        else:      
            with open(self.filename) as file:
                for it in file:
                    #запис у список рядків з файлу без символу переведення рядку
                    lst.append(it.rstrip('\n'))
        return lst
    #Контроль коректності тесту:
    #кількість рядків у файлі повинна бути не менше 3 і не більше 10
    #1-й рядок - тестове завдання
    #кожний наступний рядок - варіант відповіді
    #рядок правильної відповіді повинен починатися з символу "+"
    #тест повинен містити хоча б одну правильну і одну неправильну відповідь
    def VerifyTest(self):
        #ознака коректності тесту
        y = True
        #читання тесту з файлу
        self.data = self.ReadFromFile()
        #кількість рядків у файлі тесту
        count = len(self.data)
        #перевірка коректності кількості рядків
        if count < 3 or count > 10:
           print('кількість рядків у файлі тесту некоректна')
           y = False
        #перевірка коректності кількості правильних відповідей
        else:
           plus = 0
           for i in range(1, count):
               if self.data[i][0] == '+':
                   plus += 1
           if plus == 0 or plus == count - 1:
               print('всі відповіді тесту правильні або неправильні')
               y = False
        return y
    #Виконання тесту
    def TestExecute(self):
        #завантаження файлу тесту, контроль його коректності
        y = self.VerifyTest()
        #кількість рядків у файлі тесту
        count = len(self.data)
        if not y:
            print('Тест некоректний')
        #відображення тесту без позначень правильних відповідей
        #збереження правильних відповідей у рядку result
        else:
            print('Тестове завдання:')
            print(self.data[0])
            print('Варіанти відповідей:')
            self.result = ''
            for i in range(1, count):
                if self.data[i][0] == '+':
                    self.result += self.data[i][1]
                    print(self.data[i][1:])
                else:
                    print(self.data[i])
            #введення відповідей користувачем
            self.custom = input('Введіть позначення правильних відповідей (без пробілів): ')
            #визначення результату тесту
            self.isWrong = self.custom == self.result
            #цей блок потім потрібно видалити або закоментарити
            #print('Правильні відповіді: ' + self.result)
            #if self.isWrong:
            #    print('Результат позитивний')
            #else:
            #    print('Результат негативний')

#Клас списку тестів 
class Testing(Test):
     def __init__(self):
         self.list_files = []         #список імен файлів тестів
         #self.data = []              #список рядків файлу
         self.list_result = []        #список правильних відповідей
         self.list_custom = []        #список відповідей користувача  
         self.test_result = 0.0       #результат тестування у відсотках
     
     #Формування списку файлів тестів
     def List_tests(self):
         #поточна директорія
         dir = os.path.abspath(os.curdir)
         #список файлів поточної директорії
         files = os.listdir(dir)
         #список файлів з розширенням txt
         self.list_files = []
         for item in files:
             ext = os.path.splitext(item)[1]
             if ext == '.txt':
                 self.list_files.append(item)
     
     #Обчислення результату тестування
     def User_result(self):
          res = 0 
          count = len(self.list_result)
          for i in range(count):
              if self.list_result[i] == self.list_custom[i]:
                  x = '+'
                  res += 1
              else:
                  x = '-'
              print(str(i + 1) + '.' + self.list_result[i] + '\t' + self.list_custom[i] + '\t' + x)
          #Обчислення результату тестування
          self.test_result = res / count * 100
          print('Результат тестування - {0:.1f}%'.format(self.test_result))
    
     #Виконання тестів
     def TestDialog(self):
         self.List_tests()
         count = len(self.list_files)
         if count == 0:
             print('Список файлів тестів порожній')
         else:
             #
             self.list_result = []       
             self.list_custom = [] 
             for i in range(count):
                 print('Тест №' + str(i + 1))
                 self.filename = self.list_files[i]
                 self.TestExecute()
                 self.list_result.append(self.result)
                 self.list_custom.append(self.custom)
             #визначення та відображення результатів тестування
             self.User_result()

#створення екземпляру класу одного тесту
#T = Test('2.txt')
#виконання одного тесту
#T.TestExecute()
########################################
#створення екземпляру класу тестування
TT = Testing()
TT.TestDialog()