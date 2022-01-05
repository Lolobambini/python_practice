# Задание 16.9.4
# Команда проекта «Дом питомца» планирует большой корпоратив для своих волонтеров.
# Вам необходимо написать программу, которая позволяла бы составлять список нескольких гостей.
# Решите задачу с помощью метода конструктора и примените один из принципов наследования.
#
# При выводе в консоль вы должны получить:  “Иван Петров, г.Москва, статус "Наставник"

class Volunteers:
    def __init__(self, name):
        self.name = name

    def get_guest(self):
        return self.name


class Status (Volunteers):
    def __init__(self, name, status):
      Volunteers.__init__(self, name )
      self.status = status

    def getStatus(self):
        return self.status

class City(Status):
    def __init__(self, name, status, city):
        Status.__init__(self, name,  status)
        self.city = city
    def getCity(self):
        return self.city

a = City('Иван Петров', '"Наставник"', 'Москва')

print(f"Волонтер", a.get_guest(),',', "город", a.getCity(),',', "статус", a.getStatus())


