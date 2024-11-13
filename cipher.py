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

