from calculator.model import Calulator
class Service:

    def __init__(self, num1, num2):
        self.calc = Calulator(num1, num2)

    def exec(self, op):
        if op == '+':
            result = self.calc.add()
        elif op == '-':
            result = self.calc.sub()
        elif op == '*':
            result = self.calc.multi()
        elif op == '/':
            result = self.calc.divid()
        return result