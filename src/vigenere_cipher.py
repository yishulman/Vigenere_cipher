from alphabets import get_alphabet
from caesar_encrypt import caesar_encrypt
from cyber_tools import frequency_analysis, plot_frequency, print_crib_analysis


def vigenere_encrypt(lang, text, keyword):
    """
    Encrypt text using the Vigenère cipher with a keyword.
    
    Args:
        lang (str): Language ('english' or 'hebrew')
        text (str): Text to encrypt
        keyword (str): Keyword for encryption
    
    Returns:
        str: Encrypted text
    """
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
    keyword_index = 0
    
    for char in text:
        if char.lower() not in alphabet:
            result += char
            continue
            
        # Only increment keyword_index for alphabet characters
        key_char = clean_keyword[keyword_index % len(clean_keyword)]
        shift = alphabet.index(key_char.lower())
        
        char_pos = alphabet.index(char.lower())
        new_pos = (char_pos + shift) % len(alphabet)
        encrypted_char = alphabet[new_pos]
        
        if char.isupper():
            encrypted_char = encrypted_char.upper()
            
        result += encrypted_char
        keyword_index += 1  # Only increment for alphabet characters

    return result



def vigenere_decrypt(lang, text, keyword):
    """
    Decrypt text using the Vigenère cipher with a keyword.
    
    Args:
        lang (str): Language ('english' or 'hebrew')
        text (str): Text to decrypt
        keyword (str): Keyword for decryption
    
    Returns:
        str: Decrypted text
    """
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
    # Simple example of Vigenere cipher usage
        
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

    # Hebrew example
    print("\n=== Hebrew Example ===")
    hebrew_text = "שלום עולם"
    hebrew_keyword = "מפתח"
    print(f"Original: {hebrew_text}")
    print(f"Keyword: {hebrew_keyword}")

    encrypted_heb = vigenere_encrypt("hebrew", hebrew_text, hebrew_keyword)
    print(f"Encrypted: {encrypted_heb}")

    decrypted_heb = vigenere_decrypt("hebrew", encrypted_heb, hebrew_keyword)
    print(f"Decrypted: {decrypted_heb}")

    with open("/Users/amichaiblumenfeld/cyber_grade_11/Vigenere_cipher/Vigenere_cipher/assets/jeruslaem_history_encrypted.txt", "r", encoding="utf-8") as f:
        encrypted_history = f.read()

    decrypted_text = vigenere_decrypt("english", encrypted_history, "cjzcciroa")

    # Write to a new file
    with open("/Users/amichaiblumenfeld/cyber_grade_11/Vigenere_cipher/Vigenere_cipher/assets/jeruslaem_history_decrypted.txt", "w", encoding="utf-8") as f:
        f.write(decrypted_text)