def  intersect(A,B):
    list = []
    for i in A:
        if i in B:
            list.append(i)
    return set(list)

