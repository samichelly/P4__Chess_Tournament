from datetime import date
from datetime import datetime


def get_day():
    return date.today().strftime("%d/%m/%Y")


def get_time():
    return datetime.now().strftime("%H:%M:%S")
