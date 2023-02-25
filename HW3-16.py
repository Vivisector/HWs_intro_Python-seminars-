#task 16
import random
#n = [1,2,3,4,5,5,6,7] # учебный массив
list = [] # большой массив
for i in range(0,1000):
    x=random.randint(0,10)
    list.append(x)

find = 7 #что ищем
cnt = 0
for i in range(len(list)):
    if list[i] == find: cnt +=1
print(cnt)