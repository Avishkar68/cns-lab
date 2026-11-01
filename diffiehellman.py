
p = int(input("Enter prime number p: "))
g = int(input("Enter generator g: "))

a = int(input("Enter Alice private key: "))
b = int(input("Enter Bob private key: "))

# Generate public keys
A = pow(g, a, p)
B = pow(g, b, p)

print("Alice Public Key:", A)
print("Bob Public Key:", B)

# Generate shared secrets
key_A = pow(B, a, p)
key_B = pow(A, b, p)

print("Alice Shared Secret:", key_A)
print("Bob Shared Secret:", key_B)

if key_A == key_B:
    print("Shared Secret Matched")
else:
    print("Shared Secret Not Matched")
