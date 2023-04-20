"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число
pr_min=1
pr_max=101
# количество попыток
count = 0

while True:
    count+=1
    predict_number = int(input("Угадай число от 1 до 100: "))
    print("num",number)
    
    if predict_number > number:
        pr_max=predict_number
        print(f"Число должно быть меньше! Рекомендуем ввести: {round((pr_min+pr_max)/2)}")

    elif predict_number < number:
        pr_min=predict_number
        print(F"Число должно быть больше! Рекомендуем ввести:{round((pr_min+pr_max)/2)}")
    
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break #конец игры выход из цикла


print(f"Вы угадали число {number} за {count} попыток.")