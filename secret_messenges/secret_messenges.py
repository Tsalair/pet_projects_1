from tkinter import Tk, simpledialog, messagebox
from random import choice


def is_even(number):
    return number % 2 == 0


def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters


def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters


def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + "x"
    even_letters = get_even_letters(message)

    odd_letters = get_odd_letters(message)

    for counter in range(0, int(len(message) / 2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = "".join(letter_list)
    return new_message


def get_task():
    task = simpledialog.askstring(
        "Задание", "Что сделать: зашифровать (з) или расшифровать (р)?"
    )
    return task


def get_message():
    message = simpledialog.askstring("Сообщение", "Введите секретное сообщение:")
    return message


def encrypt(message):
    encrypted_list = []
    fake_letters = [
        "а",
        "б",
        "в",
        "г",
        "д",
        "е",
        "ё",
        "ж",
        "з",
        "и",
        "й",
        "к",
        "л",
        "м",
        "н",
        "о",
        "п",
        "р",
        "с",
        "т",
        "у",
        "ф",
        "х",
        "ц",
        "ч",
        "ш",
        "щ",
        "ъ",
        "ы",
        "ь",
        "э",
        "ю",
        "я",
    ]
    for counter in range(0, len(message)):
        encrypted_list.append(message[counter])
        encrypted_list.append(choice(fake_letters))
        new_message = "".join(encrypted_list)
    return new_message


def decrypt(message):
    even_letters = get_even_letters(message)
    new_message = "".join(even_letters)
    return new_message


root = Tk()

while True:
    task = get_task()
    task = str(task).lower()

    if task == "з" or task == "зашифровать":
        message = get_message()
        swap_letters_message = swap_letters(message)
        encrypted = encrypt(swap_letters_message)
        messagebox.showinfo("Зашифрованное сообщение", encrypted)

    elif task == "р" or task == "расшифровать":
        message = get_message()
        swap_letters_message = decrypt(message)
        decrypted = swap_letters(swap_letters_message)
        messagebox.showinfo("Расшифрованное сообщение", decrypted)

    else:
        break
