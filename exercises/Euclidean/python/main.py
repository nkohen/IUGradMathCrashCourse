def get_nums():
    while(True):
        try:
            num1 = int(input("Please enter a positive integer: "))
            break
        except TypeError:
            pass
    while(True):
        try:
            num2 = int(input("Please enter a positive integer: "))
            break
        except TypeError:
            pass

    return [num1,num2]

def euclid_loop(x,y,prev):
    big = max(x, y)
    small = min(x, y)

    r = big % small
    return prev if r == 0 else euclid_loop(r, small, r)

def euclid(x,y):
    return euclid_loop(x,y,min(x,y))

def modular_inverse(num1,mod):
    return modular_inverse_loop(num1 % mod, mod, mod, 1, None, None, None, None)

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

    if (r == 1): #Issue when this is also the first iteration
        pnext = 1 if loopcount == 1 else (p1 - p0*q1) % mod
        return (p0 - pnext*q0) % mod
    elif (r == 0):
        return False
    else:
        return modular_inverse_loop(small,r,mod,loopcount + 1,q0,q1,p0,p1)

if __name__ == '__main__':
    print(modular_inverse(7,8))