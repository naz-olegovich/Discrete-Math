from random import randint, sample, shuffle


def relations_R(A, B, list_of_women_names, list_of_men_names):
    relations_R_list = list()
    a = list()
    b = list()
    list_of_z = list()
    list_of_t = list()

    for i in A:
        if i in list_of_men_names:
            a.append(i)

    for j in B:
        if j in list_of_men_names:
            b.append(j)

    for n in sample(a, len(a)):  # n-тесть  m-зать
        num_of_z = randint(1, 2)
        for m in sample(b, len(b)):

            if m in list_of_z:  # в зятя один тесть
                continue
            if n in list_of_t:
                continue
            if [n, m] in relations_R_list:  # перевірки вже пара не входть в список
                continue
            if n == m:  # тесть не може бути тестем сам собі
                continue
            if m in A:
                continue

            list_of_t.append(n)
            list_of_z.append(m)
            relations_R_list.append([n, m])

    print('Relation R')
    print(relations_R_list)
    return relations_R_list
