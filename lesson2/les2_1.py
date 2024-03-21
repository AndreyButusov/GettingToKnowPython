# Вычисление факториала

Num = int(input('Введите число: '))
fact = 1
while Num > 1:
    fact *= Num
    Num -= 1
print(fact)