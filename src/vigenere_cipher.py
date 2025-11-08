from alphabets import get_alphabet
from caesar_encrypt import caesar_encrypt
from cyber_tools import frequency_analysis, plot_frequency, print_crib_analysis


def vigenere_encrypt(lang, text, keyword):


    alphabet = get_alphabet(lang)
    if alphabet is None:
        return text  # Return original text if language not supported
    
    if not keyword:
        return text  # Return original text if no keyword provided
    
    # Clean the keyword to only include valid alphabet characters
    clean_keyword = ''.join([char.lower() for char in keyword if char.lower() in alphabet])
    if not clean_keyword:
        return text  # Return original text if keyword has no valid characters
    
    result = ""
    n = len(alphabet)
    # Precompute shifts for the cleaned keyword
    shifts = [alphabet.index(k) for k in clean_keyword]
    key_len = len(shifts)
    key_pos = 0

    for ch in text:
        low = ch.lower()
        if low in alphabet:
            idx = alphabet.index(low)
            shift = shifts[key_pos % key_len]
            new_char = alphabet[(idx + shift) % n]
            result += new_char.upper() if ch.isupper() else new_char
            key_pos += 1
        else:
            result += ch

    return result





def vigenere_decrypt(lang, text, keyword):

    alphabet = get_alphabet(lang)
    if alphabet is None:
        return text
    
    if not keyword:
        return text  
    

    clean_keyword = ''.join([char.lower() for char in keyword if char.lower() in alphabet])
    if not clean_keyword:
        return text 
    
    result = ""
    keyword_len = len(clean_keyword)
    alphabet_len = len(alphabet)
    
    for i, char in enumerate(text):
        lower_char = char.lower()
        if lower_char in alphabet:
            # Calculate shift based on keyword character
            key_index = alphabet.index(clean_keyword[i % keyword_len])
            char_index = alphabet.index(lower_char)
            decrypted_index = (char_index - key_index) % alphabet_len
            decrypted_char = alphabet[decrypted_index]
            # Preserve original case
            if char.isupper():
                decrypted_char = decrypted_char.upper()
            result += decrypted_char
        else:
            result += char  # Non-alphabet characters are unchanged
    
    return result





if __name__ == "__main__":
        
    # English example
    print("=== English Example ===")
    original_text = "Hello World"
    keyword = "key"
    print(f"Original: {original_text}")
    print(f"Keyword: {keyword}")

    encrypted = vigenere_encrypt("english", original_text, keyword)
    print(f"Encrypted: {encrypted}")

    decrypted = vigenere_decrypt("english", encrypted, keyword)
    print(f"Decrypted: {decrypted}")





