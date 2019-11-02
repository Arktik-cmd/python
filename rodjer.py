from time import sleep
from random import randint,choice
from timeit import default_timer

print('Привет меня зовут Роджер, а как тебя?')
name = input()
print('Приятно познакомиться ' + name)
print('''Давай проверим твои знания в математике.
Ты готов? Ответь "Да" или "Нет" ''')
answer = input()

while answer not in {'да', 'нет'}:
    print('''Должно быть 'Да' или 'нет'
Введи заново''')
    answer = input()
if answer == 'да':
    print('Хорошо давай начнем')

    question_quantity = ''
    count_to = ''
    correct_answers = 0
    fails = 0
    time_in_seconds = 0

    while not question_quantity.isdigit():
        print(name + ', сколько примеров ты готов решить?')
        question_quantity = input()

        if question_quantity.isdigit():
            while int(question_quantity) < 1:
                print('Должно быть больше "0" ')
                question_quantity = input()
                while not question_quantity.isdigit():
                    print('Должна быть цифра!!!')
                    question_quantity = input()
        else:
            print('Должна быть цифра')
    

    while not count_to.isdigit():
        print('До скольки будем считать? Например до 100')
        count_to = input()

        if count_to.isdigit():
            while int(count_to) < 2:
                print('Должно быть больше "1" ')
                count_to = input()
                while not count_to.isdigit():
                    print('Должна быть цифра!!!')
                    count_to = input()

    print('Хорошо, тогда начнем...')
    sleep(1)

    for question in range (int(question_quantity)):
        print(f'Пример {question+1}:')
        number1 = randint(1,int(count_to))
        number2 = randint(1,int(count_to))
        sign = choice('+-')

        if sign == '-':
            while number1 < number2:
                number1 = randint(1, int(count_to))
                number2 = randint(1, int(count_to))
            correct_answer = number1 - number2

        if sign == '+':
            while number1 + number2 > int(count_to):
                number1 = randint(1, int(count_to))
                number2 = randint(1, int(count_to))
            correct_answer = number1 + number2

        print(number1, sign, number2)
        print('Итак, дай свой ответ:')

        start = default_timer()
        student_answer = input()
        stop = default_timer()

        time_in_seconds += stop - start

        if int(student_answer) == correct_answer:
            print('Правильно, молодец')
            correct_answers += 1
        else:
            print('Неправильно')
            print(f'Правильный ответ: {correct_answer}')
            fails += 1

    if time_in_seconds < 60:
        time_spent = f'{time_in_seconds} секунд'
    else:
        minutes = time_in_seconds // 60
        seconds = time_in_seconds - (minutes*60)
        if seconds == 0:
            time_spent = f'{minutes} минут'
        else:
            time_spent = f'{minutes} минут и {seconds} секунд'

    if fails == 0:
        print(f'Молодец, {name}, ты верно ответил на все вопросы за {time_spent}')
    else:
        print(f'Ошибок {fails}, а правильных ответов {correct_answers}')
        print(f'Затраченное время: {time_spent}')




else:
    print('''Передумал, зря!
Пока!''')
