n = int(input("Введите первое число: "))
n = abs(n)
m = int(input("Введите второе число: "))
m = abs(m)
d = n
if n > m:
    d = m
while n % d != 0 or m % d != 0:
    d -= 1
print(d)
