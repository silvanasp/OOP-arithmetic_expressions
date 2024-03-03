from abc import ABC, abstractmethod

class ArithmeticExpression(ABC):
    @abstractmethod
    def calculate(self):
        pass
    
    @abstractmethod
    def pretty_print(self):
        pass


class BinaryOperator(ArithmeticExpression, ABC):
    def __init__(self, left_expression, right_expression):
        self._left = left_expression
        self._right = right_expression

    def pretty_print(self, symbol_operator):
        print('(', end='')
        self._left.pretty_print()
        print(')', end='')
        print(symbol_operator, end='')
        print('(', end='')
        self._right.pretty_print()
        print(')', end='')


class Constant(ArithmeticExpression):
    def __init__(self, val):
        self._value = val
    
    def calculate(self):
        return self._value
    
    def pretty_print(self):
        print(self._value, end='')


class Sum(BinaryOperator):
    def __init__(self, left_expression, right_expression):
        super().__init__(left_expression, right_expression)

    def calculate(self):
        return self._left.calculate() + self._right.calculate()

    def pretty_print(self):
        super().pretty_print('+')


class Subtract(BinaryOperator):
    def __init__(self, left_expression, right_expression):
        super(left_expression, right_expression)

    def calculate(self):
        return self._left.calculate() - self._right.calculate()

    def pretty_print(self):
        super().pretty_print('-') 


class Product(BinaryOperator):
    def __init__(self, left_expression, right_expression):
        super().__init__(left_expression, right_expression)

    def calculate(self):
        return self._left.calculate() * self._right.calculate()

    def pretty_print(self):
        super().pretty_print('*')  


class Division(BinaryOperator):
    def __init__(self, left_expression, right_expression):
        super().__init__(left_expression, right_expression)

    def calculate(self):
        return self._left.calculate() / self._right.calculate()

    def pretty_print(self):
        super().pretty_print('/')                     


if __name__ == '__main__':
    one = Constant(1.0)
    two = Constant(2.0)
    three = Constant(3.0)
    # (1 + 2) * 3
    expr = Product(Sum(one, two), three)
    print(expr.calculate())

    expr.pretty_print()
    print()
