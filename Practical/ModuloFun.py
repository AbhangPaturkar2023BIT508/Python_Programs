def ModuloFun(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero");
    return numerator - (numerator // denominator) * denominator;
    # quotient = numerator // denominator
    # mul = quotient * denominator;
    # return int(numerator - mul);

print(ModuloFun(51,10))