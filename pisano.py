from nt import *

def pisano(n):
    if n < 2:
        return 1
    
    d = ppf(n)
    
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

    return lcm(list(map(pisano, map(pow, d.keys(), d.values()))))


# test
n = 1284000
d = ppf(n)
print('ppf(', n, ') =', d)
for prime, power in d.items():
    pp = pow(prime, power)
    print('pisano(', prime, ') =', pisano(prime))
    if pp != prime:
        print('pisano(', pp, ') =', pisano(pp))

print('pisano(', n, ') =', pisano(n))
