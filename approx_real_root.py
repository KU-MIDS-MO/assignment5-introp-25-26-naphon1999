import numpy as np

def approx_real_root(coeffs, interval):
    def f(x):
        c0, c1, c2, c3 = coeffs
        return c0 + c1*x + c2*x**2 + c3*x**3

    a, b = interval
    fa = f(a)

    for _ in range(100):
        c = (a+b)/2
        fc = f(c)

        if abs(fc) < 1*10**-9 or (b-a)/2 < 1*10**-9:
            return c      
        if fa*fc < 0:
            b = c
        else:
            a = c
    
    return (a+b)/2
