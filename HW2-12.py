# 12 найти два числа по их сумме и произведению
# x1+x2 = S
# x1*x2 = P
S = 41
P = 414
x = 0
#проверка уравнения на решаемость (через проверку дискриминанта)")
# ax^2-s*x+p = 0
# D = b2-4ac = -s*s-4p = 64-4*15 = 
if (S*S - 4*P)<0:
    print(f"таких чисел не существует!")
elif (S*S - 4*P)==0:
    x = S//2
    print(f"загаданные числа: {x} и {S-x}")
else:
    for i in range(P-1, 2, -1):
        # ищем наибольший делитель произведения и проверяем, чтобы он не было больше суммы S
        if P%i==0 and S-i>0:
            print(i)
            x = i
            break
    print(f"загаданные числа: {x} и {S-x}")
    

