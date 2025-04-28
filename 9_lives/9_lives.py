import random

lives = 9
words = [
    "пицца",
    "баран",
    "камаз",
    "ручка",
    "лотос",
    "слово",
    "ангел",
    "поезд",
    "какао",
    "олень",
    "мираж",
    "шторы",
    "окунь",
    "малыш",
    "носки",
    "белок",
    "топаз",
    "зомби",
    "бровь",
    "выдра",
    "песок",
    "солод",
    "петух",
    "книга",
    "вилка",
    "кошка",
    "слюна",
    "репка",
    "ванна",
    "ссора",
]
words_descriptions = {
    "ручка": "школьная принадлежность",
    "баран": "домашнее животное",
    "камаз": "марка автомобилей",
    "лотос": "цветок",
    "слово": "часть речи",
    "поезд": "транспорт",
    "какао": "растение с вкусными плодами",
    "олень": "лесное животное",
    "шторы": "предмет интерьера",
    "окунь": "рыба",
    "малыш": "всё портит",
    "белок": "органическое вещество",
    "топаз": "драгоценный камень",
    "зомби": "жуткое существо",
    "бровь": "часть лица",
    "песок": "строительный материал",
    "солод": "компонент хлеба",
    "книга": "источник знаний",
    "вилка": "всегда есть на кухне",
    "слюна": "физиологическая жидкость",
    "репка": "овощ",
    "ванна": "сантехника",
    "ссора": "когда все обижаются",
    "кошка": "имеет усы",
    "пицца": "Итальянское блюдо",
    "ангел": "Небесное существо",
    "мираж": "Несуществующее видение",
    "носки": "Одежда",
    "выдра": "Популярный зверёк",
    "петух": "Птица с цветным хвостом",
}
secret_word = random.choice(words)
clue = list("?????")
heart_symbol = "\U0001f49b"
guessed_word_not_correctly = True


# создаём функцию, которая подставляет в подсказку clue угаданную букву
def update_clue(guesssed_symbol, secret_word, clue):
    global lives, guessed_word_not_correctly
    if guesssed_symbol == "":
        print("Пустая строка. Необходимо вести минумум одну букву.")
    elif guesssed_symbol != "":
        if guesssed_symbol in secret_word:
            print("Молодец, есть такая буква!🔥")

        for i, symb in enumerate(secret_word):
            if guesssed_symbol == symb:
                clue[i] = symb
                if "?" not in clue:
                    guessed_word_not_correctly = False
                    print("Победа!💥 Поздравляю, ты угадал слово!🎉")

    if guesssed_symbol not in secret_word:
        lives -= 1
        print("Такой буквы нет.")
        print(f"Осталось жизней: {lives}", lives * heart_symbol)

    print(clue)


print(
    f"Я загадал слово из пяти букв. Это...\n✅{words_descriptions[secret_word]}✅\n{clue}",
    "\nУгадай букву или слово целиком.",
)
print("Осталось жизней:", str(9), 9 * heart_symbol)

while guessed_word_not_correctly:
    if lives > 0:
        guess = input("Введи букву или слово:\n").lower()
        if len(guess) > 1:
            if guess != secret_word:
                lives -= 1
                print(
                    "Неправильно.\nОсталось жизней:", str(lives), lives * heart_symbol
                )
            else:
                guessed_word_not_correctly = False
                print("Победа!💥 Поздравляю, ты угадал слово!🎉")
        else:
            update_clue(guess, secret_word, clue)
    else:
        print("Жизни закончились... 😭\nGame over")
        break
