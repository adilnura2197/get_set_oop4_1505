class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        if new_password > 5:
            self.__password = new_password
            print(f"To'g'ri parol")

        else:
            print(f"Noto'g'ri parol")


u1 = User('admin', 12345)
print(u1.username)

password = u1.get_password()
print(password)

u1.set_password(98765)
print(u1.get_password())
