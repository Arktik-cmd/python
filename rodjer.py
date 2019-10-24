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
    print('До скольки будем считать? Например до 100')

else:
    print('''Передумал, зря!
Пока!''')
