from random import randint
from time import sleep

def intro():
    print('''Вы находитесь в землях, населенных драконами.
Перед собой вы видите 2 пещеры.
В одной дракон который вас съест, в другой же дракон который даст вам сокровищ.''')


def  select_cave():
    print('В какую пещеру пойдете( Набери "1" или "2" )')
    cave = int(input())
    while cave not in {1,2}:
        print('ошибка ввода')
        cave = int(input())
    return cave

def check_cave(selected_cave):
    friendly_cave = randint(1, 2)

    print('И вот вы приближаетесь к пещере...')
    sleep(1)
    print('Темнота заставляет вас дрожать от страха...')
    sleep(1)
    print('И тут выпригивает огромный дракон, и ...')

    if friendly_cave == selected_cave:
        print('Ты выбрал верную пещеру, друг, дракон озолотил тебя!')

    if friendly_cave != selected_cave:
        print('Съедает тебя мой друг, ты проиграл!')


play_again = 'да'
while play_again == 'да':
    intro()
    check_cave(select_cave())
    print('Сыграем еще? Ответь "Да" или "Нет"')
    play_again = input()
    play_again = play_again.lower()