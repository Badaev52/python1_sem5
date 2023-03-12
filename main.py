# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def expNum (x, y):
    if y == 0:
        return 1
    return (expNum(x, y - 1)) * x

a = int(input("Введите число А: "))
b = int(input("Введите число B: "))

print(f" A = {a}; B = {b} -> {expNum(a, b)}")


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 