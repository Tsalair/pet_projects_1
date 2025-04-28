from tkinter import Tk, Canvas
from datetime import date, datetime
# from time import sleep
from pathlib import Path

# print("Андрюшечка", __file__)


def get_events():
    path = Path(__file__)
    print(path.parent / "dates.txt")
    list_events = []
    with open(path.parent / "dates.txt", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip("\n")
            current_event = line.split(",")
            event_date = datetime.strptime(current_event[1], "%d/%m/%Y").date()
            current_event[1] = event_date
            list_events.append(current_event)
    return list_events


def days_between_dates(date1, date2):
    time_between = (date1 - date2).days
    
    # number_of_days = time_between.split(" ")
    # return number_of_days[0]
    return str(time_between)

root = Tk()
c = Canvas(root, width=800, height=800, bg="midnightblue")
c.pack()

c.create_text(
    100,
    50,
    anchor="w",
    fill="yellow",
    font="Arial 28 bold underline",
    text="Календарь ожидания",
)

events = get_events()
today = date.today()

vertical_space = 120

events.sort(key=lambda event: event[1])

for event in events:
    event_name = event[0]
    days_until = days_between_dates(event[1], today)
    display = f"{event_name} через {days_until} дн."
    if (0 < int(days_until) <= 5):
        text_color = "red"
    else:
        text_color = "lightblue"
    c.create_text(
        100,
        vertical_space,
        anchor="w",
        fill=text_color,
        font="Arial 20 bold",
        text=display
    )
    vertical_space += 50
# print("w")
c.mainloop()
# sleep(5)
