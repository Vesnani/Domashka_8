'''
Функція повертає іменинників від поточної дати (включно) на тиждень вперед
'''
from datetime import datetime, timedelta
current_year = datetime.now().year

users = [
    {'name': 'Tania', 'birthday': datetime(year=current_year, month=6, day=12)},
    {'name': 'Roma', 'birthday': datetime(year=current_year, month=10, day=28)},
    {'name': 'Misha', 'birthday': datetime(year=current_year, month=5, day=28)},
    {'name': 'Lesia', 'birthday': datetime(year=current_year, month=5, day=27)},
    {'name': 'Olia', 'birthday': datetime(year=current_year, month=5, day=24)},
    {'name': 'Maryana', 'birthday': datetime(year=current_year, month=5, day=24)},
    {'name': 'Taras', 'birthday': datetime(year=current_year, month=5, day=25)},
    {'name': 'Igor', 'birthday': datetime(year=current_year, month=5, day=21)},
    {'name': 'Andrij', 'birthday': datetime(year=current_year, month=5, day=26)},
]

def get_birthdays_per_week(users):
    current_date = datetime.now()
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekdays = []

    next_monday = current_date + timedelta(days=(7 - current_date.weekday()))
    for i in range(7):
        index = (next_monday.weekday() + i) % 7
        weekdays.append(days_of_week[index])

    for day in weekdays:
        if day == 'Saturday' or day == 'Sunday':
            next_day = 'Monday'
        else:
            next_day = day

        birthday_users = [user['name'] for user in users if
                          (user['birthday'].weekday() == days_of_week.index(next_day) or
                          (day == 'Monday' and user['birthday'].weekday() == 6)) and
                          (current_date + timedelta(days=1)) <= user['birthday'] <= (current_date + timedelta(days=7))]

        if birthday_users:
            print(f"{day}: {', '.join(birthday_users)}")

print(get_birthdays_per_week(users))
