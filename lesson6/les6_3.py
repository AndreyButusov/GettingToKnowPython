# Задача 43. Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: 
# 1 2 3 2 3 
# Вывод:
# 2

import random

def CreateArr(num):
    return [random.randint(0, 10) for _ in range(num)]

arr = CreateArr(int(input('Введите длину ')))
print(arr)

def FindEl(arr):
    counter = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
               counter += 1 
    return counter

def recurs(arr):
    if len(arr) <= 1:
        return 0
    first_num = arr[0]
    rest_num = arr[1:]
    count = 0
    for i in rest_num:
        if first_num == i:
            count += 1
    return count + recurs(rest_num)
               
print('Количество пар классическим методом: ', FindEl(arr))
print('Количество пар методом рекурсии: ', recurs(arr))