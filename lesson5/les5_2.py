# Задача 2. 
# Хакер Василий получил доступ к классному журналу и хочет заменить все 
# свои минимальные оценки на максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

score = [1, 3, 3, 3, 4]

def revers(grades):
    list1 = []
    for grade in grades:
        if grade == max(grades):
            list1.append(min(grades))
        else:
            list1.append(grade)
    return list1

print(revers(score))