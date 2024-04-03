# Задача 1. Напишите функцию f, которая на вход принимает два числа a и b, 
# и возводит число a в целую степень b с помощью рекурсии. 
# Функция не должна ничего выводить, только возвращать значение.
# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8

# def step(a, b):
#     if b == 0:
#         return 1
#     else:
#         return a * step(a, b - 1)

# print(step(2, 3))



# Задача 2. Напишите рекурсивную функцию `sum(a, b)`, возвращающую сумму двух 
# целых неотрицательных чисел. Из всех арифметических операций допускаются 
# только `+1` и `-1`. Также нельзя использовать циклы.
# Функция не должна ничего выводить, только возвращать значение.
# Пример: sum(2, 2)  ⇒   4

def sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    return 2 + sum(a - 1, b - 1)

print(sum(16, 4))