n = int(input("Введите число: "))

x = 2
i = 0
while x < n:
    x = x * 2 
    i += 1

x = 1
for j in range(i):
    x = x * 2
    print (x)