def ModuloFun(numerator, denominator):
    quotient = numerator // denominator
    mul = quotient * denominator;
    return int(numerator - mul);

print(ModuloFun(-51,-10))