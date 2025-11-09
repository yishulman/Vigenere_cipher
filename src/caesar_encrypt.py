from alphabets import get_alphabet
from cyber_tools import frequency_analysis, plot_frequency

def char_shift(lang, char, shift): #function to shift a single character by a given shifts amount
        alphabet = get_alphabet(lang)
        alphabet_len = len(alphabet)
        result = ""
        if char.lower() in alphabet: #check if character is in the alphabet
            if char.islower():
                index = alphabet.index(char.lower())
                new_index = (index + shift + alphabet_len) % alphabet_len #double the length to avoid negative index
                result = alphabet[new_index]
            elif char.isupper():
                index = alphabet.index(char.lower())
                new_index = (index + shift + alphabet_len) % alphabet_len
                result = alphabet[new_index].upper()
            else:
                result = char
        return result


def caesar_encrypt(lang, text, shift):
    alphabet = get_alphabet(lang)
    if alphabet is None:
        return text  # Return original text if language not supported
    alphabet_len = len(alphabet)
    result = ""
    for char in text:
        result += char_shift(lang, char, shift)
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
