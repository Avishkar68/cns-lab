
# secp256k1 curve parameters
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F

a = 0
b = 7

G = (
    55066263022277343669578718895168534326250603453777594175500187360389116729240,
    32670510020758816978083085130507043184471273380659243275938904335757337482424
)


# Point Addition
def point_add(P1, P2):

    if P1 is None:
        return P2

    if P2 is None:
        return P1

    x1, y1 = P1
    x2, y2 = P2

    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    if P1 == P2:
        slope = ((3 * x1 * x1 + a) *
                 pow(2 * y1, -1, p)) % p
    else:
        slope = ((y2 - y1) *
                 pow((x2 - x1) % p, -1, p)) % p

    x3 = (slope * slope - x1 - x2) % p
    y3 = (slope * (x1 - x3) - y1) % p

    return (x3, y3)


# Scalar Multiplication
def scalar_multiply(k, point):

    result = None
    current = point

    while k > 0:

        if k % 2 == 1:
            result = point_add(result, current)

        current = point_add(current, current)
        k = k // 2

    return result


# Main program
k1 = int(input("Enter first scalar: "))
k2 = int(input("Enter second scalar: "))

# Scalar multiplication
P1 = scalar_multiply(k1, G)
P2 = scalar_multiply(k2, G)

print("First Point:", P1)
print("Second Point:", P2)

# Point addition
R = point_add(P1, P2)

print("Point Addition Result:", R)

# Scalar multiplication of combined value
combined = scalar_multiply(k1 + k2, G)

print("Scalar Multiplication Result:", combined)

if R == combined:
    print("ECC Verification Successful")
else:
    print("ECC Verification Failed")
