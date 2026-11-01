a = int(input("Enter a: "))
p = int(input("Enter prime number p: "))

if p > 1 and a % p != 0:
    result = pow(a, p - 1, p)
    print("Result:", result)

    if result == 1:
        print("Fermat's Little Theorem is satisfied")
    else:
        print("Theorem condition is not satisfied")
else:
    print("Invalid input")