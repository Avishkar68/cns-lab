a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    r = a % b
    a = b
    b = r

print("GCD =", a)