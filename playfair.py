def create_matrix(key):
    chars = ""

    for ch in key.upper() + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch == "J":
            ch = "I"

        if ch.isalpha() and ch not in chars:
            chars += ch

    return [list(chars[i:i+5]) for i in range(0, 25, 5)]


def find_position(matrix, ch):
    if ch == "J":
        ch = "I"

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join(ch for ch in text if ch.isalpha())

    result = ""
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 == len(text):
            b = "X"
            i += 1
        elif text[i] == text[i + 1]:
            b = "X"
            i += 1
        else:
            b = text[i + 1]
            i += 2

        result += a + b

    return result


def playfair(text, key, mode):
    matrix = create_matrix(key)
    text = prepare_text(text)
    result = ""

    shift = 1 if mode == "encrypt" else -1

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1 + shift) % 5]
            result += matrix[r2][(c2 + shift) % 5]

        elif c1 == c2:
            result += matrix[(r1 + shift) % 5][c1]
            result += matrix[(r2 + shift) % 5][c2]

        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


key = "UZEKJ"
text = input("Enter text: ")

encrypted = playfair(text, key, "encrypt")
print("Encrypted:", encrypted)

decrypted = playfair(encrypted, key, "decrypt")
print("Decrypted:", decrypted)