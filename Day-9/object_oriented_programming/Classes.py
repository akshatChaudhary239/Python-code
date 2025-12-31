# classes - this is like a blueprint
# A value define inside a class is known as attribute 
# A function defined inside a class is known as method

class Person:
    name = "Akku"
    age = 20
    work = "Data scientist"
    def greeting():
        return ("hey, there it's nice to see you here")

print(Person.name)
print(Person.age)
print(Person.work)
print(Person.greeting())