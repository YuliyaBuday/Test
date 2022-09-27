number = input("Введите двоичное число:")
list_of_digit=list(number)#преобразовываем введенное число в список
print(list_of_digit)#выводим список
list_of_digit.reverse()#разворачиваем список
print(list_of_digit)#выводим перевернутый список
sum=0
degree=0
error = False
for i in list_of_digit:#для значения i в списке
    i=int(i)
    if i==1 or i==0:#если i равно 0 или 1, так как в двоичной системе только 2 числа -0 и 1
        sum+=2**degree*i#умножаем i на 2 в степени, которая с каждой итерацией увеличивается на 1
        degree+=1
    else:
        error = True# иначе выводится ошибка
        print("Ошибка")
        break#прерываем выполнение, если значение не равно 0 или 1
if  error == False:#выводим сумму
    print(sum)