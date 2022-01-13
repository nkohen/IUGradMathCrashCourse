# Returns the intersection of two lists, tuples, or sets
def intersection(list1,list2):
    try:
        return set(list1) & set(list2)
    except TypeError:
        print("intersection: Inputs must be lists, tuples, or sets")

def func_intersection(f1,f2,n):
    try:
        list1 = [f1(i) for i in range(n+1)]
        list2 = [f2(i) for i in range(n+1)]
        return intersection(list1,list2)
    except TypeError:
        print("func_intersection: Inputs must be functions defined on the integers")

if __name__ == '__main__':
    func_intersection(1,2,3)
