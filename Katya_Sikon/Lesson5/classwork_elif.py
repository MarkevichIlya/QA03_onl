# 1. Напишите программу по следующему описанию:
# a. двум переменным присваиваются числовые значения;
# b. если значение первой переменной больше второй, то найти разницу значений переменных (вычесть из первой вторую), результат связать с третьей переменной;
# c. если первая переменная имеет меньшее значение, чем вторая, то третью переменную связать с результатом суммы значений двух первых переменных;
# d. во всех остальных случаях, присвоить третьей переменной значение первой переменной;
# e. вывести значение третьей переменной на экран.

print('Введите 2 целых числа ')
a = int(input())
b = int(input())
c = 0

if a > b:
    c = a - b
elif a < b:
    c = a + b
else:
    c = a
print(c)

# 2. Придумайте программу, в которой бы использовалась инструкция if-elif-else. Количество ветвей должно быть как минимум четыре

print('Введите возраст')
age = int(input())

if 0 < age < 18:
    print('Детский возраст')
elif 18 <= age < 44:
    print('Молодой возраст')
elif 45 < age < 59:
    print('Средний возраст')
elif 60 < age < 74:
    print('Пожилой возраст')
elif 75 < age < 90:
    print('Старческий возраст')
elif 90 <= age:
    print('Долголетие')
else:
    print('некорректное значение возраста')