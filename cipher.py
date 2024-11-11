def caesar_cipher(text, shift=5):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            # Calculate the shift within alphabetical bounds
            offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_text += encrypted_char
        else:
            # Keep special characters unchanged
            encrypted_text += char
    return encrypted_text

# Get input
text = input("Please enter a sentence: ")
encrypted_text = caesar_cipher(text)
print("The encrypted sentence is:", encrypted_text)
