# Написать функцию ask_user() чтобы помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”


def ask_user():
    while True:
        answer = input('How are you? ')
        if answer == 'Fine':
            break

ask_user()
