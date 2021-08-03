import datetime
from dateutil.relativedelta import relativedelta
from collections import namedtuple

InnerBlock = namedtuple('Дата', 'год, месяц, день')

class Employee:
    def __init__(self):
        self.date_today = datetime.datetime.today().date()
        self.date_new_post = None
    
    def set_date(self, date):###
        year, month, day = date.rsplit('-')
        return datetime.datetime(int(year), int(month), int(day)).date()

    def set_date_post(self, cur_date, post_date):
        if cur_date != '':
            max_date = self.set_date(cur_date)
        else:
            max_date = self.date_today
        min_date = self.set_date(post_date)
        d = relativedelta(max_date, min_date)

        return InnerBlock(
            год = d.years,
            месяц = d.months,
            день = d.days,
        )

def main():
    empl = Employee()
    input_curent_date = input(f'Дата когда была проверка знаний, если оставить пустым будет проставлена сегодняшняя дата {empl.date_today} ----> ')
    input_post_date = input('Дата вступления в должность ----> ')

    date = empl.set_date_post(input_curent_date, input_post_date)

    print(date)

if __name__ == '__main__':
    print('''
Автоматический подсчет стажа работы сотруднка в должности\n
ДАТУ заполнять в формате: (XXXX-XX-XX) ГОД-МЕСЯЦ-ДЕНЬ 
    ''')
    while 1:
        main()
        сlose_input = input("Нажать ENTER для выхода, 1 - чтобы продолжить ----> ")
        if сlose_input != '1':
            break

    print ("Закрытие...")