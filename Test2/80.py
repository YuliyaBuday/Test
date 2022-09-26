from math import floor

n = int(input("Введите число: "))
factor = 2
result = []
if n < 2:
    print("Ошибка")
else:
    while factor <= n:
        if n % factor == 0:
            result.append(factor)
            n = floor(n / factor)
        else:
            factor += 1
    print(result)
