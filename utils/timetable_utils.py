from datetime import datetime
from utils.config import SEM_START

time = ['09:30-11:05', '11:20-12:55', '13:10-14:45', '15:25-17:00', '17:15-18:50']
days = ['Понедельник',
        'Вторник',
        'Среда',
        'Четверг',
        'Пятница',
        'Суббота']


def get_day_range(day: str):
    match day:
        case 'понедельник' | '1' | 'пн':
            return range(0, 5)
        case 'вторник' | '2' | 'вт':
            return range(5, 10)
        case 'среда' | '3' | 'ср':
            return range(10, 15)
        case 'четверг' | '4' | 'чт':
            return range(15, 20)
        case 'пятница' | '5' | 'пт':
            return range(20, 25)
        case 'суббота' | '6' | 'сб':
            return range(25, 30)
        case _:
            return 0

def get_week_num():
    return (datetime.now() - SEM_START).days // 7 + 1

def get_weekday() -> int:
    return datetime.today().weekday()
