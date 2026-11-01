def encrypt(text,key):
  result=""
  for ch in text.upper():
    if ch.isalpha():
      result += key[ord(ch) - 65]
    else:
      result += ch
  return result

def decrypt(text,key):
  result=""
  for ch in text.upper():
    if ch.isalpha():
      result += chr(key.index(ch) + 65)
    else:
      result += ch
  return result
key = "HALEZQPUYJGFKNDXSOTICWBMRV"
text = input("enter a text: ")
encrypted = encrypt(text,key)
print("encrypted",encrypted)
print("decrypted",decrypt(encrypted,key))

