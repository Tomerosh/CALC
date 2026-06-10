class Variable():
    def __init__(self, name, value=1, power=1):
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
    
    def __repr__(self):
        val = ''
        if self.value != 1: 
            if self.value.is_integer():
                val = str(int(self.value))
            else: 
                val = str(self.value)
        pow = '^' + str(self.power) if self.power != 1 else ''
        return val + self.name + pow
    
    def __eq__(self, other):
        if isinstance(other, Variable):
            return self.name == other.name and self.power == other.power
        return False
    
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
            if self.power == 1:
                power = self.power + float(other)
            else :
                power = self.power ** float(other)

            return Variable(self.name, self.value, power)
    

class Number():
    def __init__(self, value, power=1):
        self.value = float(value)
        self.power = power
    def __str__(self):
        if self.value == 0:
            return '0'
        else:
            power = '^' + self.power if self.power != 1 else ''
            return f'{self.value}{power}'
    def __repr__(self):
        if self.value == 0:
            return '0'
        else:
            power = '^' + self.power if self.power != 1 else ''
            return f'{self.value}{power}'
    def __add__(self, other):
        if isinstance(other, Number):
            if self.power == other.power:
                return Number(self.value + other.value)
            else:
                return False
        elif isinstance(other, Variable):
            return False
        elif isinstance(other, (int, float)):
            return Number(self.value + other)
        
    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value)
        elif isinstance(other, Variable):
            return False
        elif isinstance(other, (int, float)):
            return Number(self.value - other)
    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value)
        elif isinstance(other, Variable):
            return other * self
        elif isinstance(other, (int, float)):
            return Number(self.value * other)
    def __truediv__(self, other):
        if isinstance(other, Number):
            return Number(self.value / other.value)
        elif isinstance(other, Variable):
            return Variable(other.name, self.value / other.value, other.power)
        elif isinstance(other, (int, float)):
            return Number(self.value / other)

    def __pow__(self, other):
        if isinstance(other, Number):
            return Number(self.value ** self.value)
        elif isinstance(other, Variable):
            return False
        elif isinstance(other, (int, float)):
            return Number(self.value ** other)
    def __float__(self):
        return float(self.value)

# b = Variable('x', 1, -5)
# print(a**2)

# print(a**2)
# print(4*x**-2**2)


# print(type(Variable('x', '2', 1).value))
# print(Variable('x', 2) + Variable('x', 3, 2))
        
# import sympy

# x, y = sympy.symbols('x y')

# exp = 2 * x * 4 * x

# a = Variable('x', 4)
# # b = Variable('x', 2)
# # c = 'a'
# num = Number(2)