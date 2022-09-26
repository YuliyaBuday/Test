number = input("Введите двоичное число:")
list_of_digit=list(number)
print(list_of_digit)
list_of_digit.reverse()
print(list_of_digit)
sum=0
degree=0
error = False
for i in list_of_digit:
    i=int(i)
    if i==1 or i==0:
        sum+=2**degree*i
        degree+=1
    else:
        error = True
        print("Ошибка")
        break
if  error == False:
    print(sum)