from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    if not users:  # в разі якщо список користувачів порожній.
        return {} # повертає порожній словник
    now = date.today() # поточна дата береться з системного часу компьютора
    current_week_day = now.weekday() # поточний тиждень береться з системного часу компьютора
    weekdays = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday',
    }
    birthdays_per_week = {day: [] for day in weekdays.values()} # день народження на тижні = словник в якому ітеруються всі значення днів народження по дням тижня
    for user in users: # для кожного користувача в переліку всіх користувачів...
        name = user['name'] # імя користувача = відповідає імені кожного користувача
        birthday = user['birthday'] # день народження користувача = відповідає дню народження кожного користувача
        new_birthday = birthday.replace(year=now.year) # найближчий день народження = в даних дня народження користувача змінюємо рік дня народження користувача на поточний
        if new_birthday < now: # якщо найближчий день народження менше поточної дати...
            new_birthday = new_birthday.replace(year=now.year + 1) # то найближчий день народження змінюємо шляхом заміни року народження на поточний рік народження для подальшого розрахунку
        # Перевіряємо, чи дата народження потрапляє в наступний тиждень
        if now <= new_birthday <= now + timedelta(days=7): # якщо оновлений показник дня народження знаходиться в інтервалі часу між поточною датою і датою + 7 днів то...
            day_week = new_birthday.weekday() # визначаємо на який день тижня припадає день народження
            day_name = weekdays[day_week] # Отримуємо назву дня тижня
            # Перевірка, чи день народження потрапляє на вихідний
            if day_name in ['Saturday', 'Sunday']: # в разі коли день тижня припадає на суботу чи неділю то...
                day_name = 'Monday' # Переносимо відображення циєї дати на понеділок
            birthdays_per_week[day_name].append(name) # в разі якщо відповідає попередній умові, добавляємо значення в словник...
    print(birthdays_per_week) # друкуємо словник днів тижня з наявними/відсутніми днями народження...
    return {key: value for key, value in birthdays_per_week.items() if value} # повертаємо словник, видаляємо пусті списки


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 11, 16).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
