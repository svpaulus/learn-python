from math import sqrt
import time

def is_odd_number(n):
    return n % 2 == 1


def is_prime_number(n):
    if not is_odd_number(n):
        return False
    for d in range(3, int(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True

def is_palindrome(text):
    return text == text[::-1]


assert is_palindrome("kajak")
assert not is_palindrome('Pavel')
assert sqrt(49) == 7
assert is_odd_number(13)
assert is_prime_number(13)
assert is_prime_number(997)
assert not is_prime_number(31*41)

t1 = time.time()

for n in range(2, 1000000):
    if is_prime_number(n):
        if is_palindrome(str(n)):
            print(n, end=' ', flush=True)

t2 = time.time()
elapsed = t2 - t1

print(f'TIME elapsed = {elapsed} sec')
