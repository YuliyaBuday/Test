import random

x_max = random.randint(1, 100)
print(x_max)
y = 0
counter = 1
while counter <= 100:
    x2 = random.randint(1, 100)
    if x2 > x_max:
        y += 1
        print(x2, '-обновление')
        x_max = x2
    else:
        print(x2)
    counter += 1
print("Количество смен лидера:", y)
print("Максимальное число в ряду:", x_max)
