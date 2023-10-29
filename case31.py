'''
Последовательностью Фибоначчи называется
последовательность чисел a0, a1, ..., an, ..., где
    a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию
'''

# Решение через функцию
n = 7
fibo_prev, fibo_next = 0, 1
for i in range(0, n):
    fibo_prev, fibo_next = fibo_next, fibo_prev + fibo_next
print(f'{n}-е число Фибоначчи = {fibo_next}')

# Решение через рекурсию
n = 7
fibo_prev, fibo_next = 0, 1

def fibo(n):
    if n < 3:
        return n    
    return fibo(n - 1) + fibo(n - 2)
print(f'{n}-е число Фибоначчи = {fibo(n)}')