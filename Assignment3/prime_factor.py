"""
- take the number
 a = 12

looping n from 2 until a
  while number is not 1,
        - if divisible by only itself
            return the number
            if n is prime:
                if number is divisible by n:
                update the number to be divided
                # 12-> 6
                put n in an array
print array
if len(array) > 1:
    True

"""
import math
a = int(input("Insert integer"))
#
print("Here are the prime factors:")
divisor = 2
while a >= divisor**2:
    if a % divisor == 0:
        print(divisor, end=", ")
        a = a / divisor
    else:
        divisor += 1
if a>1:
    print(int(a), end='')