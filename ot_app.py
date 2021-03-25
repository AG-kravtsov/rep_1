import datetime
# from dateutil.relativedelta import relativedelta


class ChkKnowledge:
    pass


class Training:
    def __init__(self):
        self._data = None
        self._frequency = None

    def set_data(self, new_data):
        self._data = new_data


class WorkSafety(Training):
    pass


class FireSafety(Training):
    pass


class ElectroSafety(Training):
    pass


class SaveData:
    def __init__(self):
        self._objcts = {
            'post': Post,
            'employee': Employee,
            'empl': Employee
        }

    def save(self, obj_id):
        obj_type = self._objcts.get(obj_id)
        print('!!!!!!!', obj_type, '!!!!!!!!!!')


class Post:
    def __init__(self, title=None, date=None):
        # присвоить значение из Хранилища во время инициализиации
        self._date_received = None
        self._title = None

    def set_date_recevied(self, new_date):
        self._date_received = new_date

    def set_title(self, new_title):
        self._title = new_title

    # def save_changes(self):
    #     pass

    def get_post_info(self):
        return {
            'date': self._date_received,
            'title': self._title
            }

class Employee:
    def __init__(self):
        # присвоить значение из Хранилища во время инициализиации
        self.name = None
        self.surname = None
        self.second_name = None
        self.Post = Post()

    # def save_changes(self):
    #     pass

def main():
    empl = Employee()
    empl.Post.get_post_info()
    empl.Post.set_date_recevied('2020-01-21')
    empl.Post.set_title('spec')     # тут справочник вставляем
    e = empl.Post.get_post_info()
    print(e)
    wsaf = WorkSafety()
    
    # SaveData().save('post')

if __name__ == '__main__':
    main()
