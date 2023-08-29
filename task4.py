import random
LOW_LIMIT=0
UPPER_LIMIT=1000
random_number = random.randint(LOW_LIMIT, UPPER_LIMIT)
print("The random integer is :", random_number)

for i in range(10):
    hidden_number = int(input('Ваш ответ: '))
    if hidden_number > random_number:
        print('Ваш ответ(',hidden_number, ') больще провильного ответа')
    elif hidden_number < random_number:
        print('Ваш ответ(',hidden_number,') менше провильного ответа')
    else:
        print('Поздравляю, вы угадали! Правильный ответ:',random_number)
else:
    print('Вы потратили все 10 попыток')