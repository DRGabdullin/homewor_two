# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

while True:
    try:
        value = int(input("Введите целое число, для преобразования: "))
        break
    except ValueError:
        print("Введите число!")


def convert(value):
    hexaDeciNum = ['0'] * 100
    i = 0
    while (value != 0):
        temp = 0
        temp = value % 16
        if (temp < 10):
            hexaDeciNum[i] = chr(temp + 48)
            i = i + 1
        else:
            hexaDeciNum[i] = chr(temp + 55)
            i = i + 1
        value = int(value / 16)
    j = i - 1
    while (j >= 0):
        print((hexaDeciNum[j]), end="")
        j = j - 1
    print()


convert(value)

print(hex(value))