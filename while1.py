# Пройдите в цикле по списку ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"] пока не встретите имя "Валера".
# Когда найдете напишите "Валера нашелся". Подсказка: используйте метод list.pop()

names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

name_to_find = "Валера"

while True:
    try:
        name = names.pop()
        if name == name_to_find:
            print("{} нашелся".format(name_to_find))
            break
    except IndexError:
        print('{}? Я такого не знаю...'.format(name_to_find))
        break
