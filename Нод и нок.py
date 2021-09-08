def nod(a, b):
    if a < b:
        a,b = b,a
    while b != 0:
        x = a % b
        a,b=b,x
    return a

def nok_n(l):          #нок=a*b/нод(а*b)
    a = l[0]
    for i in l:
        a = (a * i /nod(a, i))
    return a

def nod_n(l):                       #ищет нод для первых двух чисел, а затем нод для предыдущего нода и чисел в строке, в итоге нод для строки
    nod0=nod(l[0], l[1])
    for l in l:
        nod0=nod(nod0,l)
    return nod0

l=[6,21,54,7]
print(nok_n(l))
print(nod_n(l))
