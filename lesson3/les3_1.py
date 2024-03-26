# Задача про среднесуточную температуру

day = int (input("Какое количество дней: "))

max_counter = 0
counter = 0

for _ in range(day):    #повторять day раз
    temp = int(input("Сегодня температура: "))
    if temp > 0:
        counter += 1
    else:
        counter = 0
    if counter > max_counter:
        max_counter = counter
print(max_counter)