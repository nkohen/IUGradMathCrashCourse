def intersection(list1,list2):
    ret = []
    list2_dict = {list2[i]:"" for i in range(len(list2))}
    for element in list1:
        if element in list2_dict and element not in ret:
            ret.append(element)
    return ret

def func_intersection(f1,f2,n):
    list1 = [f1(i) for i in range(n+1)]
    list2 = [f2(i) for i in range(n+1)]
    return intersection(list1,list2)

if __name__ == '__main__':
    print(intersection([1,2,3,"a","b","c",1],[1,3,4,4,4,"a","a"]))
