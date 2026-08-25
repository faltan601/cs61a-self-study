def search(f):
    x=0
    while not f(x):
        x+=1
    return x

def is_three(x):
    return x==3

def square(x):
    return x*x

def positive(x):
    return max(0,square(x)-100)

def inverse(f):
    '''Return g(y) such that g(f(y))==x.'''
    return lambda y:search(lambda x:f(x)==y)

def f(x):
    return g(x-1)

def g(y):
    return abs(h(y)-h(1/y))

def h(z):
    return z*z

print(f(1))
