def caeser_encrypt(text,key):
  result = ""
  for ch in text:
    if ch.isalpha():
      result += chr((ord(ch) - 65 + key) % 26 + 65)
    else:
      result += ch
  return result
def caeser_decrypt(text, key):
  return caeser_encrypt(text, -key)

CAESER_KEY = 22

text = input("enter a text:").upper()
encrypted = caeser_encrypt(text, CAESER_KEY)
print(encrypted)

decrypted = caeser_decrypt(encrypted, CAESER_KEY)
print(decrypted)

