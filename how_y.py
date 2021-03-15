import datetime
from collections import namedtuple

InnerBlock = namedtuple('Дата', 'years, months, days')

class Employee:
    def __init__(self):
        # self.how_long_post = None
        self.date_new_post = None

    def set_date_post(self, day, month, year):
        self.date_new_post = datetime.datetime(year, month, day)

    def get_date_post(self):
        cur_date = datetime.datetime.today()
        date = self.date_new_post

        day, month, year = 0, 0, 0

        if cur_date.day < date.day:
            # day = date.day - cur_date.day
            day = (cur_date - datetime.timedelta(date.day)).day
        elif cur_date.day >= date.day:
            if cur_date.month != date.month:
                month += 1
            day = cur_date.day - date.day
        if cur_date.month <= date.month:
            month += date.month - cur_date.month
        elif cur_date.month > date.month and cur_date.year > date.year:
            # year += 1
            # print(year)
            month += cur_date.month - date.month

        year += cur_date.year - date.year

        print(year, month, day)

        # return InnerBlock(
        #     years=year,
        #     months=month,
        #     days=day,
        # )

def main():
    empl = Employee()
    empl.set_date_post(15, 4, 2020)
    empl.get_date_post()
    # years, month, days = empl.get_date_post()    

if __name__ == '__main__':
    main()