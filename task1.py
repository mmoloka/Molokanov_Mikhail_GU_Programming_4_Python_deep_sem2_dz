# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

num = int(input('Введите целое число: '))

print(hex(num))

MOD = 16
string = ''
hex_members = '0123456789ABCDEF'

while num > 0:
    string = hex_members[num % 16] + string
    num //= MOD

print(string)