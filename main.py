# # Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# #
# # Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
#
# add_odd_positions = input('введите элементы через пробел: ')
#
#
# def sum_of_positions(odd_positions):
#     count = 0
#     for i in range(len(odd_positions)):
#         odd_positions[i] = int(odd_positions[i])
#         if i % 2 != 0:
#             count += odd_positions[i]
#
#     return count
#
#
# print(sum_of_positions(add_odd_positions.split()))

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# count = int(input('сколько раз хотим пройти цикл? '))
# numbers = list(map(int, input('введите числа через пробел: ').split()))
# recording_number = 0
# if count % 2 != 0:
#     for count in range(len(numbers) // 2 + 1):
#         recording_number = numbers[count] * numbers[len(numbers) - count - 1]
#         print(recording_number, end=' ')
# elif count % 2 == 0:
#     for count in range(len(numbers) // 2):
#         recording_number = numbers[count] * numbers[len(numbers) - count - 1]
#         print(recording_number, end=' ')

# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# count = int(input('сколько раз хотим пройти цикл? '))
# numbers = []
# for i in range(count):
#     number = float(input())
#     numbers.append(number)
# maxx = 0
# minn = 1
# for el in numbers:
#     if '.' in str(el):
#         dr = str(el).split('.')[1]
#         if float('0.' + dr) > maxx:
#             maxx = float('0.' + dr)
#         elif float('0.' + dr) < minn:
#             minn = float('0.' + dr)
#
# print(maxx - minn)


# 1.1 1.2 3.1 5 10.01


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# number = int(input('введите число которое хотите перевести в двоичное: '))
# count = ''
# while number > 0:
#     count = str(number % 2) + count
#     number = number // 2
# print(count)

