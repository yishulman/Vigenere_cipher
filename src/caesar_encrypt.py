from alphabets import get_alphabet
from cyber_tools import frequency_analysis, plot_frequency



def caesar_encrypt(lang, text, shift):
    alphabet = get_alphabet(lang)
    if alphabet is None:
        return text  # Return original text if language not supported

    result = ""

    for letter in text:
        if letter.lower() in alphabet:
            letterNew = alphabet[(alphabet.index(letter.lower()) + shift) % len(alphabet)]
            if letter.isupper():
                result += letterNew.upper()
            else:
                result+=letterNew
        else:
            result+=letter

             
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
