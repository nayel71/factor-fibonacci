from nt import is_prime

class Fibonacci:
    def __init__(self, index):
        if not is_prime(index):
            raise Exception("index " + str(index) + " is not prime")

        self._index = index
        prev, self._value = 1, 1

        for i in range(2, index):
            prev, self._value = self._value, prev + self._value


    def __str__(self):
        return "Fibonacci( " + str(self._index) + " ) = " + str(self._value)


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
                        fac.append(pr2)
                        quo //= pr2
                    elif ((pr1 % 10 == 1) or (pr1 % 10 == 9)) and quo % pr1 == 0:
                        fac.append(pr1)
                        quo //= pr1
                    else:
                        pr1 += dif
                        pr2 += dif

                if quo > 1:             # quo is prime
                    fac.append(quo)

        return fac


# test
large_prime_factor = [43, 83, 97, 101, 109, 113, 127] # these indices have a large prime factor
least_prime_factor = [227, 503, 907, 1009, 1013, 1019] # prime_factorisation() may be slow for these indices

print("Prime Factorisation:")
for index in large_prime_factor:
    fib = Fibonacci(index)
    print(fib, "->", fib.prime_factorisation())

print("Least Prime Factor:")
for index in least_prime_factor :
    fib = Fibonacci(index)
    print(fib, "->", fib.least_prime_factor())
