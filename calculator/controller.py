from calculator.service import Service
class Controller:
    def __init__(self):
        num1 = int(input('첫번째 수'))
        num2 = int(input('두번째 수'))
        service = Service(num1, num2)
        op = input('연산자 입력')
        result = service.exec(op)
        print('계산결과 : %d' % result)