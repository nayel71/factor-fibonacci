# number theory module

def is_prime(p):
    if p < 2:
        return False

    d = 2
    
    while d * d <= p:
        if p % d == 0:
            return False

        d += 1 + d%2

    return True


def __gcd(a, b):
    if a < b:
        return __gcd(b, a)
    
    if a % b == 0:
        return b
    
    return __gcd(b, a % b)


def gcd(arr):
    """Return the GCD of the elements of arr."""
    if len(arr) == 1:
        return arr[0]
    
    return __gcd(gcd(arr[:len(arr)//2]), gcd(arr[len(arr)//2:]))


def __lcm(a, b):
    return a*b // __gcd(a, b)


def lcm(arr):
    """Return the LCM of the elements of arr."""
    if len(arr) == 1:
        return arr[0]
    
    return __lcm(lcm(arr[:len(arr)//2]), lcm(arr[len(arr)//2:]))


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
