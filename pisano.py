from nt import *

def pisano(n):
    if n < 2:
        return 1
    
    d = ppf(n)
    
    if len(d) == 1: # n is a prime power
        k = 2 # k(n)
        pre, cur = 1, 1

        while cur != 0:
            pre, cur = cur % n, (pre + cur) % n
            k += 1

        if pre == 1:
            return k
        elif k % 2 == 0:
            return 2 * k
        else:
            return 4 * k

    return lcm(list(map(pisano, map(pow, d.keys(), d.values()))))


# test
n = 1284000
d = ppf(n)
print('ppf(', n, ') =', d)
for prime, power in d.items():
    pp = pow(prime, power)
    print('pisano(', pp, ') =', pisano(pp))

print('pisano(', n, ') =', pisano(n))
