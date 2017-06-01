# Перепишите предыдущий пример в виде функции find_person(name), которая ищет имя в списке.

names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]


def find_person(name_to_find, list_names):
    while True:
        try:
            item = list_names.pop()
            if item == name_to_find:
                print('{} нашелся'.format(name_to_find))
                break
        except IndexError:
            print('{}? Я такого не знаю...'.format(name_to_find))
            break

if __name__ == '__main__':
    find_person('Денис', names)