def initial_expression(A,B,C,U):
    operation1 = A - C
    operation2 = B - C
    operation3 = (U - C).union(B)        
    operation4 = (U - C) & operation1
    operation5 = operation4 & operation2
    operation6 = operation5 & operation3

    return operation6