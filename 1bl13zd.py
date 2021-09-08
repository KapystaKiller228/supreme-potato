def converter(num, new_base, old_base):
    if isinstance(num, str):
        n = int(num, old_base)   #переводит число из неадекватной строки в 10-систему(сам в шоке что это уже вшито в питон)
        print(n)
    else:
        n = int(num)

    if n < new_base:
        return alphabet[n]
    else:
        return converter(n // new_base, new_base, old_base) + alphabet[n % new_base]

alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num=input('Print number: ')
new_base=int(input('Print new base: '))
old_base=int(input('Print old base: '))
for i in range(len(num)):               #проверка на дебила
    for n in range(len(alphabet)):
        if num[i] == alphabet[n]:
            if n+1 > old_base:
                print('deleting system32...')
                quit()
print(converter(num,new_base,old_base))