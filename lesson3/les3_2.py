# Задача
# Выбор арбуза для себя и для тещи (себе потяжелее, теще - полегче)
# На вход дается N - количество арбузов

# watermelon = int(input("Количество арбузов: "))
# for i in range(watermelon):
#     weight = int(input("Вес: "))
#     if i == 0:
#         min_num = weight
#         max_num = weight
#         continue
#     if weight < min_num:
#         min_num = weight
#     elif weight > max_num:
#         max_num = weight
# print(min_num, "теще")
# print(max_num, "нам")

# Аналогичное решение

n = int(input("Введите число арбузов: "))
arr = [int(input()) for _ in range(n)]
print("Мой арбуз весит: ", max(arr))
print("Арбуз для тёщи весит: ", min(arr))