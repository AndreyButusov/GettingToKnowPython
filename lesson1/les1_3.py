class1 = int(input('Количество учащихся в первом классе: '))
class2 = int(input('Количество учащихся в втором классе: '))
class3 = int(input('Количество учащихся в третьем классе: '))
result = class1 // 2 + class1 % 2 + class2 // 2 + class2 % 2 + class3 // 2 + class3 % 2
print(f'Наименьшее число необходимых парт: {result}')