<<<<<<< HEAD
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        # Check if character is an uppercase letter
        if char.isupper():
            encrypted_text += chr(((ord(char) - 65 + shift) % 26) + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            encrypted_text += chr(((ord(char) - 97 + shift) % 26) + 97)
        else:
            # For characters like spaces, punctuation, and numbers, keep them unchanged
            encrypted_text += char
    return encrypted_text

# Prompt the user for input
sentence = input("Please enter a sentence: ")
shift = 5
encrypted_sentence = caesar_cipher(sentence, shift)

# Display the encrypted result
print("The encrypted sentence is:", encrypted_sentence)

=======
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
>>>>>>> 89ea48a836bd3b5f5860836af681ecd4ee957374
