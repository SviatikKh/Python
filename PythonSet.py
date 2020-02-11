import random

#Створення списку count елементів - псевдовипадкових чисел у діапазоні [left, right]
def ListRandom(left, right, count):
    lst = []
    for num in range(0, count):
        lst.append(random.randint(left, right))
    lst.sort
    return lst

#Створення множини чисел, що зустрічаються (ins=true) або не зустрічаються (ins=false) в списку lst
def SetRandom(lst, left, right, ins):
    s = set(lst)
    if ins == False:
        fulllist = []
        for num in range(left, right + 1):
            fulllist.append(num)
        sf = set(fulllist)
        s = sf - s
    return s

#Виведення на екран списку, множини
def Show(result, caption):
    print(caption)
    for it in result:
        print(it, end = '  ')
    print('\n')

#Виведення на екран словника
def ShowDic(result, caption):
    print(caption)
    lkeys = ()
    lkeys = result.keys()
    for it in lkeys:
        print(str(it) + '\t' + str(result[it]))

#Формування словника - ключі - псепдовипадкові числа, значення - їх кількість у списку
def DicRandom(left, right, count):
    dic = {}
    lx = ListRandom(left, right, count)
    Show(lx, 'Cписок псевдовипадкових чисел')
    sy = SetRandom(lx, left, right, True)
    Show(sy, 'Множина наявних псевдовипадкових чисел')
    sv = SetRandom(lx, left, right, False)
    Show(sv, 'Множина вiдсутнiх псевдовипадкових чисел')
    for item in sy:
        dic[item] = lx.count(item)
    return dic

lt = int(input('Лiва границя iнтервалу            '))
rt = int(input('Права границя iнтервалу           '))
ct = int(input('Довжина вибiрки (к-ть елементiв): '))
#Виклик функції створення списку псевдовипадкових чисел  
#lr = ListRandom(0, 10, 10)
#Show(lr, 'Cписок псевдовипадкових чисел')
#
#sr = SetRandom(lr, 0, 10,  True) 
#Show(sr, 'Множина наявних псевдовипадкових чисел')
#
#sr = SetRandom(lr, 0, 10, False) 
#Show(sr, 'Множина вiдсутнiх псевдовипадкових чисел')
#
dc = DicRandom(lt, rt, ct)
ShowDic(dc, 'Псевдовипадковi числа та їх кiлькiсть')

