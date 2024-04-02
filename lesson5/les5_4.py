# Зачада 37. Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def revers_values(N):
#     num = input("введите число: ")
#     if N == 1:
#         return num
#     return revers_values(N - 1) + num

# print(revers_values(3))


# Второе решение 

def reverse(arr):
    if len(arr) > 0:
        print(arr[-1], end=" ")
        reverse(arr[:-1])
    pass
n = [3, 4, 5, 7]
reverse(n)