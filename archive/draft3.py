
class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1
    
    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def __add__(self, other):
        self.age += 1
        return  f'{self.name} is {self.age + other} years old'
    

user = User('Tomer', 30)
user.birthday()
print(user + 1)