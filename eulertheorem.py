def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def phi(n):
    count = 0

    for i in range(1, n + 1):
        if gcd(i, n) == 1:
            count += 1

    return count


a = int(input("Enter a: "))
n = int(input("Enter n: "))

if gcd(a, n) == 1:
    result = pow(a, phi(n), n)
    print("Euler Result:", result)
else:
    print("GCD must be 1")