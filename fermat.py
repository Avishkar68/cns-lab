def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def fermat_test(n):
    if n < 2:
        return "Composite"
    if n == 2:
        return "Prime"
    if n % 2 == 0:
        return "Composite"

    bases = [2, 3, 5, 7, 11]

    for a in bases:
        if a < n and gcd(a, n) == 1:
            if pow(a, n - 1, n) != 1:
                return "Composite"

    return "Probably Prime"


n = int(input("Enter a number: "))
print("Fermat Test:", fermat_test(n))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def euler_test(n):
    if n < 2:
        return "Composite"
    if n == 2:
        return "Prime"
    if n % 2 == 0:
        return "Composite"

    bases = [2, 3, 5, 7, 11]

    for a in bases:
        if a < n and gcd(a, n) == 1:
            x = pow(a, (n - 1) // 2, n)

            if x != 1 and x != n - 1:
                return "Composite"

    return "Probably Prime"


n = int(input("Enter a number: "))
print("Euler Test:", euler_test(n))



def miller_rabin(n):
    if n < 2:
        return "Composite"
    if n == 2 or n == 3:
        return "Prime"
    if n % 2 == 0:
        return "Composite"

    d = n - 1
    r = 0

    while d % 2 == 0:
        d //= 2
        r += 1

    bases = [2, 3, 5, 7, 11]

    for a in bases:
        if a >= n:
            continue

        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for i in range(r - 1):
            x = pow(x, 2, n)

            if x == n - 1:
                break
        else:
            return "Composite"

    return "Probably Prime"


n = int(input("Enter a number: "))
print("Miller Rabin Test:", miller_rabin(n))
