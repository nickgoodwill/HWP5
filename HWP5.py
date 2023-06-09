# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
print(is_prime(int(input('Введите число: '))))

# Задача №37.
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def rev(n):
    if n > 0:
        rev (n-1)
        print(k[-n], end=" ")

n = int(input("Введите число: "))
k = list(map(int, input("Введите числа через пробел: ").split()))
rev(n)


# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.


def rev1(a,b):
    if b == 1:
        return (a)
    if b != 1:
        return (a * rev1(a, b-1))

a = int(input("Введите число: "))
b = int(input("Введите число: "))
print("результат возедения в степень равен: ", rev1(a,b))


# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def sumdig(a, b):
    if b == 0:
        return a
    return sumdig(a + 1, b - 1)

a = int(input("Введите число: "))
b = int(input("Введите число: "))
print("Сумма чисел: ", sumdig(a, b))