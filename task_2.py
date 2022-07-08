# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

print('Введите 5 чисел: ')                  # a = list(map(int, input().split))
a = int(input())                            # max_number = a[0]
b = int(input())                            # for i in a:
c = int(input())                            #   if i > max_number:
d = int(input())                            #       max_number = i
e = int(input())
max_number = a
if b > a:
    max_number = b
if c > b:
    max_number = c
if d > c:
    max_number = d
if e > d:
    max_number = e
print(f'Максимальное число = {max_number}')    
