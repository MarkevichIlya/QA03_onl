# Написать функцию, которая вычисляет банковский вклад
# Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых
# (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада,
# и на них в следующем году тоже будут проценты).
# Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.

def bank(a, years):
    """
    Функция вычисляет банковский вклад:
    Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых
    (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада,
    и на них в следующем году тоже будут проценты).

    :param a: первоначальный вклад
    :param years: срок вклада
    :return: сумма в коце срока
    """
    sum = a
    i = 0
    for i in range(0, years):
        sum = 1.1 * sum
    return round(sum, 2)


def count_deposit():
    a = float(input('Введите размер первоначального взноса: '))
    years = int(input('Введите срок вклада в годах: '))
    print('Сумма в конце срока: ', bank(a, years))

count_deposit()