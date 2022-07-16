import random
import math
a = random.randint(99, 1000)
b = random.randint(99, 1000)
print(a)
print(b)
print("GCD of a and b is ", math.gcd(a, b))
divisor = 0
print("THE COMMON DIVISORS OF NUMBER ",a," AND ",b," ARE -")
L = []
for i in range(1, min(a, b)+1):
  if a % i == b % i == 0:
    divisor = i
    L.append(i)
    L.reverse()
    print(L)