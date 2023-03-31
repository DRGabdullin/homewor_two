# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей. Для проверки своего кода используйте модуль fractions.
import fractions
from math import gcd

a1, b1 = map(int, input("Введите первую дробь в формате a/b: ").split('/'))
a2, b2 = map(int, input("Введите вторую дробь в формате a/b: ").split('/'))

if a1 == b2:
    print('{}/{}'.format(a1 + a2, b1))
else:
    cd = int(b1 * b2 / gcd(b1, b2))
    rn = int(cd / b1 * a1 + cd / b2 * a2)
    g2 = gcd(rn, cd)
    n = int(rn / g2)
    d = int(cd / g2)
    print('Сумма дробей = {}/{}'.format(n, d) if n != d else n)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def multiply_fractions(num1, den1, num2, den2):
    num = num1 * num2
    den = den1 * den2
    common_factor = gcd(num, den)
    num //= common_factor
    den //= common_factor
    return (num, den)


product_num, product_den = multiply_fractions(a1, b1, a2, b2)
print(f"Произведение: {product_num}/{product_den}")

f1 = fractions.Fraction(a1, b1)
f2 = fractions.Fraction(a2, b2)
print("\nПроверка по модулю fractions")
print('Сумма дробей {} + {} = {}'.format(f1, f2, f1 + f2))
print('Произведение дробей {} * {} = {}'.format(f1, f2, f1 * f2))