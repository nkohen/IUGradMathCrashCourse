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

    return([num1,num2])

def euclid_loop(x,y,prev):
    big = max(x, y)
    small = min(x, y)

    r = big % small
    return (prev if r == 0 else euclid_loop(r, small, r))

def euclid(x,y):
    return(euclid_loop(x,y,min(x,y)))

if __name__ == '__main__':
    nums = get_nums()
    print(euclid(nums[0],nums[1]))