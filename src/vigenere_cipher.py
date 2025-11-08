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
    if alphabet is None or not keyword:
        return text

    clean_keyword = ''.join([c.lower() for c in keyword if c.lower() in alphabet])
    if not clean_keyword:
        return text

    result = ""
    keyword_index = 0
    for char in text:
        lower_char = char.lower()
        if lower_char in alphabet:
            key_char = clean_keyword[keyword_index % len(clean_keyword)]
            shift = alphabet.index(key_char)
            new_pos = (alphabet.index(lower_char) + shift) % len(alphabet)
            encrypted_char = alphabet[new_pos]
            result += encrypted_char.upper() if char.isupper() else encrypted_char
            keyword_index += 1
        else:
            result += char  # keep punctuation and symbols unchanged
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
    if alphabet is None or not keyword:
        return text

    clean_keyword = ''.join([c.lower() for c in keyword if c.lower() in alphabet])
    if not clean_keyword:
        return text

    result = ""
    keyword_index = 0
    for char in text:
        lower_char = char.lower()
        if lower_char in alphabet:
            key_char = clean_keyword[keyword_index % len(clean_keyword)]
            shift = alphabet.index(key_char)
            new_pos = (alphabet.index(lower_char) - shift) % len(alphabet)
            decrypted_char = alphabet[new_pos]
            result += decrypted_char.upper() if char.isupper() else decrypted_char
            keyword_index += 1
        else:
            result += char
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

    decrypted_text = vigenere_decrypt("english", encrypted_history, "himmelfarb")

    # Write to a new file
    with open("/Users/amichaiblumenfeld/cyber_grade_11/Vigenere_cipher/Vigenere_cipher/assets/jeruslaem_history_decrypted.txt", "w", encoding="utf-8") as f:
        f.write(decrypted_text)