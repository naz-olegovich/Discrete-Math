def simplified_expression(A,B,C,U):
    operation1 = (U - C) & A
    operation2 = (B) & (U-C)
    operation3 =operation1 & operation2
    return operation3