def is_prime(p):
    if p < 2:
        return False

    d = 2
    while d * d <= p:
        if p % d == 0:
            return False
        d += 1 + d%2

    return True


class Fibonacci:
    def __init__(self, index):
        if not is_prime(index):
            raise Exception("index " + str(index) + " is not prime")

        self._index = index
        prev, self._value = 1, 1

        for i in range(2, index):
            prev, self._value = self._value, prev + self._value


    def least_prime_factor(self):
        p = self._index

        if p > 2:
            dif = 4 * p
            pr1 = 4*p + 1
            pr2 = 2*p - 1

            while pr2 * pr2 <= self._value:
                if ((pr2 % 10 == 3) or (pr2 % 10 == 7)) and self._value % pr2 == 0:
                    return pr2
                elif ((pr1 % 10 == 1) or (pr1 % 10 == 9)) and self._value % pr1 == 0:
                    return pr1
                else:
                    pr1 += dif
                    pr2 += dif

            return self._value


    def prime_factorisation(self):
        p = self._index
        fac = []

        if p > 2:
            lpf = self.least_prime_factor()
            fac.append(lpf)
            val = self._value // lpf
            dif = 4 * p

            if lpf % p == 1:            # lpf is of the form 4tp + 1
                pr1 = lpf
                pr2 = lpf + 2*p - 2
            else:                       # lpf is of the form (4t - 2)p - 1
                pr1 = lpf + 2*p + 2
                pr2 = lpf

            if p > 5:
                while val >= lpf:
                    if ((pr2 % 10 == 3) or (pr2 % 10 == 7)) and val % pr2 == 0:
                        fac.append(pr2)
                        val //= pr2
                    elif ((pr1 % 10 == 1) or (pr1 % 10 == 9)) and val % pr1 == 0:
                        fac.append(pr1)
                        val //= pr1
                    else:
                        pr1 += dif
                        pr2 += dif

                        if pr1 * pr1 > val and pr2 * pr2 > val: # val is prime
                            fac.append(val)
                            break

        return fac


#fib = Fibonacci(31)
#fib = Fibonacci(37)
#fib = Fibonacci(41)
#fib = Fibonacci(43)
#fib = Fibonacci(71)
#fib = Fibonacci(81)  # not prime
#fib = Fibonacci(83)
#fib = Fibonacci(89)
#fib = Fibonacci(91)  # not prime
#fib = Fibonacci(97)
#fib = Fibonacci(101) # this has large prime factors
#fib = Fibonacci(103)
#fib = Fibonacci(107)
#fib = Fibonacci(109)
fib = Fibonacci(113)  # this has a very large prime factor
#fib = Fibonacci(119)
#fib = Fibonacci(127)
#fib = Fibonacci(227)
#fib = Fibonacci(503)
#fib = Fibonacci(907)
#fib = Fibonacci(1009)
#fib = Fibonacci(1013)
#fib = Fibonacci(1019)
#fib = Fibonacci(1319)

print(fib.least_prime_factor())
print(fib.prime_factorisation())
