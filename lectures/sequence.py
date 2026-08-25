def count(s,value):
    '''Count the number of times that value occur in sequence s.
    >>> count([1,3,2,1],1)
    2
    '''
    total=0
    for element in s:
       if element==value:
          total=total+1
    return total

def sum_below(n):
   total=0
   for i in range(n):
      total += i
   return total

def cheer():
   for _ in range(3):
      print('Love you!')

def divisors(n):
   return [1]+[x for x in range(2,n) if n%x==0]

