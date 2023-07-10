from datetime import date
from datetime import datetime


class Timing:
    def get_day(self):
        return date.today().strftime("%d/%m/%Y")

    def get_time(self):
        return datetime.now().strftime("%H:%M:%S")

    def birthday_date(self, birthday):
        return datetime.strptime(birthday, "%d/%m/%Y")
