import datetime

class Employee:
    def __init__(self):
        self.how_long_post = None

    def set_date_post(self, day, month, year):
        cur_date = datetime.datetime.today()
        self.how_long_post = cur_date - datetime(year, month, day)


def main():
    empl = Employee()


if __name__ == '__main__':
    main()