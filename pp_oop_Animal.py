class Animal:
    def __init__(self, age):
        self._age = age
        self._name = None

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name

    def set_age(self, newage):
        self._age = newage

    def set_name(self, newname=""):
        self._name = newname

    def __add__(self, other):
        return Animal(self._age + other._age)

    def __eq__(self, other: object) -> bool:
        return type(self) == type(other) and self._age == other._age

    def speak(self):
        print("mniam mniam")

    def __str__(self):
        return f"Animal name: {self._name}, animal age:{self._age}"
