# При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”

answers = {'what is love?': 'Baby don\'t hurt me',
           'how are you?': 'Fine',
           'what is the size of the universe?': 'Very big'}


def get_answer(question, answers):
    return answers.get(question, 'I don\'t know :(')


def ask_user(answers):
    while True:
        try:
            user_text = input('Ask me sth: ')
        except KeyboardInterrupt:
            print('Come back soon, bye!')
            break

        if user_text == 'bye!':
            break
        answer = get_answer(user_text, answers)
        print(answer)

ask_user(answers)
