class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        print(f'{date1.day} {date1.month} {date1.year}')
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        if day <= 31 and day != 0 and month <= 12 and month != 0 and year <= 3999:
            print(date_as_string)
            return day, month, year,
        else:
            print('Ошибка ввода данных')


d = '06-10-1999'
date_to_nums = Date.from_string(d)
is_date = Date.is_date_valid(d)
