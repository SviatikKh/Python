#Порівняння сусідніх чисел
def CompareNear(ls):
    s = str(ls[0])
    for i in range(1,len(ls)):
        if ls[i-1] == ls[i]:
            s += '-' + str(ls[i])
        else:
            s += ' ' + str(ls[i])
    return s

#GГоризонтальне порівняння
def CompareGor(ls1, ls2, ls3):
    res = []
    res.append(CompareNear(ls1))
    res.append('')
    res.append(CompareNear(ls2))
    res.append('')
    res.append(CompareNear(ls3))
    return res

#Вертикальне порівняння
def CompareVert(ls1, ls2, ls3):
    res = []
    #Формування рядків з елементів списку
    s1 = str(ls1[0])
    s2 = str(ls2[0])
    s3 = str(ls3[0])
    for i in range (1, len(ls1)):
        s1 += ' ' + str(ls1[i])
        s2 += ' ' + str(ls2[i])
        s3 += ' ' + str(ls3[i])
    #Рядок результатів порівняння першого і другого списків
    sr1 = ''
    for i in range(0, len(ls1)):
        if ls1[i] == ls2[i]:
            sr1 += '| '
        else:
            sr1 += '  '
 #Рядок результатів порівняння другого і третього списків
    sr2 = ''
    for i in range(0, len(ls1)):
        if ls2[i] == ls3[i]:
            sr2 += '| '
        else:
            sr2 += '  '
    res.append(s1)
    res.append(sr1)
    res.append(s2)
    res.append(sr2)
    res.append(s3)
    return res

#Порівняння по лівій діагоналі
def CompareLeft(ls1, ls2, ls3):
    res = []
    #Формування рядків з елементів списку
    s1 = str(ls1[0])
    s2 = str(ls2[0])
    s3 = str(ls3[0])
    for i in range (1, len(ls1)):
        s1 += ' ' + str(ls1[i])
        s2 += ' ' + str(ls2[i])
        s3 += ' ' + str(ls3[i])
    #Рядок результатів порівняння першого і другого списків
    sr1 = ' '
    for i in range(0, len(ls1) - 1):
        if ls1[i] == ls2[i + 1]:
            sr1 += '\\ '
        else:
            sr1 += '  '
    #Рядок результатів порівняння другого і третього списків
    sr2 = ' '
    for i in range(0, len(ls1)- 1):
        if ls2[i] == ls3[i+1]:
            sr2 += '\\ '
        else:
            sr2 += '  '
    res.append(s1)
    res.append(sr1)
    res.append(s2)
    res.append(sr2)
    res.append(s3)
    return res

#Порівняння по правій діагоналі
def CompareRight(ls1, ls2, ls3):
    res = []
    #Формування рядків з елементів списку
    s1 = str(ls1[0])
    s2 = str(ls2[0])
    s3 = str(ls3[0])
    for i in range (1, len(ls1)):
        s1 += ' ' + str(ls1[i])
        s2 += ' ' + str(ls2[i])
        s3 += ' ' + str(ls3[i])
    #Рядок результатів порівняння першого і другого списків
    sr1 = ' '
    for i in range(0, len(ls1) - 1):
        if ls1[i+1] == ls2[i]:
            sr1 += '/ '
        else:
            sr1 += '  '
 #Рядок результатів порівняння другого і третього списків
    sr2 = ' '
    for i in range(0, len(ls1)- 1):
        if ls2[i+1] == ls3[i]:
            sr2 += '/ '
        else:
            sr2 += '  '
    res.append(s1)
    res.append(sr1)
    res.append(s2)
    res.append(sr2)
    res.append(s3)
    return res

#Загальна картинка
def CompareFull(ls1, ls2, ls3):
    res = []
    #Формування рядків з елементів списку
    s1 = CompareNear(ls1)
    s2 = CompareNear(ls2)
    s3 = CompareNear(ls3)
   
    #довжина списків
    lstlen = len(ls1)

    sr1 = ''
    for i in range(0, len(ls1)):
        if ls1[i] == ls2[i]:
            sr1 += '|'
        else:
            sr1 += ' '
        sr = ' '
        if (i < lstlen -1) and (ls1[i] == ls2[i+1]):
            sr ='\\'
        #якщо і-й елемент першого списку не останній
        #i i-й елемент першого списку дорівнює (i+1)-му елементу другого списку
        if (i < lstlen -1) and (ls1[i + 1] == ls2[i]):
            if sr == '\\':
                sr = 'X'
            else:
                sr ='/'
        sr1 += sr

    sr2 = ''
    for i in range(0, len(ls1)):
        if ls2[i] == ls3[i]:
            sr2 += '|'
        else:
            sr2 += ' '
        sr = ' '
        if (i < lstlen -1) and (ls2[i] == ls3[i+1]):
            sr ='\\'
        #якщо і-й елемент другого списку не останній
        #i i-й елемент першого списку дорівнює (i+1)-му елементу третього списку 
        if (i < lstlen -1) and (ls2[i + 1] == ls3[i]):
            if sr == '\\':
                sr = 'X'
            else:
                sr ='/'
        sr2 += sr

    res.append(s1)
    res.append(sr1)
    res.append(s2)
    res.append(sr2)
    res.append(s3)
    return res
#Виведення списку на екран
def PrintList(lst, cap):
    print(cap)
    for item in lst:
        print(item)
    print('\n')

#++++++++++++++++++++++++++
lst1 = [1, 2, 3, 7, 6, 5]
lst2 = [2, 1, 2, 6, 7, 5]
lst3 = [1, 3, 2, 2, 8, 7]
PrintList(CompareGor(lst1, lst2, lst3), 'Горизонтальне порівняння')
PrintList(CompareVert(lst1, lst2, lst3), 'Вертикальне порівняння')
PrintList(CompareLeft(lst1, lst2, lst3), 'Порівняння по лівій діагоналі')
PrintList(CompareRight(lst1, lst2, lst3), 'Порівняння по правій діагоналі')
PrintList(CompareFull(lst1, lst2, lst3), 'Результат порівняння елементів списку')


