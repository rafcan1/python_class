import random
from pp_oop_Animal import Animal


class Person(Animal):
    def __init__(self, name, age):
        # in the body of the class we can invoke (Parent class) Animal.__init__() to set an age data attrbute
        Animal.__init__(self, age)
        # the same way we can invoke any other parrent method
        Animal.set_name(self, name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print("hello")

    def age_diff(self, other):
        # alternate way: diff = self.age - other.age
        # the same way we can invoke any other parrent method
        diff = self.get_age() - other.get_age()
        if self._age > other.age:
            print(f"{self._name} is {diff} years older than {other.name}")
        else:
            print(f"{self._name} is {-diff} years younger than {other.name}")

    def __eq__(self, other):
        return type(self) == type(other) and self._name == other._name

    def __str__(self):  # overrides __str__() method from Animal class
        return f"Person name: {self._name}, person age:{self._age}"


class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self._major = major

    def change_major(self, major):
        self._major = major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.75:
            print("i should eat")
        else:
            print("i am watching tv")

    def __add__(self, other):
        name = self.get_name()+"-"+other.get_name()
        new_student = Student(name, self._age+other._age)
        return new_student

    def __str__(self):  # overrides __str__() method from Person class
        return f"Student name: {self._name}, student age:{self._age}"
