# 1. Создайте список, состоящий из четырех строк. Затем, с помощью цикла for, выведите строки поочередно на экран.

stih = ['Гроза прошла, и ветка белых роз','В окно мне дышит ароматом…','Еще трава полна прозрачных слез,','И гром вдали гремит раскатом.']
for i in stih:
    print(i)

print('\n')

# 2. Измените предыдущую программу так, чтобы в конце каждой буквы строки добавлялось тире и выведите это на экран.
#  (Подсказка: цикл for может быть вложен в другой цикл.)

for i in stih:
    for j in i:
        print(j, end='-')

print('\n')
# 3. Создайте список, содержащий элементы целочисленного типа, затем с помощью цикла перебора (list comprehension)
# измените тип данных элементов на числа с плавающей точкой. (Подсказка: используйте встроенную функцию float().)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = [float(i) for i in list]

print('\n',list)
print(new_list)