'''
# task9
# вычисление факториала

n = int(input('число: '))
sum = 1
while n>0:
    sum = sum*n
    n = n-1

print(sum)
'''
'''''''''''''''''''''''
# task11
# найти для числа порядковый номер его места в ряду Фибоначчи
# 1 2 3 4 5 6 7 8  9  10 11
# 0 1 1 2 3 5 8 13 21 34 55
n = int(input('введите число: '))
a = 0
b = 1
sum = a + b
sum = 1
counter = 1
while n >= b:
    sum = a + b
    a = b
    b = sum
    #print(a) #контроль
    counter = counter + 1
if n!=a:
    print('этого числа нет в ряду Фибоначчи')
else:
    print(f" число находится на {counter}-й позиции ряда")
'''''''''''''''''''''''
'''''''''''''''''''''''
# task13
# найти самую длинную оттепель
# 6 -20 30 -40 50 10 -10
#    1 3 -3 4 5 7 -1
number = 7
counter = 0
srok = 0
for i in range(number):
    temper = int(input('введите температуру: '))
    if temper>= 0:
        counter += 1
        srok = counter 
    else:
        counter = 0
print(srok)
'''''''''''''''''''''''

'''''''''''''''''''''''
#15 задача про арбузы (нахождение макс-мин)
n = 7
max = 0
min = 0
for i in range(n):
    mass = int(input('введите массы: '))
    if mass > max:
        min = max = mass
    elif mass<min:
        min = mass

print(f"самый тяжелый весит {max} кило,", end=" ")
print(f"самый легкий весит {min} кило")
'''''''''''''''''''''''
n = (1, 2)
print (n)