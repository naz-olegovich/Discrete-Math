from random import randint, sample


def relations_S(A, B, list_of_men_names, R):
    relations_S_list = list()
    list_of_R = list()
    for i in R:
        for j in i:
            list_of_R.append(j)

        for a in A:
            num_of_children = randint(1, 2)
            for b in sample(B, len(B)):
                if a in list_of_men_names:
                    x = len(list(filter(lambda R: R[0] == a, relations_S_list)))
                    if list(filter(lambda R: R[1] == b, relations_S_list)):
                        continue
                    if b in list_of_R:
                        continue
                    if x >= num_of_children:
                        continue
                    if b in A:
                        continue

                    relations_S_list.append([a, b])
    print("S relation")
    print(relations_S_list)
    return relations_S_list
