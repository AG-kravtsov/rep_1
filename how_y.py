import datetime
from dateutil.relativedelta import relativedelta
from collections import namedtuple

InnerBlock = namedtuple('Дата', 'years, months, days')

class Employee:
    def __init__(self):
        # self.how_long_post = None
        self.date_new_post = None

    def set_date_post(self, day, month, year):
        self.date_new_post = datetime.datetime(year, month, day)

    def get_date_post(self):
        max_date = datetime.datetime.today()
        min_date = self.date_new_post
        d = relativedelta(max_date, min_date)
        return InnerBlock(
            years=d.years,
            months=d.months,
            days=d.days,
        )

def main():
    empl = Employee()
    empl.set_date_post(15, 2, 2020)
    d = empl.get_date_post()
    print(d)

if __name__ == '__main__':
    main()