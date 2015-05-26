#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Akshay
#
# Created:     25-05-2015
# Copyright:   (c) Akshay 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def square(x):
    return x*x

def two_power(x, n):
    while n > 1:
        x = square(x)
        n = n//2
    return x

def find_power(x, power, epsilon = 0.01):
    if x < 0 and power%2 == 0:
        return None
    low = min(-1, x) #WHY?
    high = max(x,1)


    ans = low + high
    ans = ans/2.0
    while abs(ans**power - x) > epsilon:
        print(low, high, ans)
        if ans**power > x:
            high = ans
        else:
            low = ans
        ans = (high + low)/2.0
    return ans


def is_same(q):
    global p
    print(q is p)

p = [1,2,3]
is_same(p)
def main():
    print(two_power(2,8))
    print(two_power(2,16))

if __name__ == '__main__':
    main()
