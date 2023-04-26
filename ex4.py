#Найти наименьшее общее кратное
def noc(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)

x = int(input('A = '))
y = int(input('b = '))
print('Наименьшее общее кратное =', noc (x, y))
   