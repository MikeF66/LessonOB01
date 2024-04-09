class User():
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._access = "user "

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_access(self):
        return self._access

    def set_name(self):
        self._name = name

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self._access = "admin"
        self._users = []

    def add_user(self, user):
        if user not in self._users:
            self._users.append(user)
            print("В список добавлен   ID", user.get_id(), ",  допуск", user.get_access(), ",  ", user.get_name())
        else:
            print("Ошибка: пользователь с такими атрибутами уже есть, либо некорректные данные пользователя")

    def remove_user(self, user):
        if user in self._users:
            self._users.remove(user)
            print("Пользователь", user.get_name(), "ID -", user.get_id(), "удален")
        else:
            print("Ошибка: пользователя с такими атрибутами нет с списке, либо некорректные данные пользователя")

    def show_users(self):
        if self._users:
            print("Список пользователей:")
            for user in self._users:
                print(" ID", user.get_id(), ",  допуск", user.get_access(),",  ", user.get_name())
        else:
            print("В списке нет пользователей")

ad1 = Admin("101", "Владимир")

user1 = User("201", "Михаил")
user2 = User("202", "Анна")
user3 = User("203", "Сергей")
user4 = User("204", "Артем")
print("")

ad1.add_user(user1)
ad1.add_user(user2)
ad1.add_user(user3)
ad1.add_user(user4)
ad1.add_user(ad1)
ad1.show_users()
print("")

ad1.remove_user(user2)
ad1.show_users()
print("")

ad1.remove_user(user3)
ad1.show_users()

