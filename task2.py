import math
import fractions

# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и *произведение дробей. Для проверки своего кода используйте модуль fractions.

f1 = input("Введите первую дробь (в формате a/b, без пробелов): ")
f2 = input("Введите вторую дробь (в формате a/b, без пробелов): ")

numerator1 =int(f1.split('/')[0])
denominator1 =int(f1.split('/')[1])
numerator2 = int(f2.split('/')[0])
denominator2 =int(f2.split('/')[1])

sum_numerator = numerator1 * denominator2 + numerator2 * denominator1
sum_denominator = denominator1 * denominator2
gcd_sum = math.gcd(sum_numerator, sum_denominator)
if  gcd_sum != 1:
    sum_numerator //= gcd_sum
    sum_denominator //= gcd_sum
print(f'Сумма дробей: {sum_numerator}/{sum_denominator}')

mult_numerator = numerator1 * numerator2
mult_denominator = denominator1 * denominator2
gcd_mult = math.gcd(mult_numerator, mult_denominator)
if  gcd_mult != 1:
    mult_numerator //= gcd_mult
    mult_denominator //= gcd_mult
print(f'Произведение дробей: {mult_numerator}/{mult_denominator}')


f1 = fractions.Fraction(numerator1, denominator1)
f2 = fractions.Fraction(numerator2, denominator2)
print(f1 + f2)
print(f1 * f2)
