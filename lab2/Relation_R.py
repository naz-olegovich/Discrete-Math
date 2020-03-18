from random import randint, sample, shuffle

def relations_R(A, B, list_of_women_names, list_of_men_names, S):
    relations_R_list = list()
    a = list()
    b = list()
    #################################################################################################
    list_dad_with_daughter = list(filter(lambda daughter: daughter[1] in list_of_women_names, S))
    list_dad_with_sun = list(filter(lambda sun: sun[1] in list_of_men_names, S))
    list_of_women_dads = list()  # список бать жінок
    list_of_men_dads = list()  # список бать чоловіків
    list_of_t = list()  # список  тестів
    list_of_z = list()  # список зятів

    for i in range(len(list_dad_with_daughter)):
        list_of_women_dads.append(list_dad_with_daughter[i][0])

    for i in range(len(list_dad_with_sun)):
        list_of_men_dads.append(list_dad_with_sun[i][0])



    for i in A:
        if i in list_of_men_names:
            a.append(i)

    for j in B:
        if j in list_of_men_names:
            b.append(j)
    #################################################################################################

    for n in sample(a,len(a)):  # n-тесть  m-зать


        #rndt = randint(1, 2)  # рандомна кількість зятів в тестя

        for m in sample(b,len(b)):
            if (n in list_of_men_dads):  # тесть не може бути батьком чоловіка( заберає багато суперечностей)
                for i in list_dad_with_sun:
                    if i[1] == m:
                        continue

            if list_of_women_dads.count(n) <= list_of_t.count(n):  # у тестя стільки зятів, скільки в нього дочок, може менше, але не більше
                continue

            if m in list_of_z:  # в зятя один тесть
                continue

            if m in list_of_women_dads:  # зять не може бути синоим тестю
                continue

            # if int(list_of_t.count(n)) >= rndt:  # рандомна кількість зятів в тестя
            #     continue

            if [n, m] in relations_R_list:  # перевірки вже пара не входть в список
                continue
            if n == m:  # тесть не може бути тестем сам собі
                continue


            list_of_t.append(n)
            list_of_z.append(m)
            relations_R_list.append([n, m])
    print('Relation R')
    print(relations_R_list)
    return relations_R_list