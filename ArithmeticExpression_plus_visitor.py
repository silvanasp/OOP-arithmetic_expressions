from abc import ABC, abstractmethod

class ArithmeticExpression(ABC):
    @abstractmethod
    def accept_visitor(self):
        pass


class BinaryOperator(ArithmeticExpression, ABC):
    def __init__(self, left_expression, right_expression):
        self._left = left_expression
        self._right = right_expression

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right
    

class Constant(ArithmeticExpression):
    def __init__(self, val):
        self._value = val

    @property
    def value(self):
        return self._value
    
    def accept_visitor(self, v):
        v.visit_constant(self)


class Sum(BinaryOperator):
    def __init__(self, left_expression, right_expression):
        super().__init__(left_expression, right_expression)
        self._symbol = '+'

    def accept_visitor(self, v):
        v.visit_sum(self)


class Subtract(BinaryOperator):
    def __init__(self, left_expression, right_expression):
        super().__init__(left_expression, right_expression)

    def accept_visitor(self, v):
        v.visit_subtract(self)


class Product(BinaryOperator):
    def __init__(self, left_expression, right_expression):
        super().__init__(left_expression, right_expression)

    def accept_visitor(self, v):
        v.visit_product(self)  


class Division(BinaryOperator):
    def __init__(self, left_expression, right_expression):
        super().__init__(left_expression, right_expression)

    def accept_visitor(self, v):
        v.visit_division(self)                     


class Visitor(ABC):
    @abstractmethod
    def visit_constant(self, constant):
        pass

    @abstractmethod
    def visit_sum(self, sum):
        pass

    @abstractmethod
    def visit_subtract(self, subtract):
        pass

    @abstractmethod
    def visit_product(self, product):
        pass

    @abstractmethod
    def visit_division(self, division):
        pass


class PrettyPrinter(Visitor):
    def _pretty_print_binary_operator(self, binary_operator, symbol_operator):
        print('(', end='')
        binary_operator.left.accept_visitor(self)
        print(')', end='')
        print(symbol_operator, end='')
        print('(', end='')
        binary_operator.right.accept_visitor(self)
        print(')', end='')

    def visit_constant(self, constant):
        print(constant.value, end='')

    def visit_sum(self, sum):
        self._pretty_print_binary_operator(sum, '+')

    def visit_subtract(self, subtract):
        self._pretty_print_binary_operator(subtract, '-')

    def visit_product(self, product):
        self._pretty_print_binary_operator(product, '*')

    def visit_division(self, division):
        self._pretty_print_binary_operator(division, '/')


class Stack:
    def __init__(self):
        self._stack = []
        # a list is the easyest way to implement a stack, but dequeue 
        # (a linked list) may be more efficient, see 
        # https://realpython.com/how-to-implement-python-stack/

    def push(self, value):
        self._stack.append(value)

    def pop(self):
        return self._stack.pop()
    
    def is_empty(self):
        return len(self._stack) == 0
         

class Calculator(Visitor):
    def __init__(self):
        self._stack = Stack()
    
    @property
    def result(self):
        res = self._stack.pop()
        assert self._stack.is_empty()
        return res

    def visit_constant(self, constant):
        self._stack.push(constant.value)

    def visit_sum(self, sum):
        sum.left.accept_visitor(self)
        sum.right.accept_visitor(self)
        self._stack.push(self._stack.pop() + self._stack.pop())

    def visit_subtract(self, subtract):
        subtract.left.accept_visitor(self)
        subtract.right.accept_visitor(self)
        res_right = self._stack.pop()
        res_left = self._stack.pop()
        self._stack.push(res_left - res_right)

    def visit_product(self, product):
        product.left.accept_visitor(self)
        product.right.accept_visitor(self)
        self._stack.push(self._stack.pop() * self._stack.pop())

    def visit_division(self, division):
        division.left.accept_visitor(self)
        division.right.accept_visitor(self)
        res_right = self._stack.pop()
        res_left = self._stack.pop()
        self._stack.push(res_left / res_right)


if __name__ == '__main__':
    one = Constant(1.0)
    two = Constant(2.0)
    three = Constant(3.0)
    expr = Product(Division(one, two), three) # (1 + 2) * 3

    pretty_printer = PrettyPrinter()
    expr.accept_visitor(pretty_printer)
    print()

    calculator = Calculator()
    expr.accept_visitor(calculator)
    print(calculator.result)
