def inverse_mod(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1


def hill_encrypt(text, key):
    text = "".join(ch for ch in text.upper() if ch.isalpha())

    if len(text) % 2 != 0:
        text += "X"

    result = ""

    for i in range(0, len(text), 2):
        a = ord(text[i]) - 65
        b = ord(text[i + 1]) - 65

        x = (key[0][0] * a + key[0][1] * b) % 26
        y = (key[1][0] * a + key[1][1] * b) % 26

        result += chr(x + 65) + chr(y + 65)

    return result


def hill_decrypt(text, key):
    det = (key[0][0] * key[1][1] -
           key[0][1] * key[1][0]) % 26

    inv = inverse_mod(det, 26)

    if inv == -1:
        return "Inverse does not exist"

    inverse_key = [
        [(inv * key[1][1]) % 26,
         (-inv * key[0][1]) % 26],

        [(-inv * key[1][0]) % 26,
         (inv * key[0][0]) % 26]
    ]

    return hill_encrypt(text, inverse_key)


key = [[20, 25], [3, 2]]

text = input("Enter text: ")

encrypted = hill_encrypt(text, key)
print("Encrypted:", encrypted)

decrypted = hill_decrypt(encrypted, key)
print("Decrypted:", decrypted)

