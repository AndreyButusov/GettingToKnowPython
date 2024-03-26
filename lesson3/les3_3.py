# Задача 17
# Дан список чисел. Определите, сколько в нем
# встречается различных(уникальных) чисел


# list_num = [1, 1, 2, 0, -1, 3, 4, 4]
# set_num = set()
# for i in list_num:
#     set_num.add(i)
# print(*set_num)
# print(len(set_num))


# Аналогичное решение

list_num = [1, 1, 2, 0, -1, 3, 4, 4]
num = set(list_num)
print(len(num))


# Аналогичное решение

# list_num = [1, 1, 2, 0, -1, 3, 4, 4]
# result_list = list()
# for i in list_num:      # для каждого элемента в list_num
#     if i not in result_list:
#         result_list.append(i)
# print(result_list)
# print(len(result_list))