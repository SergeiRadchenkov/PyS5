'''
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
'''
n = 2

def func(n):
    if n > 0:
        num = int(input("Число: "))
        func(n - 1)
        print(num, end=" ")

func(n)

# вариант 2 без рекурсии
n = 2
numbers = {3, 4}
print()
print(sorted(numbers, reverse=True))