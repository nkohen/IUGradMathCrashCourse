# Returns the intersection of two lists, tuples, or sets
def intersection(list1,list2):
    try:
        return set(list1) & set(list2)
    except TypeError:
        print("intersection: Inputs must be lists, tuples, or sets, inputted: ",list1, " ", list2)

# Input two functions defined on the nonnegative integers
# Returns the intersection of f1 and f2 applied to 0,1,...,n
def func_intersection(f1,f2,n):
    try:
        list1 = [f1(i) for i in range(n+1)]
        list2 = [f2(i) for i in range(n+1)]
        return intersection(list1,list2)
    except TypeError:
        print("func_intersection: Inputs must be functions defined on the integers, inputted: ",f1, " ",f2)

if __name__ == '__main__':
    def f1(n):
        return n ** 2
    def f2(n):
        return n
    print(func_intersection(f1,f2,10))