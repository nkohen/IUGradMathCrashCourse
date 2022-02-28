def input_num(message):
    while (True):
        try:
            num = int(input(message))
            if (num > 0):
                return num
            else:
                pass
        except ValueError:
            pass

# Here is a reference for the Euclidean algorithm
# http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html
def euclid_loop(x,y,prev):
    big = max(x, y)
    small = min(x, y)

    r = big % small
    return prev if r == 0 else euclid_loop(r, small, r)

def gcd():
    num1 = input_num("Please enter the first positive integer: ")
    num2 = input_num("Please enter the second positive integer: ")
    return euclid_loop(num1,num2,min(num1,num2))

def modular_inverse():
    num = input_num("Please enter a positive integer: ")
    mod = input_num("Please enter a modulus: ")
    return modular_inverse_loop(num % mod, mod, mod, 1, None, None, None, None)

# Here is a reference for the extended Euclidean algorithm
# http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html
# q1/p1 represent the values from the previous step
# q2/p2 represent the values from two steps prior
# loopcount records the number of iterations in order to manually set the correct values for the first two loops
def modular_inverse_loop(x,y,mod,loopcount,q1,q2,p1,p2):
    big = max(x, y)
    small = min(x, y)

    q0 = int(big / small)
    r = big % small

    if (loopcount == 1):
        p0 = 0
        q1 = None
        p1 = None
    elif (loopcount == 2):
        p0 = 1
        p1 = 0
    else:
        p0 = (p2 - p1*q2) % mod

    if (r == 1):
        pnext = 1 if loopcount == 1 else (p1 - p0*q1) % mod
        return (p0 - pnext*q0) % mod
    elif (r == 0):
        return False
    else:
        return modular_inverse_loop(small,r,mod,loopcount + 1,q0,q1,p0,p1)

if __name__ == '__main__':
    print(gcd())