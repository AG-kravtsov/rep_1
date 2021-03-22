import datetime
# from dateutil.relativedelta import relativedelta


class Post:
    def __init__(self, title=None, date=None):
        # присвоить значение из Хранилища во время инициализиации
        self.date_received = None
        self.title = None

    def set_date_recevied(self, new_date):
        self.date_received = new_date

    def set_title(self, new_title):
        self.title = new_title

    def save_changes(self):
        pass

    def get_post_info(self):
        return {
            'date': self.date_received,
            'title': self.title
            }

class Employee:
    def __init__(self):
        # присвоить значение из Хранилища во время инициализиации
        self.name = None
        self.surname = None
        self.second_name = None
        self.Post = Post()


def main():
    empl = Employee()
    empl.Post.set_date_recevied('2020-01-21')
    empl.Post.set_title('spec')     # тут справочник вставляем
    empl.Post.get_post_info()

if __name__ == '__main__':
    main()
