# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.


def ritm(str):
    str = str.lower().split()
    f = lambda x: sum(1 for i in x if i in 'аеёиоуыэюя')
    tmp = f(str[0])
    if all([f(i) == tmp for i in str]):
        return 'Парам пам-пам'
    return 'Пам парам'


str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
print(ritm(str_1))