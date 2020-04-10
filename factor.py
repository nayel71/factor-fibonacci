def isprime(p):
    if p < 2:
        return False

    x = 2
    while x * x < p:
        if p % x == 0:
            return False
        x += 1

    return True

def fibonacci(n):
    prv, cur = 1, 1

    for i in range(2, n):
        prv, cur = cur, prv + cur

    return cur

def factor_fibonacci(p):
    if not isprime(p):
        print(p, "is not prime")
        return

    fibp = fibonacci(p)
    can1 = 4 * p + 1
    can2 = 2 * p - 1
    diff = 4 * p

    while can2 * can2 <= fibp:
        if ((can2 % 10 == 3) or (can2 % 10 == 7)) and fibp % can2 == 0 and isprime(can2):
            print("The least prime factor of Fibonacci(", p, ") =", fibp, "is", can2)
            return
        if ((can1 % 10 == 1) or (can1 % 10 == 9)) and fibp % can1 == 0 and isprime(can1):
            print("The least prime factor of Fibonacci(", p, ") =", fibp, "is", can1)
            return

        can1 += diff
        can2 += diff

    print("Fibonacci(", p, ") =", fibp, "is prime")


factor_fibonacci(31)
factor_fibonacci(37)
factor_fibonacci(41)
factor_fibonacci(43)
factor_fibonacci(71)
factor_fibonacci(83)
factor_fibonacci(89)
factor_fibonacci(91)
factor_fibonacci(97)
factor_fibonacci(101)
factor_fibonacci(103)
factor_fibonacci(107)
factor_fibonacci(109)
factor_fibonacci(113)
factor_fibonacci(119)
factor_fibonacci(127)
factor_fibonacci(227)
