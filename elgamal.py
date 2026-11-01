
def mod_inverse(a, p):
    for x in range(1, p):
        if (a * x) % p == 1:
            return x
    return -1


p = int(input("Enter prime p: "))
g = int(input("Enter generator g: "))

# Private key
x = int(input("Enter private key x: "))

# Public key
y = pow(g, x, p)

print("Public Key:", y)
print("Private Key:", x)

message = int(input("Enter message: "))
k = int(input("Enter temporary key k: "))

if message <= 0 or message >= p:
    print("Message must be between 1 and p-1")
else:
    # Encryption
    c1 = pow(g, k, p)
    shared = pow(y, k, p)
    c2 = (message * shared) % p

    print("Ciphertext C1:", c1)
    print("Ciphertext C2:", c2)

    # Decryption
    shared = pow(c1, x, p)
    inverse = mod_inverse(shared, p)

    decrypted = (c2 * inverse) % p

    print("Decrypted Message:", decrypted)
