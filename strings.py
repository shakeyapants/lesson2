# Написать функцию, которая принимает на вход две строки.
# Если строки одинаковые, возвращает 1.
# Если строки разные и первая длиннее, возвращает 2.
# Если строки разные и вторая строка 'learn', возвращает 3.


input1 = input('Please enter sth: ')
input2 = input('Please enter sth one more time: ')


def strings(input1, input2):
    if input1 == input2:
        return 1
    elif len(input1) > len(input2):
        return 2
    elif input2 == 'learn':
        return 3

print(strings(input1, input2))