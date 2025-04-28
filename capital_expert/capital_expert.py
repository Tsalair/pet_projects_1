from tkinter import Tk, simpledialog, messagebox
from pathlib import Path

# print("Андрюшечка", __file__)


def read_from_file():
    path = Path(__file__)
    # print(path.parent)
    with open(path.parent / "capital_data.txt", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            country, city = line.split("/")
            the_world[country] = city
        # return f.read().splitlines()


def write_to_file(country, city):
    path = Path(__file__)
    with open(path.parent / "capital_data.txt", "a", encoding="utf-8") as f:
        # for country, city in the_world.items():
        f.write(f"{country}/{city}\n")


print("Знаток - столицы мира")
root = Tk()
root.withdraw()

the_world = {}

read_from_file()

a = True
while a:
    query_country = simpledialog.askstring("Страна", "Введите название страны:")
    if query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo(
            "Ответ", f"{query_country}: столица этой страны - {result}!"
        )

    elif query_country is not None and query_country not in the_world:
        new_city = simpledialog.askstring(
            "Научите меня", f"Я не знаю, как называется столица страны {query_country}!"
        )
        the_world[query_country] = new_city
        write_to_file(query_country, new_city)
    elif KeyboardInterrupt:
        root.destroy()
        a = False
    else:
        root.destroy()
        a = False
