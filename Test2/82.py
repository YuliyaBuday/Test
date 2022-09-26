q = int(input("Введите десятичное число:"))
result = []
index = 0
while q != 0:
    r = q % 2
    # k=list(result)
    result.insert(index, str(r))
    q = q // 2
    
print(''.join(result))