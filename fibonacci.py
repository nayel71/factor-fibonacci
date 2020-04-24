import nt 

class Fibonacci:
    def __init__(self, index):
        """Create a Fibonacci object with prime index."""
        if not nt.is_prime(index):
            raise Exception(" ".join(["index", str(index), "is not prime"]))

        self._index = index
        prev, self._value = 1, 1

        for i in range(2, index):
            prev, self._value = self._value, prev + self._value


    def __str__(self):
        return "".join([self.__class__.__name__, "(", str(self._index), ")"])


    def lpf(self):
        """Return the least prime factor of self._value."""
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


    def ppf(self):
        """Return the prime power factorisation of self._value."""
        p = self._index
        ppf = {}

        if p > 2:
            lpf = self.lpf()
            ppf[lpf] = ppf.get(lpf, 0) + 1
            quo = self._value // lpf
            dif = 4 * p

            if lpf % p == 1:            # lpf is of the form 4tp + 1
                pr1 = lpf
                pr2 = lpf + 2*p - 2
            else:                       # lpf is of the form (4t - 2)p - 1
                pr1 = lpf + 2*p + 2
                pr2 = lpf

            if p > 5:
                while pr1 * pr1 <= quo or pr2 * pr2 <= quo:
                    if ((pr2 % 10 == 3) or (pr2 % 10 == 7)) and quo % pr2 == 0:
                        ppf[pr2] = ppf.get(pr2, 0) + 1
                        quo //= pr2
                    elif ((pr1 % 10 == 1) or (pr1 % 10 == 9)) and quo % pr1 == 0:
                        ppf[pr1] = ppf.get(pr1, 0) + 1
                        quo //= pr1
                    else:
                        pr1 += dif
                        pr2 += dif

                if quo > 1:             # quo is prime
                    ppf[quo] = ppf.get(quo, 0) + 1

        return ppf


    @staticmethod
    def period(n):
        """Return the length of the Pisano period modulo n."""
        if n < 2:
            return 1
    
        d = nt.ppf(n)
    
        if len(d) == 1:   # n is a prime power
            p = list(d)[0]
            e = d[p]      # n = p^e
            k = 2         # k(p)
            pre, cur = 1, 1

            while cur % p != 0:
                pre, cur = cur, pre + cur
                k += 1

            r = 0         # p^r || F_{k(p)}
            while cur % p == 0:
                cur //= p
                r += 1

            q = n         # q = p^{e-r}
            for i in range(r):
                q //= p

            if pre == 1:  # k(p^e) = p^{e-r} * k(p), pi(n) = {1,2,4} * k(n)
                return k * q
            elif k % 2 == 0:
                return 2 * k * q
            else:
                return 4 * k * q

        return nt.lcm(list(map(Fibonacci.period, map(pow, d.keys(), d.values()))))



# constants for print
LPAR = "("
RPAR = ")"
EQ = " = "

# lpf test
lpf_test = [227, 503, 907, 1009, 1013, 1019] # ppf may be slow for these indices

for index in lpf_test:
    fib = Fibonacci(index)
    print(Fibonacci.lpf.__name__, LPAR, fib, RPAR, EQ, fib.lpf(), sep = "")

# ppf test
ppf_test = [43, 83, 97, 101, 109, 113, 127]

for index in ppf_test:
    fib = Fibonacci(index)
    print(Fibonacci.ppf.__name__, LPAR, fib, RPAR, EQ, fib.ppf(), sep = "")

# period test
n = 1284000
d = nt.ppf(n)
print(nt.ppf.__name__, LPAR, n, RPAR, EQ, d, sep = "")
for prime, power in d.items():
    prime_power = pow(prime, power)
    print(Fibonacci.period.__name__, LPAR, prime, RPAR, EQ, Fibonacci.period(prime), sep = "")
    if prime_power != prime:
        print(Fibonacci.period.__name__, LPAR, prime_power, RPAR, EQ, Fibonacci.period(prime_power), sep = "")

print(Fibonacci.period.__name__, LPAR, n, RPAR, EQ, Fibonacci.period(n), sep = "")
