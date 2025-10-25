import matplotlib.pyplot as plt
from alphabets import get_alphabet



def caesar_encrypt(lang, text, shift):
    alphabet = get_alphabet(lang)
    if alphabet is None:
        return text  # Return original text if language not supported

    result = ""
    
    return result


def frequency_analysis(lang, text):
        alphabet = get_alphabet(lang)
        if alphabet is None:
            return {}  # Return empty dict if language not supported

        # Initialize frequency dictionary with all alphabet characters set to 0
        frequency_dict = {char: 0 for char in alphabet}
        
        return frequency_dict
    


def plot_frequency(lang, text, title="Character Frequency Analysis"):
    """
    Plot the frequency of characters in the given text.
    
    Args:
        lang (str): Language ('english' or 'hebrew')
        text (str): Text to analyze
        title (str): Title for the plot
    """
    frequency_dict = frequency_analysis(lang, text)
    
    characters = list(frequency_dict.keys())
    frequencies = list(frequency_dict.values())
    
    # Calculate total characters to convert to percentages
    total_chars = sum(frequencies)
    percentages = [freq / total_chars * 100 for freq in frequencies]
    
    plt.figure(figsize=(12, 6))
    plt.bar(characters, percentages)
    plt.xlabel('Characters')
    plt.ylabel('Percentage (%)')
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Simple example usage
    original_text = "Hello World"
    shift_value = 3

    print(f"Original text: {original_text}")

    # Encrypt the text
    encrypted_text = caesar_encrypt('english', original_text, shift_value)
    print(f"Encrypted text (shift {shift_value}): {encrypted_text}")

    # Decrypt by shifting back
    decrypted_text = caesar_encrypt('english', encrypted_text, -shift_value)
    print(f"Decrypted text: {decrypted_text}")

    # Show frequency analysis
    print("\nFrequency analysis of encrypted text:")
    freq_dict = frequency_analysis('english', encrypted_text)
    for char, count in freq_dict.items():
        if count > 0:
            print(f"{char}: {count}")

    # Plot frequency analysis
    plot_frequency('english', encrypted_text, "Frequency Analysis of Encrypted Text")
