
def factorial(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result


def factorial2(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


def factorial3(n):
    if n == 1:
        return 1
    else:
        return n*factorial3(n-1)


assert factorial3(1) == 1
assert factorial3(2) == 2
assert factorial3(3) == 6
assert factorial3(4) == 24
assert factorial3(5) == 120
print('OK')
