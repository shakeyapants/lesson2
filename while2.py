# Перепишите предыдущий пример в виде функции find_person(name), которая ищет имя в списке.

lst = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]


def find_person(name):
    while True:
        item = lst.pop()
        if item == name:
            print(name + ' нашелся')
            break

find_person('Маша')