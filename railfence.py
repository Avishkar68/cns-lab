def encrypt(text, key):
    rail = [['\n' for i in range(len(text))]
            for j in range(key)]

    row = 0
    direction = 1

    for col in range(len(text)):
        rail[row][col] = text[col]

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    result = ""

    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result += rail[i][j]

    return result


def decrypt(cipher, key):
    rail = [['\n' for i in range(len(cipher))]
            for j in range(key)]

    row = 0
    direction = 1

    for col in range(len(cipher)):
        rail[row][col] = '*'

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    index = 0

    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*':
                rail[i][j] = cipher[index]
                index += 1

    result = ""
    row = 0
    direction = 1

    for col in range(len(cipher)):
        result += rail[row][col]

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    return result


text = input("Enter message: ")
key = int(input("Enter key: "))

if key < 2 or key > len(text):
    print("Invalid key")
else:
    cipher = encrypt(text, key)
    print("Encrypted:", cipher)
    print("Decrypted:", decrypt(cipher, key))