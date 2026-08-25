def if_(c,t,f):
    if c:
        return t
    else:
        return f

from math import sqrt,pi

def real_sqrt(x):
    '''Reurn the real part of the square root of x.'''
    return if_(x>=0,sqrt(x),0)

def has_big_sqrt(x):
    return x > 0 and sqrt(x) > 10

def reasonable(n):
    return n == 0 or 1/n != 0

''''Generalization.'''

def area(r,shape_constant):
    assert r > 0,'A length must be positive.'
    return r*r*shape_constant

def area_square(r):
    return area(r,1)

def area_circle(r):
    return area(r,pi)

def area_hexagon(r):
    return area(r,3 * sqrt(3) / 2) 

