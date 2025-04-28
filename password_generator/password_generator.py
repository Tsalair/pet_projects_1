import random
import string

genering = True
while genering:
    adjectives = ['red', 'blue', 'orange', 'yellow', 'green', 'grey', 'black', 'purple']
    names = ['Vasya', 'Katya', 'Masha', 'Petya', 'Kolya', 'Vika', 'Fyokla']
    number = random.randrange(0,100)
    special_char = random.choice(string.punctuation)

    password = (random.choice(adjectives) + random.choice(names) + str(number) + special_char)
    print(password)
    'Тебе нравится пароль?'
    answer = input('Нужен другой пароль? Введите да или нет\n').lower()
    if answer == 'нет':
        genering = False


