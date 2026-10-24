
# 6-m
class Teacher:
    def __init__(self, fullname, subject):
        self.fullname = fullname
        self.subject = subject

    def __repr__(self):
        return f"{self.fullname} — {self.subject} fani o'qituvchisi"


teacher1 = Teacher("Dilnoza Rahimova", "Informatika")
print(teacher1)


# 7-m
class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __repr__(self):
        return f'{self.year}-yilda chiqarilgan "{self.title}" filmi'


movie1 = Movie("Abdullajon", 1991)
print(movie1)


# 8-m
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def __repr__(self):
        return f"{self.name}ning chiqaradigan ovozi: {self.sound}!"


animal1 = Animal("Mushuk", "Miyov")
print(animal1)


# 9-m
class City:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __repr__(self):
        return f"{self.name} shahri {self.country} davlatida joylashgan."


city1 = City("Urganch", "O'zbekiston")
print(city1)


# 10-m
class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def __repr__(self):
        return f"{self.brand} noutbuki, tezkor xotirasi: {self.ram} GB"


laptop1 = Laptop("Lenovo", 16)
print(laptop1)
