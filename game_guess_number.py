# Игра угадай число
from random import randint

print('Привет! Как тебя зовут?')
name = input()

def guess_number():

    print('Чтож, ' + name + ', давай начнем, я загадал число, попробуй угадать')
    number = randint(1, 20)


    for i in range(6):
        print('Попробуй угадать: ')
        guess_number = int(input())

        if guess_number > number:
            print('Твое число слишком большое')
        if guess_number < number:
            print('Твое число слишком маленькое')
        if guess_number == number:
            break

    if guess_number == number:
        print('Ты угадал за ' + str(i+1) + ' попыток')
    else:
        print('Я загадал число ' + str(number))

play_again = 'да'

while play_again == 'да':
    guess_number()
    print('Сыграем еще? Ответь "Да" или "Нет"')
    play_again = input()
    play_again = play_again.lower()