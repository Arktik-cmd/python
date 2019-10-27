from time import sleep
from random import randint,choice

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
                sign = choice('+-')

        if sign == '+':
            while number1 + number2 > count_to:
                number1 = randint(1, int(count_to))
                number2 = randint(1, int(count_to))
                sign = choice('+-')


        print(number1, sign, number2)

else:
    print('''Передумал, зря!
Пока!''')
