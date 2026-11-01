def encrypt(text, key):
    result = ""
    key = key.upper()
    j = 0

    for ch in text.upper():
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - 65
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
            j += 1
        else:
            result += ch

    return result

def decrypt(text, key):
    result = ""
    key = key.upper()
    j = 0

    for ch in text.upper():
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - 65
            result += chr((ord(ch) - 65 - shift) % 26 + 65)
            j += 1
        else:
            result += ch

    return result

key = "UZEKJ"
text = input("Enter text: ")

encrypted = encrypt(text, key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypt(encrypted, key))