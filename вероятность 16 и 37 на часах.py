n1=0
n=0
for h in range(24):
    for min in range(60):
        for sec in range(60):
            if h==16:
                if (min==37 or sec==37):
                    n1=n1+1
            elif min==16 and sec==37:
                n1=n1+1
            elif min==37 and sec==16:
                n1=n1 + 1
            n=n+1
print(n1)
print(n)
print('вероятность: ', n1/n)
