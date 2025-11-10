from alphabets import get_alphabet
from cyber_tools import frequency_analysis, plot_frequency


def caesar_encrypt(lang, text, shift):
    alphabet = get_alphabet(lang)
    if alphabet is None:
        return text  # Return original text if language not supported

    result = ""
    for char in text:
        # Store original case
        is_upper = char.isupper()
        # Work with lowercase version for consistency
        char_lower = char.lower()
        
        # If character is in alphabet, shift it
        if char_lower in alphabet:
            # Get the position of char in alphabet
            current_pos = alphabet.index(char_lower)
            # Calculate new position after shift
            new_pos = (current_pos + shift) % len(alphabet)
            # Get the shifted character
            shifted_char = alphabet[new_pos]
            # Restore original case
            result += shifted_char.upper() if is_upper else shifted_char
        else:
            # If character is not in alphabet, keep it unchanged
            result += char
            
    return result



if __name__ == "__main__":
    # Simple example usage
    with open('./assets/bible_en.txt', 'r', encoding='utf-8') as file:
            original_text = file.read()
    
    shift_value = 3
    # Encrypt the text
    encrypted_text = caesar_encrypt('english', original_text, shift_value)

    print("\nEncrypted Text Sample:")
    print(encrypted_text[:1000])  # Print the first 1000 characters of the encrypted text

    # Plot frequency analysis
    plot_frequency('english', original_text, "Frequency Analysis of Original Text", ignore_spaces=True)
    plot_frequency('english', encrypted_text, "Frequency Analysis of Encrypted Text", ignore_spaces=True)
