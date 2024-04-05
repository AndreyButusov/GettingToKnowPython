# Задача 41.  Дан массив, состоящий из целых чисел. Напишите программу, 
# которая в данном массиве определит количество элементов, у которых 
# два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.


def create_arr(st1):
    return [int(input(f"Введите {i+1} элемент: ")) for i in range(int(input(st1)))]

def FindBigEl(st):
    count = 0
    for el in range(len(st)):
        if st[el] > st[el - 1] and st[el] > st[el - len(st) + 1]:
            count += 1
    return count

def recurs(st):
    if len(st) <= 2:
        return 0
    counter = 0
    if st[1] > st[0] and st[1] > st[2]:
        counter += 1
    return counter + recurs(st[1:])

ar = create_arr('Введите длину списка ')
print(ar)
print(FindBigEl(ar))
print(recurs(ar))
    