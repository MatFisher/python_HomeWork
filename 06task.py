# Требуется написать программу, которая проверяет счастливость билета.

n = int(input("Введите номер билета: "))
num = str(n)
if int (num[0]) + int (num[1]) + int (num[2]) == int (num[3]) + int (num[4]) + int (num[5]):
    print ("Билет счастливый")
else:
    print ("Билет не счастливый")