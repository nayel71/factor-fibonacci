def factor_fibonacci(p):
    if not is_prime(p):
        print p, "is not prime"
        return

    fibp = fibonacci(p)
    can1 = 4 * p + 1
    can2 = 2 * p - 1
    diff = 4 * p

    while can2 * can2 <= fibp:
        if is_prime(can2) and ((can2 % 10 == 3) or (can2 % 10 == 7)) and fibp % can2 == 0:
            print "The least prime factor of Fibonacci(", p, ") =", fibp, "is", can2
            return
        if is_prime(can1) and ((can1 % 10 == 1) or (can1 % 10 == 9)) and fibp % can1 == 0:
            print "The least prime factor of Fibonacci(", p, ") =", fibp, "is", can1
            return

        can1 += diff
        can2 += diff

    print "Fibonacci(", p, ") =", fibp, "is prime"
