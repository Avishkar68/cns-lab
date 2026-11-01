
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return -1


# Key Generation
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

if not is_prime(p) or not is_prime(q) or p == q:
    print("Enter two different prime numbers")

else:
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2

    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    if e >= phi:
        print("No valid RSA public exponent for these primes")

    else:
        d = mod_inverse(e, phi)

        print("Public Key:", e, n)
        print("Private Key:", d, n)

        # Find digits needed to represent one byte
        block_size = 0
        capacity = 1

        while capacity <= 255:
            capacity *= n
            block_size += 1

        # Encryption
        message = input("Enter any message: ")
        data = message.encode("utf-8")

        encrypted = []

        for byte in data:
            digits = []

            for i in range(block_size):
                digits.append(byte % n)
                byte //= n

            digits.reverse()

            for digit in digits:
                encrypted.append(pow(digit, e, n))

        print("Encrypted:", encrypted)

        # Decryption
        decrypted_bytes = bytearray()

        for i in range(0, len(encrypted), block_size):
            block = encrypted[i:i + block_size]

            number = 0

            for value in block:
                digit = pow(value, d, n)
                number = number * n + digit

            decrypted_bytes.append(number)

        decrypted = decrypted_bytes.decode("utf-8")

        print("Decrypted:", decrypted)
