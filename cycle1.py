# Создать список из десяти целых чисел.
# Вывести на экран каждое число, увеличенное на 1.

lst = []
for i in range(1, 11):
    lst.append(i)

for i in lst:
    print(i + 1)