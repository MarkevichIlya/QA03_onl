import random
import math

# 1) a = 10, b=23, поменять значения местами, чтобы в переменную “a” было записано значение “23”, в “b” - значение “-10”
a = 10
b = 23
a, b = b, -a
print("a =", a, "b =", b)
# 2) значение переменной “a” увеличить в 3 раза, а значение “b” уменьшить на 3
a = a * 3
b = b - 3
print(a, b)

# 3) преобразовать значение “a” из целочисленного в число с плавающей точкой (float), а значение в переменной “b”
# в строку
a = float(a)
b = str(b)
print(a, type(a), b, type(b))

# 4) Разделить значение в переменной “a” на 11 и вывести результат с точностью 3 знака после запятой
print(round(a / 11, 3))

# 5) Преобразовать значение переменной “b” в число с плавающей точкой и записать в переменную “c”.
# Возвести полученное число в 3-ю степень.
b = float(b)
c = b ** 3
print(c)
# 6) Получить случайное число, кратное 3-м Получить случайное число, кратное 3-м
rand_num = (random.randrange(0, 1000000, 3))
# rand_num = random.random() * 3
print(rand_num)

# 7) Получить квадратный корень из 100 и возвести в 4 степень
print(math.sqrt(100) ** 4)

# 8) Строку “Hi guys” вывести 3 раза и в конце добавить “Today” “Hi guysHi guysHi guysToday”
print('Hi guys' * 3 + 'Today')

# 9) Получить длину строки из предыдущего задания
print(len('Hi guys' * 3 + 'Today'))

# 10) Взять предыдущую строку и вывести слово “Today” в прямом и обратном порядке
line_1 = 'Hi guys' * 3 + 'Today'
print(line_1[21:26])
print(line_1[:20:-1])

# 11) “Hi guysHi guysHi guysToday” вывести каждую 2-ю букву в прямом и обратном порядке
print(line_1[1::2])
print(line_1[::-2])

# 12) Используя форматирования подставить результаты из задания 10 и 11 в следующую строку
# “Task 10: <в прямом>, <в обратном> Task 11: <в прямом>, <в обратном>”
f_1 = line_1[21:26]
f_2 = line_1[:20:-1]
f_3 = line_1[1::2]
f_4 = line_1[::-2]
string_1 = 'Task 10: {}, {} Task11: {}, {}'.format(f_1, f_2, f_3, f_4)
print(string_1)

# 13) Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте ваше имя.
name = "Anton"
print("my name is name".replace("name", name).replace(name, "name", 1))

# 14) Полученную строку в задании 12 вывести:
# а) Каждое слово с большой буквы
# б) все слова в нижнем регистре
# в) все слова в верхнем регистре
print(string_1.title())
print(string_1.upper())
print(string_1.lower())

# 15) Посчитать сколько раз слово “Task” встречается в строке из задания 12
print(string_1.count('Task'))