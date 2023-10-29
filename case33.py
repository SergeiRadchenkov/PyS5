'''
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''

# Решение с помощью функции
grades = [1, 3, 3, 3, 4]
max_grade = max(grades)
min_grade = min(grades)
print(grades)

def change_max():
    for index, item in enumerate(grades):
        if item == max_grade:
            grades[index] = min_grade
    return grades

print(change_max())

# Решение с помощью рекурсии
grades = [1, 3, 3, 3, 4]

def recur(grades, index = 0, max_grade = max(grades), min_grade = min(grades)):
    if len(grades) - 1 < index:
        return
    if grades[index] == max_grade:
        grades[index] = min_grade
    recur(grades, index + 1)

recur(grades)
print(grades)