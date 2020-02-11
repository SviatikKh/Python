class Student:
    def __init__(self):
        #прізвище ім'я по-батькові
        self.name = ''
        #список оцінок
        self.lst = []
    #true - всі оцінки "5"
    def is5(self):
        x = set(self.lst)
        y = x - {5}
        return len(y) == 0 
    #true - оцінки "4" і "5" і не відмінник
    def is45(self):
        x = set(self.lst)
        y = x - {4, 5}
        return len(y) == 0 and not self.is5()
    #true - оцінки "3", "4" і "5" і не відмінник і не хорошист
    def is345(self):
        x = set(self.lst)
        y = x - {3, 4, 5}
        return len(y) == 0 and not self.is45() and not self.is5()
    #true - є оцінки "2"
    def is2(self):
        x = set(self.lst)
        y = x & {2}
        return len(y) > 0
    #визначення статусу студента: A - відмінник, B - хорошист, C - трієчник, D - двієчник
    def status(self):
        s = ''
        if self.is5():
            s = 'A'
        if self.is45():
            s = 'B'
        if self.is345():
            s = 'C'
        if self.is2():
            s = 'D'
        return s
    #рейтинг (сума балів)
    def reitung(self):
        sum_bal = 0
        for x in self.lst:
            sum_bal += x
        return sum_bal
    #середній бал
    def mid_bal(self):
        sb = 0
        x = len(self.lst)
        if x != 0:
            sb = self.reitung() / x
        return sb
    #виведення рядку: прізвище, оцінки, середній бал, рейтинг
    def show(self):
        print('{0:<20s}'.format(self.name), end = '')
        for m in self.lst:
            print('{0:<10s}'.format(str(m)), end = '')
        print('{0:<10d}{1:<.1f}{2:>10s}'.format(self.reitung(), self.mid_bal(), self.status()))

####################################
class Group(Student):
    ####конструктор
    def __init__(self, group):
        #
        self.group = group
        #словник: прізвища студентів (ключі) та їх оцінки (значення-списки)
        self.dic = {}
    ####створення словника для заданого статусу студентів (stat)
    def Extraсt(self, stat):
        #створення словника даних про студентів заданого статусу
        dic_stat = {}
        #визначення списку студентів групи - ключів словника self.dic
        stud_name = list(self.dic.keys())
        #для кожного студента групи (item)
        for item in stud_name:
            #визначається прізвище студента (ключ словника self.dic)
            self.name = item
            #визначення списку оцінок студента - значень ключа словника self.dic
            self.lst = self.dic[item]
            #визначення статусу студента методом status() класу Student
            #якщо від відповідає заданому статусу stat, то в вихідний словник додається запис про студента
            if self.status() == stat:
                dic_stat[item] = self.lst
        #повертається словник з даними про студентів з заданим статусом
        return dic_stat
    ####виведення відомості оцінок для заданого статусу stat, для всіх статусів stat = ''
    def vidom(self, stat):
        #створення робочого словника для виведення відомості оцінок студентів заданого статусу
        dic_ved = {}
        #якщо stat є порожнім рядком, то це означає, що потрібно вивести відомість всієї групи
        #тоді робочому словнику присвоюється вхідний словник (атрибут класу Group)
        if stat == '':
            dic_ved = self.dic
        #якщо рядок stat є символом, що одначає відповідний сстатус студента
        #то в робочий словник методом Extract() класу Group записується словник з даними про студентів заданого статусу 
        else:
            dic_ved = self.Extraсt(stat)
        #якщо робочий словник виявиться порожнім, то формується відповідне повідомлення 
        if len(dic_ved) == 0:
            #визначається фрагмент повідомлення
            com = 'ВСІ'
            #якщо був заданий конкретний статус студента цей фрагмент замінюється на статус
            if stat != '':
                com = stat
            #виводиться повідомлення з визначеним фрагментом тексту
            print('статус ' + com + ' - дані відсутні')
        #якщо робочий словник не порожній
        else:
            #визначається список його ключів - прізвищ студентів
            stud_name = list(dic_ved.keys())
            #для кожного студента (item)
            for item in stud_name:
                #визначається його прізвище - ключ робочого словника
                self.name = item
                #за ключем визначається список оцінок студента
                self.lst = dic_ved[item]
                #після визначення потрібних атрибутів класу Student 
                #викликається його метод show для виведення рядку відомості
                self.show()               
        print('\n')
    ####визначення середнього балу по групі
    def mid_bal_group(self):
        #визначається список його ключів - прізвищ студентів
        stud_name = list(self.dic.keys())
        s_bal = 0
        count = len(self.dic)
        if count > 0:
           for item in stud_name:
                #визначається його прізвище - ключ робочого словника
                self.name = item
                #за ключем визначається список оцінок студента
                self.lst = self.dic[item]
                #після визначення потрібних атрибутів класу Student 
                #викликається його метод mid_bal для обчислення середнього балу студента
                x = self.mid_bal()
                #накопичується сума середніх балів студентів групи
                s_bal += x
           #сума середніх балів ділиться на кількість студентів
           s_bal /= count
        return s_bal
    ####визначення якості знань по групі в відсотках
    def quality_group(self):
        #визначення кількості відмінників і хорошистів
        countAB = len(self.Extraсt('A')) + len(self.Extraсt('B'))
        count_stud = len(self.dic)
        return countAB / count_stud * 100
    ####визначення успішності по групі
    def success_group(self):
        #визначення кількості двієчників
        countD = len(self.Extraсt('D')) 
        count_stud = len(self.dic)
        return (count_stud - countD) / count_stud * 100
    ####формування кортежу показників успішності по групі
    def indicators_group(self):
        cort = []
        #успішність (%)
        cort.append(self.success_group())
        #якість знань (%)
        cort.append(self.quality_group())
        #середній бал
        cort.append(self.mid_bal_group())
        #кількість відмінників
        cort.append(len(self.Extraсt('A')))
        #кількість хорошистів
        cort.append(len(self.Extraсt('B')))
        #кількість трієчників
        cort.append(len(self.Extraсt('C')))
        #кількість двієчників
        cort.append(len(self.Extraсt('D')))
        return cort
    ####виведення кортежу показників успішності по групі
    def show_indicators(self):
        crt = self.indicators_group()
        print('{0:<20s}'.format(self.group), end = '')
        for i in range(0, 3):
            print('{0:<15.1f}'.format(crt[i]), end = '')
        for i in range(3, 7):
            print('{0:<15d}'.format(crt[i]), end = '')
        print('\n')

####################################################################
class Faculty(Group):
    ####конструктор
    def __init__(self):
        #словник: назви груп (ключі) та дані про студентів (словники)
        self.dic_fc = {}
    ####відображення показників успішності по групах факультету
    def indicators_faculty(self):
        group_name = list(self.dic_fc.keys())
        for item in group_name:
            self.group = item
            self.dic = self.dic_fc[item]
            self.show_indicators()
    ####визначення середнього балу по факультету
    def mid_bal_faculty(self):
        m_bal = 0
        group_name = list(self.dic_fc.keys())
        for item in group_name:
            self.group = item
            self.dic = self.dic_fc[item]
            m_bal += self.mid_bal_group()
        return m_bal / len(group_name )
    ####визначення списків студентів (словники - студент:група) с заданим статусом по факультету
    def status_faculty(self, stat):
        #список груп
        group_name = list(self.dic_fc.keys())
        #
        dic_status = {}
        for item in group_name:
            self.group = item
            self.dic = self.dic_fc[item]
            #словник відмінників
            dic_stud = self.Extraсt(stat)
            #список ключів - прізвищ студентів
            stud_name = list(dic_stud.keys())
            for it in stud_name:
                dic_status[it] = item
        return dic_status
    ####відображення списків студентів та груп зі статусом stat
    def show_status_faculty(self, stat):
        dic_show = self.status_faculty(stat)
        stud_name = list(dic_show.keys())
        for item in stud_name: 
            print('{0:<20s} {1:<10s}'.format(item, dic_show[item]))
        print('\n')
    ####визначення кількості студентів на факультеті
    def studen_faculty(self):
        group_name = list(self.dic_fc.keys())
        count = 0
        for item in group_name:
            self.group = item
            self.dic = self.dic_fc[item]
            count += len(self.dic)
        return count
    ###визначення якості знань  по факультету в відсотках
    def quality_faculty(self):
        #визначення кількості відмінників і хорошистів
        countAB = len(self.status_faculty('A')) + len(self.status_faculty('B'))
        count_stud = self.studen_faculty()
        return countAB / count_stud * 100
    ####визначення успішності по факультету в відсотках
    def success_faculty(self):
        #визначення кількості двієчників
        countD = len(self.status_faculty('D')) 
        count_stud = self.studen_faculty()
        return (count_stud - countD) / count_stud * 100
###############################################################
#Відомість: дані зі словника
d = {
     'Tim': [5,5,4],
     'Den': [3,4,4],
     'Sem': [5,5,5],
     'Ket': [2,3,3],
     'Jon': [3,4,5]
    }
#########################################################
#створення об'єкту дочірнього класу
#g = Group('turist')
##передача параметрів (атрибутів) об'єкту
#g.dic = d
#виклик методу виведення відомості
#print('Повна відомість по групі: ' + g.group)
#g.vidom('')
#print('Відмінники в групі: ' + g.group)
#g.vidom('A')
#print('Хорошисти в групі: ' + g.group)
#g.vidom('B')
#print('Трієчники в групі: ' + g.group)
#g.vidom('C')
#print('Двієчники в групі: ' + g.group)
#g.vidom('D')
#print('Успішність   по групі складає {0:.1f}%'.format(g.success_group()))
#print('Якість знань по групі складає {0:.1f}%'.format(g.quality_group()))
#print('Середній бал по групі складає {0:.1f}'.format(g.mid_bal_group()))
#print('Показники успішності по групі: ')
#g.show_indicators()
#print('*'*100)
###########################################################
#словник груп факультету (ключі - назви груп, значення - словники даних про студентів групи
df = { 
      'bank':
        {
            'Tim' :[5,5,4],
            'Den' :[3,4,4],
            'Sem' :[5,5,5],
            'Ket' :[2,3,3],
            'Iren':[3,4,5]
        },
      'prog':
        {
            'Tom':[5,5,4,5],
            'Max':[3,4,4,3],
            'Fil':[5,5,5,5],
            'Jak':[2,3,3,4]
        },
      'comp':
        {
            'Cler'  :[5,5,4,5,4],
            'Sandra':[3,4,4,3,3],
            'Jon'   :[5,5,5,5,5]
        }      
    }
#список груп - ключів словника df
#group_name = list(df.keys())
#для кожної групи
#for item in group_name:
    #створюється екземпляр класу Group
#    gr = Group(item)
    #створюється словник даних про студентів групи
#    gr.dic = df[item]
    #виводиться на екран відомість
#    print('Повна відомість по групі: ' + gr.group)
#    gr.vidom('')
    #відображаються показники успішності
#    print('Показники успішності по групі: ')
#    gr.show_indicators()
#print('*'*100)
###########################################################
f = Faculty()
f.dic_fc = df
print('Показники успішності по групах: ')
print('{0:<20s}{1:<15s}{2:<15s}{3:<15s}{4:<15s}{5:<15s}{6:<15s}{7:<15s}'.
      format("Група", "Успішність", "Якість знань", "Середній бал", "Відмінники", "Хорошисти", "Трієчники", "Двієчники"))
f.indicators_faculty()
print('Відмінники:          Група')
f.show_status_faculty('A')
print('Хорошисти:           Група')
f.show_status_faculty('B')
print('Трієчники:           Група')
f.show_status_faculty('C')
print('Двієчники:           Група')
f.show_status_faculty('D')
print('Показники успішності по факультету: ')
print('Якість знань - {0:<.1f}%'.format(f.quality_faculty()))
print('Успішність   - {0:<.1f}%'.format(f.success_faculty()))
print('Середній бал - {0:<.1f}'.format(f.mid_bal_faculty()))
print('Відмінників  - {0:<5d}'.format(len(f.status_faculty('A'))))
print('Хорошистів   - {0:<5d}'.format(len(f.status_faculty('B'))))
print('Трієчників   - {0:<5d}'.format(len(f.status_faculty('C'))))
print('Двієчників   - {0:<5d}'.format(len(f.status_faculty('D'))))


