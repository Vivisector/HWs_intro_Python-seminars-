# n = [0,-1,5,2,3]
# # посчитать колво элементов, больших предыдущего
# print(sum([n[i] > n[i-1] for i in range(1, len(n))]))

''' определение наименьшего делителя
n = 31 #int(input())
flag = True
i = 2
while flag:
    if n % i == 0: # если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
        print(n)
        flag = False
    i += 1
'''