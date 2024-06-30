import math
from decimal import Decimal, getcontext
import sys

getcontext().prec = int(10**16)

x = int(input())


c = Decimal((1+math.sqrt(5))/2)**x - Decimal((1-math.sqrt(5))/2)**x

val = int(Decimal(1/math.sqrt(5))*c)
print(val)


sys.set_int_max_str_digits(int(10**6)) 

a, b = 0, 1
for _ in range(x):
    a, b = b, a + b

val2 = a
print(val2)

print(val==val2)