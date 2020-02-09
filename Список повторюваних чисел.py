def rep(n):
  number = 0      #начало отсчета
  result = ''     #cтрока результата 
  while True:
    number += 1
    s = str(number) * number    #повтор цифры
    len_current = len(result)   #текущая длина строки
    len_rest = n - len_current
    mm = len(s)                 #длина добавляемого фрагмента
    if mm > len_rest:
      result += s[0:len_rest]
      break
    else:
      result += s
  return result

print(rep(20)) 