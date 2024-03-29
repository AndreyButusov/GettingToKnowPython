# Задача
# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально. Пользователь его не вводит

# # Входные данные
# data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# # Создаем множество для хранения уникальных значений
# unique_values = set()
# # Проходим по каждому словарю в списке
# for dictionary in data:
#     # Проходим по каждому значению в словаре
#     for value in dictionary.values():
#         # Добавляем значение в множество
#         unique_values.add(value.strip())
# # Выводим уникальные значения
# print(unique_values)



# Аналогичное решение

dc = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII":" S007 "}]
print({list(slovar.values())[0].strip() for slovar in dc})