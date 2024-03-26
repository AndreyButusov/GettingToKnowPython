# Задача 21. 
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)


mass = [0, -1, 5, 2, 3]
count = 0
for i in range(len(mass)-1):
    if mass[i] < mass[i + 1]:
        count +=1
print(count)



# Аналогичное решение

# mass = [0, -1, 5, 2, 3]
# count = 0
# for i in range(1, len(mass)):
#     if mass[i] > mass[i - 1]:
#         count +=1
# print(count)