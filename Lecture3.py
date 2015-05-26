#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Akshay
#
# Created:     23-05-2015
# Copyright:   (c) Akshay 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def to_binary(n):
    """Convert integer n to binary string."""
    assert type(n) == type(4)
    result = ''
    isNeg = False
    if n < 0:
        isNeg = True
        n = -n
    if n == 0:
        return '0'

    while(n > 0):
        result = str(n%2) + result
        n = n>>1
    if isNeg:
        result = '-' + result
    return result



def compute_binary(x):
    print('Computing binary of '+str(x))
    p = 0
    while ((2**p)*x) %1 != 0:
        print((2**p)*x)
        p += 1
        if p > 10000:
            raise ValueError('Not possible')

    result = ''
    isNeg = False
    n = int((2**p) * x)
    print('n ='+str(n))
    if n < 0:
        isNeg = True
        n = -n
    if n == 0:
        return '0'

    while(n > 0):
        result = str(n%2) + result
        n = n>>1

    current = len(result)
    remaining = p - current
    for i in range(remaining):
        result = '0'+result

    #find decimal place
    if p == 0:
        return result
    result = result[:-p] + '.' + result[-p:]
    return result


#guess and check square root
def guess_sqrt(n,epsilon = 0.01, step_size = None):
    if step_size is None:
        step_size = epsilon**2

    ans = 0
    num_steps = 0
    while abs(ans**2 - n) >= epsilon and ans <= n:
        ans += step_size #make better guess
        num_steps += 1

    if abs(ans**2 - n) >= epsilon:
        print('Failed for step size = ' + str(step_size))
        return None
    print("number of steps = " + str(num_steps))
    return ans

def test():
    x = 23
    epsilon = 0.01
    step = 0.1
    guess = 0.0

    while abs(guess**2-x) >= epsilon:
        if guess <= x:
            guess += step
        else:
            break

    if abs(guess**2 - x) >= epsilon:
        print('failed')
    else:
        print('succeeded: ' + str(guess))





def bisection_search_sqrt(x, epsilon=0.01):
    """Compute sqrt(x) using bisection search accurate to epsilon."""
    steps = 0
    low = 0
    high = x
    while low < high:
        steps += 1
        g = (low + high)/2
        if abs(g*g - x) < epsilon:
            return g, steps
        if g*g < x:
            low = g
        else:
            high = g



    return None, "Failed"

def main():
##    print(compute_binary(44))
##    print(compute_binary(0.14))
##    guess = guess_sqrt(3025)
##    if guess is None:
##        pass
##    else:
##        print(guess)
##    test()

if __name__ == '__main__':
    main()
