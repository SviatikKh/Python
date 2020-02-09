class Student:
    #Конструктор
    def __init__(self):
        self.name = ''
        self.lst = []

   #Чи відмінник
    def is5(self):
        x = set(self.lst)
        y = x - {5}
        return len(y) == 0

    #Оцінки 4, 5
    def is45(self):
        x = set(self.lst)
        y = x - {4, 5}
        return len(y) == 0 and not self.is5()

    #Оцінка 3
    def is345(self):
        x = set(self.lst)
        y = x - {3, 4, 5}
        return len(y) == 0 and not self.is45() and not self.is5()

    #Двійочник
    def is2(self):
        x = set(self.lst)
        y = x & {2}
        return len(y) > 0

    #Статус студента
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

     #Сума балів
    def reitung(self):
        sum_bal = 0
        for x in self.lst:
            sum_bal += x
        return sum_bal
    
    #Середній бал
    def mid_bal(self):
        sb = 0
        x = len(self.lst)
        if x != 0:
            sb = self.reitung() / x
        return sb

    #Виведення
    def show(self):
        print('{0:<10s}'.format(self.name), end = '')
        for m in self.lst:
            print('{0:<10s}'.format(str(m)), end = '')
        print('{0:<10d}{1:<.1f}{2:>10s}'.format(self.reitung(), self.mid_bal(), self.status()))


class Group(Student):
    def __init__(self):
        self.dict = {}

    def vidom(self):
        stud_name = list(self.dict.keys())
        for item in stud_name:
            self.name = item
            self.lst = self.dict[item]
            self.show()





#s = Student('Tim')
#s.lst = [5, 5, 4]
#s.show()

d = {
        'Tim':[5, 5, 5, 4],
        'Den':[3, 3, 4, 4],
        'Sem':[5, 5, 5, 5],
        'Ket':[2, 2, 3, 3],
        'Jon':[3, 3, 4, 5]
    }

#Список ключів
#stud_name = list(d.keys())
#В циклі по кількості студентів(елементів списку ключів словника d)
#for item in stud_name:
    #створення об*єкта з іменем ключів
    #obj = Student()
    #obj.name = item
    #obj.lst = d[item]
    #виведення ключа
    #obj.show()

g = Group()
g.dict = d
g.vidom()



