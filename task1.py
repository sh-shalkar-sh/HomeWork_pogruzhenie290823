print('Таблица умножения')


for i in range(2, 10):
    for k in range(2, 11):
        print(f'{i} * {k} = {i * k}\t', end='')
    print('')
else:
    print('Конец')