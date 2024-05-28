from pp_oop_Animal import Animal


class Cat(Animal):
    def speak(self):
        print("meow")

    def __str__(self):
        return f"Cat name: {self._name}, cat age:{self._age}"


class Rabbit(Animal):
    def speak(self):
        print("meep")

    def __str__(self):
        return f"Rabbit name: {self._name}, rabbit age:{self._age}"
