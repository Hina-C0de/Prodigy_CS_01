def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

mode = input("Encrypt or Decrypt? (e/d): ").strip().lower()
message = input("Enter message: ")
shift = int(input("Enter shift value: "))

if mode == 'd':
    shift = -shift % 26  

print("Result:", caesar_cipher(message, shift))
