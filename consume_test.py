import timeit
import collections
from random import random
from itertools import islice

def consumeA(iterator, n):
    "Advance the iterator n-steps ahead. If n is none, consume entirely."
    # Use functions that consume iterators at C speed.
    if n is not None:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n),None)
    else:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)

def consumeB(iterable, n):
    for i in range(n):
        next(iterable, None)

if __name__=='__main__':
    print(timeit.timeit('a = iter([random() for i in range(500)]); consumeA(a, 50)', setup="from __main__ import consumeA, random", number=50000))
    print(timeit.timeit('a = iter([random() for i in range(500)]); consumeB(a, 50)', setup="from __main__ import consumeB, random", number=50000))
#   time(A) ~= time(B), but always time(B) > time(A)
