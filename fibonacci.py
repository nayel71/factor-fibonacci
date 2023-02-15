import nt 
from quadratic_integer import QuadraticIntegerRing, QuadraticInteger


class Fibonacci:
    """A class to represent a Fibonacci number."""

    def __init__(self, index):
        """Create Fibonacci number corresponding to index."""
        self._index = index
        z_phi = QuadraticIntegerRing(1, -1, "phi")
        phi = QuadraticInteger(z_phi, 0, 1)
        self._value = int(phi**(index+1))

    def __str__(self):
        return f"Fibonacci({self._index})"

    def __neg__(self):
        """Return -self."""
        return -self._value

    def __add__(self, other):
        """Return self + other."""
        if isinstance(other, int):
            return self._value + other
        if isinstance(other, Fibonacci):
            return self._value + other._value
        return NotImplemented

    def __sub__(self, other):
        """Return self - other."""
        return self + -other

    def __mul__(self, other):
        """Return self * other."""
        if isinstance(other, int):
            return self._value * other
        if isinstance(other, Fibonacci):
            return self._value * other._value
        return NotImplemented

    def __floordiv__(self, other):
        """Return self // other."""
        if isinstance(other, int):
            return self._value // other
        if isinstance(other, Fibonacci):
            return self._value // other._value
        return NotImplemented

    def __mod__(self, other):
        """Return self % other."""
        if isinstance(other, int):
            return self._value % other
        if isinstance(other, Fibonacci):
            return self._value % other._value
        return NotImplemented

    def __eq__(self, other):
        """Return self == other."""
        if isinstance(other, int):
            return self._value == other
        if isinstance(other, Fibonacci):
            return self._index == other._index
        return NotImplemented

    def __ne__(self, other):
        """Return self != other."""
        if isinstance(other, int):
            return self._value != other
        if isinstance(other, Fibonacci):
            return self._index != other._index
        return NotImplemented

    def __lt__(self, other):
        """Return self < other."""
        if isinstance(other, int):
            return self._value < other
        if isinstance(other, Fibonacci):
            return self._value < other._value
        return NotImplemented

    def __le__(self, other):
        """Return self <= other."""
        if isinstance(other, int):
            return self._value <= other
        if isinstance(other, Fibonacci):
            return self._value <= other._value
        return NotImplemented

    def __gt__(self, other):
        """Return self >= other."""
        if isinstance(other, int):
            return self._value > other
        if isinstance(other, Fibonacci):
            return self._value > other._value
        return NotImplemented

    def __ge__(self, other):
        """Return self >= other."""
        if isinstance(other, int):
            return self._value >= other
        if isinstance(other, Fibonacci):
            return self._value >= other._value
        return NotImplemented

    def __radd__(self, other):
        """Return other + self."""
        return self + other

    def __rsub__(self, other):
        """Return other - self."""
        return -self + other

    def __rmul__(self, other):
        """Return other * self."""
        return self * other

    def __rfloordiv__(self, other):
        """Return other // self."""
        if isinstance(other, int):
            return other // self._value
        if isinstance(other, Fibonacci):
            return other._value // self._value
        return NotImplemented

    def __rmod__(self, other):
        """Return other % self."""
        if isinstance(other, int):
            return other % self._value
        if isinstance(other, Fibonacci):
            return other._value % self._value
        return NotImplemented

    def __req__(self, other):
        """Return other == self."""
        return self == other

    def __pow__(self, other):
        """Return self**other."""
        if isinstance(other, int) and other >= 0:
            if other == 0:
                return 1
            if other % 2 == 0:
                sqrt = self**(other//2)
                return sqrt * sqrt
            return self * self**(other-1)
        return NotImplemented

    def characteristic_factors(self):
        """Return the characteristic factors of self."""
        ppf = nt.ppf(self._index)
        char_factor = self._value

        if self._index in (6, 12):  # Carmichael's theorem
            return {}
        if len(ppf) == 1:  # index is a prime power
            for prime, power in ppf.items():
                char_factor //= Fibonacci(prime**(power-1))
        else: 
            for prime, power in ppf.items():
                char_factor //= Fibonacci(prime**power)

        return nt.ppf(char_factor)


class FibonacciPrime(Fibonacci):
    """A class to represent a Fibonacci number with prime index."""
    
    def __init__(self, index):
        """Create object if index is prime, raise exception otherwise."""
        if not nt.is_prime(index):
            raise IndexError(f"index {index} is not prime")

        super().__init__(index)

    def lpf(self):
        """Return the least prime factor of self."""
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
        """Return the prime power factorisation of self."""
        d = {}
        p = self._index

        if p > 2:
            pr0 = self.lpf()
            d[pr0] = 1
            quo = self._value // pr0
            dif = 4 * p

            if pr0 % p == 1:  # lpf is of the form 4tp + 1
                pr1 = pr0
                pr2 = pr0 + 2*p - 2
            else:  # lpf is of the form (4t - 2)p - 1
                pr1 = pr0 + 2*p + 2
                pr2 = pr0

            if p > 5:
                while pr1 * pr1 <= quo or pr2 * pr2 <= quo:
                    if ((pr2 % 10 == 3) or (pr2 % 10 == 7)) and quo % pr2 == 0:
                        d[pr2] = d.get(pr2, 0) + 1
                        quo //= pr2
                    elif ((pr1 % 10 == 1) or (pr1 % 10 == 9)) and quo % pr1 == 0:
                        d[pr1] = d.get(pr1, 0) + 1
                        quo //= pr1
                    else:
                        pr1 += dif
                        pr2 += dif

                if quo > 1:  # quo is prime
                    d[quo] = d.get(quo, 0) + 1

        return d


def pisano_period(n):
    """Return the length of the Pisano period modulo n."""
    if n < 2:
        return 1

    d = nt.ppf(n)

    if len(d) == 1:  # n is a prime power
        p = tuple(d)[0]
        e = d[p]  # n = p^e
        k = 2  # k(p)
        pre, cur = 1, 1

        while cur % p != 0:
            pre, cur = cur, pre + cur
            k += 1

        r = 0  # p^r || F_{k(p)}
        while cur % p == 0:
            cur //= p
            r += 1

        q = n  # q = p^{e-r}
        for i in range(r):
            q //= p

        if pre == 1:  # k(p^e) = p^{e-r} * k(p), pi(n) = {1,2,4} * k(n)
            return k * q
        elif k % 2 == 0:
            return 2 * k * q
        else:
            return 4 * k * q

    return nt.lcm(*map(pisano_period, map(pow, d.keys(), d.values())))


# test
if __name__ == "__main__":
    def print_fun(fun, arg, val=None):
        """Print 
        "fun(arg) = val" if val != None, and 
        "fun(arg) = [value of fun at arg]" otherwise.
        """
        if val is None:
            print(fun.__name__, "(", arg, ")", " = ", fun(arg), sep="")
        else:
            print(fun.__name__, "(", arg, ")", " = ", val, sep="")

    # lpf
    lpf_test = [227, 503, 907, 1009, 1013, 1019] # ppf may be slow for these indices

    for index in lpf_test:
        print_fun(FibonacciPrime.lpf, FibonacciPrime(index))

    # ppf
    ppf_test = [43, 83, 97, 101, 109, 113, 127]

    for index in ppf_test:
        print_fun(FibonacciPrime.ppf, FibonacciPrime(index))

    # period
    n = 1284000
    d = nt.ppf(n)
    print_fun(nt.ppf, n, d)

    for prime, power in d.items():
        prime_power = pow(prime, power)
        print_fun(pisano_period, prime)
        if prime_power != prime:
            print_fun(pisano_period, prime_power)

    print_fun(pisano_period, n)
