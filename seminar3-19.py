list = [1,2,3,4,5,6,7]
print("исходный список")
print(*list)

# k = 3
for j in range(1, len(list)):
    for i in range(j):
        list.insert(0, list.pop(-1))
    print(*list)