# -*- coding: UTF-8 -*-

from itertools import compress
import numpy as np


def rwh_primes1v1(n):
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = bytearray((n - i * i - 1) // (2 * i) + 1)
    return [2, *compress(range(3, n, 2), sieve[1:])]


def primesfrom2to(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n // 3 + (n % 6 == 2), dtype=np.bool)
    sieve[0] = False
    for i in range(int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) // 3)::2 * k] = False
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = False
    a = np.r_[2, 3, ((3 * np.nonzero(sieve)[0] + 1) | 1)]
    return a


# Prime numbers from 0 to N
N = 1000
N0 = 1000000
N1 = 1000000000
# n1 = rwh_primes1v1(N)
n = primesfrom2to(N)
n0 = primesfrom2to(N0)
n0_ = str(len(n0))
n1 = primesfrom2to(N1)
n1_ = str(len(n1))
# assert len(n1) == len(n2)
n_ = str(len(n))
print(n1_, n0_, n_)
