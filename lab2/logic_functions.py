import copy

def unite(A, B):
    result = list()
    for i in A:
        result.append(i)
    for j in B:
        result.append(j)
    print('Union func was executed')
    return result


def intersect(R, S):
    result = []
    for i in R:
        if i in S:
            result.append(i)
    print('Intersection function was executed')
    return result


def difference_f(a, b):
    print('Difference function was executed')
    return list(filter(lambda i: i not in b, a))

def addition(R, A, B):
    print('Addition function was executed')
    A = list(A)
    B =list(B)
    R = list(R)
    U = list()
    for i in A:
        for j in B:
            U.append([i, j])
    for i in U:
        if i in R:
            U.remove(i)
    return U

def inverse_f(S):
    print('Inverse function was executed')
    S1 = copy.deepcopy(S)
    for i in S1:
        i[0], i[1] = i[1], i[0]

    return S1
