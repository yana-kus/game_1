from hidden import *
import numpy as np
def replace_duplicates(s): # на вход строка
    alf="abcdefghijklmnopqrstuvwxyz"
    s=s.lower()# привели к нижнему
    if len(set(s)) == len(s):#возвращает логическое значение, True если строка не содержит повторяющихся символов, False в противном случае.
        return s

    for i in s:
        if s.count(i)>2 or s.count(i)==2:#проверка вхождений нужно 2 или больше
            s1=s.replace(i,'',2)# удалила 2 вхождения
            for b in alf:# находим букву в алфавите
                    if b=="z":# если последняя добавляем а
                        s1 += alf[0]
                    else:
                        index = alf.find(b)  # индекс искомой буквы в строке, добавляем следующую
                        s1+=alf[index+1]

    return replace_duplicates(s1)




print(replace_duplicates(s='hhakafh'))
