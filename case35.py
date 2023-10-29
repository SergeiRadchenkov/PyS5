'''
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes 
'''
# Решение с помощью функции
def is_prime_1(n):
    flag = True
    for el in range(3, n):
        if n % el == 0:
            flag = False
    return flag

print(is_prime_1(32))

# Решение с помощью рекурсии
def is_prime_2(n, el = 3):
    if el < n:
        if n % el == 0:
            return False
        return is_prime_2(n, el + 1)
    return True

print(is_prime_2(7))