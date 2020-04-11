def is_prime(p):
    if p < 2:
        return False

    d = 2
    while d * d < p:
        if p % d == 0:
            return False
        d += 1 + d % 2

    return True

def fibonacci(n):
    prv, cur = 1, 1

    for i in range(2, n):
        prv, cur = cur, prv + cur

    return cur

def factor_fibonacci(p):
    if not is_prime(p):
        print(p, "is not prime")
        return

    fib = fibonacci(p)
    pr1 = 4 * p + 1
    pr2 = 2 * p - 1
    dif = 4 * p

    while pr2 * pr2 <= fib:
        if ((pr2 % 10 == 3) or (pr2 % 10 == 7)) and fib % pr2 == 0:
            print("The least prime factor of Fibonacci(", p, ") =", fib, "is", pr2)
            return

        if ((pr1 % 10 == 1) or (pr1 % 10 == 9)) and fib % pr1 == 0:
            print("The least prime factor of Fibonacci(", p, ") =", fib, "is", pr1)
            return

        pr1 += dif
        pr2 += dif

    print("Fibonacci(", p, ") =", fib, "is prime")


#factor_fibonacci(31)
#factor_fibonacci(37)
#factor_fibonacci(41)
#factor_fibonacci(43)
#factor_fibonacci(71)
#factor_fibonacci(83)
#factor_fibonacci(89)
#factor_fibonacci(91)
#factor_fibonacci(97)
#factor_fibonacci(101)
#factor_fibonacci(103)
#factor_fibonacci(107)
#factor_fibonacci(109)
#factor_fibonacci(113)
#factor_fibonacci(119)
#factor_fibonacci(127)
#factor_fibonacci(227)
factor_fibonacci(503)
