#Создание венца творения человечества (калькулятора)
def calc(a, b, operation):
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        if b != 0:
            result = a / b
        else:
            result = 'Деление на 0 братан!'
    return result

x = float(input('Введите первое число: '))
y = float(input('Введите второе число: '))
op = input('Введите операцию (+, -, /, *)')
print(calc(x, y, op))