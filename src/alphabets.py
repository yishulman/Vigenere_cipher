"""
Alphabet definitions for different languages used in cipher implementations.
"""

# English alphabet in lowercase
english_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

# Hebrew alphabet
hebrew_alphabet = ['א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'כ', 'ל', 'מ', 'ם', 'נ', 'ן', 'ס', 'ע', 'פ', 'ף', 'צ', 'ץ', 'ק', 'ר', 'ש', 'ת', ' ']

# Dictionary mapping language names to their alphabets
ALPHABETS = {
    'english': english_alphabet,
    'hebrew': hebrew_alphabet
}


def get_alphabet(language):
    """
    Get the alphabet for a specific language.
    
    Args:
        language (str): Language name ('english' or 'hebrew')
    
    Returns:
        list: List of characters in the alphabet, or None if language not supported
    """
    return ALPHABETS.get(language.lower())


def get_supported_languages():
    """
    Get a list of all supported languages.
    
    Returns:
        list: List of supported language names
    """
    return list(ALPHABETS.keys())