#Copyright CyberWolf Coding Company



encrypt_key = {'a': 'f', 'b': 'd', 'c': 'p', 'd': 'q', 'e': 's', 'f': 'w', 'g': 'r', 'h': 'z', 'i': 'm', 'j': 'a', 'k': 'g', 'l': 'i', 'm': 'c', 'n': 'l', 'o': 'y', 'p': 'h', 'q': 'u', 'r': 'n', 's': 'e', 't': 'o', 'u': 't', 'v': 'j', 'w': 'x', 'x': 'b', 'y': 'k', 'z': 'v'}

decrypt_key = {'f': 'a', 'd': 'b', 'p': 'c', 'q': 'd', 's': 'e', 'w': 'f', 'r': 'g', 'z': 'h', 'm': 'i', 'a': 'j', 'g': 'k', 'i': 'l', 'c': 'm', 'l': 'n', 'y': 'o', 'h': 'p', 'u': 'q', 'n': 'r', 'e': 's', 'o': 't', 't': 'u', 'j': 'v', 'x': 'w', 'b': 'x', 'k': 'y', 'v': 'z'}

def encrypt(message):
  encrypted_message = ""
  for letter in message:
    if letter in encrypt_key:
      encrypted_message += encrypt_key[letter]
    else:
      encrypted_message += letter
  return encrypted_message

def decrypt(encrypted_message):
  decrypted_message = ""
  for letter in encrypted_message:
    if letter in decrypt_key:
      decrypted_message += decrypt_key[letter]
    else:
      decrypted_message += letter
  return decrypted_message

while True:
    message = input('message to crypt: ')
    task = input('encrypt or decrypt? ')
    if task == 'encrypt':
        encrypted_message = encrypt(message)
        print(encrypted_message)
    
    elif task == 'decrypt':
        decrypted_message = decrypt(message)
        print(decrypted_message)
    else:
        break