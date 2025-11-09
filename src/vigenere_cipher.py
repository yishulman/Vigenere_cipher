from caesar_encrypt import char_shift
from alphabets import get_alphabet
from cyber_tools import frequency_analysis, plot_frequency, print_crib_analysis
def crib_func():
    my_file = open(r'C:\Users\user\Documents\firstassignment\Vigenere_cipher\src\assets\jeruslaem_history_encrypted.txt', "r", encoding="utf-8")
    ciphertext = my_file.read()
    my_file.close()
    print_crib_analysis(ciphertext, " Jerusalem ")
crib_func()

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
    key_index = 0
    for char in text:
        if char.lower() in alphabet:
            shifts = alphabet.index(clean_keyword[key_index % len(clean_keyword)]) #get shifts amount from key's character
            result += char_shift(lang, char, shifts)
            key_index += 1
        else:
            result += char  
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
    key_index = 0
    for char in text:
        if char.lower() in alphabet:
            shifts = alphabet.index(clean_keyword[key_index % len(clean_keyword)])
            result += char_shift(lang, char, -shifts) #negative shifts for decryption
            key_index += 1
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

def print_decrypted_jerusalem_history():
    my_file = open(r'C:\Users\user\Documents\firstassignment\Vigenere_cipher\src\assets\jeruslaem_history_encrypted.txt', "r", encoding="utf-8")
    ciphertext = my_file.read()
    my_file.close()
    print(vigenere_decrypt("english", ciphertext, "himmelfarb"))
print_decrypted_jerusalem_history()
