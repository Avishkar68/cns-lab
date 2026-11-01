n = int(input("Enter number of equations: "))

a = []
m = []

for i in range(n):
    a.append(int(input("Enter remainder: ")))
    m.append(int(input("Enter modulus: ")))

# Calculate product of moduli
M = 1

for x in m:
    M = M * x

result = 0

for i in range(n):
    Mi = M // m[i]

    inverse = pow(Mi, -1, m[i])

    result += a[i] * Mi * inverse

result = result % M

print("Final Answer:", result)