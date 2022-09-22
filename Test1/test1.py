# Практическая часть

# задание 1
print("Юлия\n220116 г.Минск, ул. Мира, 35")

# задание 2
len = int(input("Введите длину садового участка, футы :"))
width = int(input("Введите ширину садового участка, футы :"))
square = len * width
square_1 = round(square / 43560, 5)
print("Площадь участка ", square_1, "акр")

# задание 3

total_sum = int(input("Введите сумму заказа в ресторане:"))
tax = round(total_sum * 20 / 120, 2)
tips = round((total_sum - tax) * 0.18, 2)
print("налог составит:", tax)
print("сумма чаевых составит:", tips)
print("общая сумма выплат составит:", tax + tips)

# задание 4
len_1 = int(input("Введите длину стороны многоугольника:"))
number_of_sides = int(input("Введите количество сторон многоугольника:"))
from math import pi
from math import tan

area = (number_of_sides * len_1 ** 2) / (4 * tan(pi / number_of_sides))
print("Площадь правильного многоугольника равна:", area)

# задание 5
answer = str(input("В группе есть еще посетители, если да - введите 'y'"))
total_sum=0
while answer=="y":
    age = int(input("Введите возраст посетителя"))
    price = 0
    if age<=2:
        price=0
    elif age>=3 and age<12:
        price=14
    elif age >65:
        price = 18
    else:price = 23
    total_sum+=price
    answer = str(input("В группе есть еще посетители, если да - введите 'y'"))
print("Общая цена билетов составляет:", round(total_sum,2))

