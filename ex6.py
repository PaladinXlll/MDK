#Сложить цифры у введённого числа
def sum(num):
    s = 0
    for item in str(num):
        s = s + int(item)
    return s

n = int(input('Введи число целое, а я цифры сложу: '))

print(sum(n))