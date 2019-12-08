import os

#Эта функция удаляет дубликаты в файле
def delete_same_rows(file_name):
    uniques = []
    with open(file_name, 'r') as f, open(f'tmp_{file_name}', 'a')as f2:

        for row in f:
            splited = row.split()
            number1, sign, number2, repeat = splited
            unique = f'{number1} {sign} {number2}'

            if unique not in uniques:
                uniques.append(unique)
                f2.write(f'{inique} {repeat}')

    os.delete(file_name)
    os.rename(f'tmp_{file_name}', file_name)

delete_same_rows('1_errors.txt')