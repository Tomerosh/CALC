class Test():
    def __init__(self, name):
        self.name = name
        self.age = 30

    def __setattr__(self, name, value):
        if name == 'name'

t =Test('tomer')
t.age = 5
print(t.name)