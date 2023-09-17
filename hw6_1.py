# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.


import sys
def _leap_year(year: int):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def data_check(a: str='01.01.0001'):
    data = [int(i) for i in a.split('.')]
    day, month, year = data
    if 1 <= year <= 9999:
        if 1 <= month <= 12:
            if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
                return True
            elif month in [4, 6, 9, 11] and 1 <= day <= 30:
                return True
            else:
                if _leap_year(year) is True and 1 <= day <= 29:
                    return True
                elif _leap_year(year) is False and 1 <= day <= 28:
                    return True
        return False
    return False

if __name__ == '__main__':
    # a = input('введите дату для проверки в формате дд.мм.гггг')
    a, *_ = sys.argv[1:]
    print(data_check(a))