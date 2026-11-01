def encrypt(text, key):
    cols = len(key)
    rows = (len(text) + cols - 1) // cols

    text = text.ljust(rows * cols, 'X')

    matrix = []

    for i in range(rows):
        matrix.append(list(text[i * cols:(i + 1) * cols]))

    result = ""

    order = sorted(range(cols), key=lambda i: key[i])

    for col in order:
        for row in range(rows):
            result += matrix[row][col]

    return result


def decrypt(cipher, key):
    cols = len(key)
    rows = len(cipher) // cols

    matrix = [['' for i in range(cols)]
              for j in range(rows)]

    order = sorted(range(cols), key=lambda i: key[i])

    index = 0

    for col in order:
        for row in range(rows):
            matrix[row][col] = cipher[index]
            index += 1

    result = ""

    for row in range(rows):
        for col in range(cols):
            result += matrix[row][col]

    return result.rstrip('X')


text = input("Enter message: ").replace(" ", "")
key = input("Enter key (example: 3142): ")

if not key.isdigit() or len(set(key)) != len(key):
    print("Enter a key with unique digits")
else:
    cipher = encrypt(text, key)
    print("Encrypted:", cipher)
    print("Decrypted:", decrypt(cipher, key))