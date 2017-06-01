# Попросить пользователя ввести возраст.
# По возрасту определить, чем он должен заниматься: учиться в детском саду, школе, ВУЗе или работать.
# Вывести занятие на экран.

age = float(input('Please enter your age: '))

if age < 7:
    print('Go to kindergarten!')
elif age in range(7,18):
    print('Go to school!')
elif age in range(18, 23):
    print('Go to university!')
else:
    print('Go to work!')