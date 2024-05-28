from pp_oop_Animal import Animal
from pp_oop_Animals import Cat, Rabbit
from pp_oop_Humans import Person, Student

jelly = Cat(4)
jelly.set_name("Jelly")

print(jelly)

tiger = Cat(1)
tiger.set_name("Tiger")

suzan = Cat(6)
suzan.set_name("Suzan")


# this works because we have a magic add method for animal class
new_cat = jelly + tiger + suzan
print(new_cat.get_age())
print(new_cat)

suzan.speak()

rafia = Student("Rafia", 27, "LMT")
rafia.speak()

ansı = Student("Ansı", 25, "LMT")


rafia.add_friend(ansı)
