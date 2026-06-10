# import sympy

class Variable():
    def __init__(self, name, value, power=1):
        self.name:str = name
        self.value:float = float(value)
        self.power:float = float(power)

    # Print
    def __str__(self):
        
        val = ''
        if self.value != 1: 
            if self.value.is_integer():
                val = str(int(self.value))
            else: 
                val = str(self.value)
        pow = '^' + str(self.power) if self.power != 1 else ''
        return val + self.name + pow
    
    # Addition
    def __add__(self, other):
        if isinstance(other, Variable):
            if self == other:
                return Variable(self.name, self.value + other.value, self.power)
        return False
        
    # Substract
    def __sub__(self, other):
        if isinstance(other, Variable):
            if self == other:
                return Variable(self.name, self.value - other.value, self.power)
        return False

    # Multiply
    def __mul__(self, other):
        if isinstance(other, Variable):
            if self.name == other.name:
                return Variable(self.name, self.value * other.value, self.power + other.power )
            else:
                return False
        else:
            return Variable(self.name, self.value * float(other), self.power)
        
    # Divide
    def __truediv__(self, other):
        if isinstance(other, Variable):
            if self.name == other.name:
                return Variable(self.name, self.value / other.value, self.power + (other.power*(-1)) )
            else:
                return False
        else:
            return Variable(self.name, self.value / float(other), self.power)
        
    # Power
    def __pow__(self, other):
        if isinstance(other, Variable): # Power of another var
            pass
        else:
            return Variable(self.name, self.value, self.power ** float(other))
        
    def __eq__(self, other):
        if isinstance(other, Variable):
            return self.name == other.name and self.power == other.power
        return False
    
# print(type(Variable('x', '2', 1).value))
print(Variable('x', 2) + Variable('x', 3, 2))
        
# a = Variable('x', 1, 10)
# b = Variable('x', 1, -5)

# x, y = sympy.symbols('x y')

# exp = 2 * x * 4 * x

# print(a**2)

# print(x ** 10 ** 2 )


