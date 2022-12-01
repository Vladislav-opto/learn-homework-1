"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def string_comparison(string1, string2):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if not isinstance(string1, str) or not isinstance(string2, str):
        return 0
    elif len(string1) == len(string2):
        return 1
    elif len(string1) > len(string2):
        return 2
    elif (len(string1) != len(string2)) and string2 == 'learn': 
        return 3


if __name__ == "__main__":
    result = string_comparison("123", "learn")
    print(result)
    result = string_comparison(1, "python")
    print(result)
    result = string_comparison("qwerty", "qwerty")
    print(result)
