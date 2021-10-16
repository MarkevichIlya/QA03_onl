#СПИСКИ
# 1. Создайте два любых списка и свяжите их с переменными.
element1 = [1, 2, 3, 4, 5]
element2 = [9, 8, 7, 6, 11]
print("первый список:", element1)
print("второй список:", element2)

# 2. Извлеките из первого списка второй элемент.
print("второй элемент первого списка:",  element2[1])

# 3. Измените во втором списке последний элемент. Выведите список на экран.
element2[-1] = 99
print("измененный второй список:", element2)

# 4. Соедините оба списка в один, присвоив результат новой переменной. Выведите получившийся список на экран.
double_element= element1 + element2
print ("двойной список:", double_element)

# 5. "Снимите" срез из соединенного списка так, чтобы туда попали некоторые части обоих первых списков. Срез свяжите с очередной новой переменной. Выведите значение этой переменной.
slice_element=double_element[int(len(double_element)/2-1):int(len(double_element)/2+1)]
print("срез из частей двух списков:", slice_element)

# 6. Добавьте в список два новых элемента и снова выведите его.
double_element.append( 105 )
double_element.append( 106 )
print("обновленный список:", double_element)

# 7. Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
#Нужно вернуть список, который состоит из элементов, общих для этих двух списков. -- !не использовать циклы
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=list(set(a)&set(b))
print("общие элементы двух списков:", c)

# 8. Есть список: [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3] оставить в нем только уникальные значения. !не использовать циклы

#Логические операции:
#1. Присвойте двум переменным любые числовые значения.
k=55
l=33
print("k=", k)
print("l=", l)
#2. Составьте четыре сложных логических выражения с помощью оператора and, два из которых должны давать истину, а два других - ложь.
print(k==55 and l==33)
print(k!=0 and l!=0)
print(k==33 and l==55)
print(k>=0 and l<=0)
#3. Аналогично выполните п. 2, но уже используя оператор or.
print(k==55 or l==33)
print(k!=0 or l!=0)
print(k==33 or l==55)
print(k<=0 or l<=0)
#4. Попробуйте использовать в сложных логических выражениях работу с переменными строкового типа.

#Словари:
#1. Создайте словарь, связав его с переменной school, и наполните его данными, которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).
school={ '1a':25, '1b':18, '1c':19, '1d':17}
print("словарь:", school)

#2. Узнайте сколько человек в каком-нибудь классе.
print("колличество человек в классе 1b=", school['1b'])
#3. Представьте, что в школе произошли изменения, внесите их в словарь:
#◦ в трех классах изменилось количество учащихся;
school['1a']=24
school['1b']=16
school['1с']=10
#◦ в школе появилось два новых класса;
school['1e'] = 20
#◦ в школе расформировали один из классов.
del school['1d']
#4. Выведите содержимое словаря на экран.
print("измененный словарь:", school)

