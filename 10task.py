n = int(input("Введите число монеток: "))

i = 0
count1 = 0
count2 = 0
while i < n:
    m = int(input("Введите сторону монетки - 0 или 1: "))
    if m > 0:
        count1 += 1
    else:
        count2 += 1
    i += 1
if count1 > count2:
    print (f'нужно перевернуть {count2} монет')
else:
    print (f'нужно перевернуть {count1} монет')
        