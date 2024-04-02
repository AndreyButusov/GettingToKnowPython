# Задача 35. Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым 
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


# def IsSimple(num):
#     if num % 2 == 0:
#         return 'no'
#     for i in range(3, num // 2, 2):
#         if num % i == 0:
#             return 'no'
#     return 'yes'

# print(IsSimple(17))

def simple_number(number, dev = 2):
    if number == dev:
        return 'yes'
    if number % dev == 0:
        return 'no'
    return simple_number(number, dev + 1)
print(simple_number(3))