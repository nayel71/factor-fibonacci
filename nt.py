"""Number Theory Module"""

def is_prime(p):
    """What the name says: check if p is prime."""
    if p < 2:
        return False

    d = 2
    while d * d <= p:
        if p % d == 0:
            return False

        d += 1 + d%2

    return True


def __gcd2(a, b):
    """Return the GCD of a and b."""
    if a < b:
        return __gcd2(b, a)
    
    if b == 0:
        return a
    
    return __gcd2(b, a % b)


def __gcd(arr):
    """Return the GCD of the elements of arr."""
    if len(arr) == 1:
        return abs(arr[0])
    
    return __gcd2(__gcd(arr[:len(arr)//2]), __gcd(arr[len(arr)//2:]))


def gcd(*args):
    """Return the GCD of args."""
    if not args:
        raise Exception("no arguments")

    return __gcd(args)


def __lcm2(a, b):
    """Return the LCM of a and b."""
    if a < b:
        return __lcm2(b, a)

    if b == 0:
        return 0

    return a*b // __gcd2(a, b)


def __lcm(arr):
    """Return the LCM of the elements of arr."""
    if len(arr) == 1:
        return abs(arr[0])
    
    return __lcm2(__lcm(arr[:len(arr)//2]), __lcm(arr[len(arr)//2:]))


def lcm(*args):
    """Return the LCM of args."""
    if not args:
        raise Exception("no arguments")

    return __lcm(args)


def ppf(n):
    """Return the prime power factorisation of n."""
    d = {}
    p = 2
    
    while n > 1:
        if n % p == 0:
            d[p] = 0
            while n % p == 0:
                n //= p
                d[p] += 1
        else:
            p += 1

    return d


# test
if __name__ == "__main__":
    tests = ((48, 8, 500, 72), (0, -4, 6), (-2, 0), (0, 0), (-1323, -1519), (2,))
    for t in tests:
        print(f"gcd{t} = {gcd(*t)}, lcm{t} = {lcm(*t)}")

    t = range(1, 10)
    l = lcm(*t)
    print(f"lcm({t}) = {l}\nppf({l}) = {ppf(l)}")
