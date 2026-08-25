from math import pow
def remove(n,digit):
    '''Return all digits of non-negative N 
    that are not DIFIT,for some
      non-negative DIGIT less than 10.
    >>> remove(231,3)
    21
    >>>remove(243132,2)
    4313
    '''
    kept,digits=0,0
    while(n>0):
        n,last=n//10,n%10
        if(last!=digit):
            kept=kept+last*pow(10,digits)
            digits=digits+1
    return int(kept) 

remove(231,3)
remove(243132,2)


def trace1(fn):
    '''Returns a version of fn that first print
    it is called.
    
    fn - a function of 1 argument
    '''
    def traced(x):
        print('Calling',fn,'on argument',x)
        return fn(x)
    return traced


#decorate
@trace1
def square(x):
    return x*x

@trace1
def sum_square_up_to(n):
    k=1
    total=0
    while k<=n:
        total,k=total+square(k),k+1
    return total