import random
#Pi=4*кол-во точек в круге/кол во точек
def pi(n):
    n_in=0
    for i in range(n):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        if (x*x+y*y) <=1:
            n_in=n_in+1
    return 4*n_in/n

n=int(input(print('enter amount of dots: ')))
print("pi= ",pi(n))
