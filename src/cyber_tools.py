"""
Cybersecurity and cryptanalysis tools for cipher analysis.
"""

from alphabets import get_alphabet

def vigenere_crib_search(ciphertext, crib, lang='english'):
    """
    Perform a crib search on Vigenere cipher to find potential key fragments.
    
    Args:
        ciphertext (str): The encrypted text
        crib (str): Known plaintext word/phrase to search for
        lang (str): Language ('english' or 'hebrew')
    
    Returns:
        list: List of tuples (position, key_fragment, decrypted_window)
    """
    alphabet = get_alphabet(lang)
    if alphabet is None:
        return []
    
    # Clean inputs
    ciphertext = ciphertext.lower()
    crib = crib.lower()
    
    results = []
    crib_length = len(crib)
    
    # Slide the crib across the ciphertext
    for i in range(len(ciphertext) - crib_length + 1):
        window = ciphertext[i:i + crib_length]
        key_fragment = ""
        
        # Calculate potential key fragment
        valid = True
        for j in range(crib_length):
            if window[j] not in alphabet or crib[j] not in alphabet:
                valid = False
                break
            
            # Calculate key character: K = C - P (mod alphabet_size)
            cipher_idx = alphabet.index(window[j])
            plain_idx = alphabet.index(crib[j])
            key_idx = (cipher_idx - plain_idx) % len(alphabet)
            key_fragment += alphabet[key_idx]
        
        if valid:
            results.append((i, key_fragment, window))
    
    return results


def analyze_crib_results(results):
    """
    Analyze crib search results and count unique key fragments.
    
    Args:
        results (list): Results from vigenere_crib_search
    
    Returns:
        dict: Dictionary with key fragments and their counts
    """
    key_counts = {}
    
    for position, key_fragment, window in results:
        if key_fragment in key_counts:
            key_counts[key_fragment]['count'] += 1
            key_counts[key_fragment]['positions'].append(position)
        else:
            key_counts[key_fragment] = {
                'count': 1,
                'positions': [position]
            }
    
    return key_counts


def print_crib_analysis(ciphertext, crib, lang='english', top_n=10):
    """
    Perform crib search and display results with unique key fragments.
    
    Args:
        ciphertext (str): The encrypted text
        crib (str): Known plaintext word/phrase to search for
        lang (str): Language ('english' or 'hebrew')
        top_n (int): Number of top results to display
    """
    print(f"\nVigenere Crib Search Analysis")
    print("=" * 70)
    print(f"Crib: '{crib}'")
    print(f"Ciphertext length: {len(ciphertext)}")
    print(f"Language: {lang}")
    print("=" * 70)
    
    results = vigenere_crib_search(ciphertext, crib, lang)
    
    if not results:
        print("No matches found for the crib.")
        return
    
    print(f"\nTotal possible positions: {len(results)}")
    
    key_counts = analyze_crib_results(results)
    
    # Sort by count (descending)
    sorted_keys = sorted(key_counts.items(), key=lambda x: x[1]['count'], reverse=True)
    
    print(f"\nUnique key fragments found: {len(sorted_keys)}")
    print("=" * 70)
    print(f"{'Key Fragment':<20} {'Count':<10} {'Positions'}")
    print("-" * 70)
    
    for key_fragment, data in sorted_keys[:top_n]:
        positions_str = ', '.join(map(str, data['positions'][:5]))
        if len(data['positions']) > 5:
            positions_str += f", ... ({len(data['positions'])} total)"
        print(f"{key_fragment:<20} {data['count']:<10} {positions_str}")
    
    print("=" * 70)
    
    # Show most likely key fragment
    if sorted_keys:
        most_common = sorted_keys[0]
        print(f"\nMost frequent key fragment: '{most_common[0]}' (appears {most_common[1]['count']} times)")
        print(f"This suggests the key repeats with these characters at corresponding positions.")



def frequency_analysis(lang, text, ignore_spaces=False):
    """
    Perform frequency analysis on the given text.
    
    Args:
        lang (str): Language ('english' or 'hebrew')
        text (str): Text to analyze
    
    Returns:
        dict: Dictionary with character frequencies
    """
    alphabet = get_alphabet(lang)
    if alphabet is None:
        return {}  # Return empty dict if language not supported

    # Initialize frequency dictionary with all alphabet characters set to 0
    frequency_dict = {char: 0 for char in alphabet}
    
    # Count occurrences of each character in the text
    for char in text.lower():
        if char in alphabet:
            frequency_dict[char] += 1

    if ignore_spaces:
        frequency_dict.pop(' ', None)  # Remove space from frequency dict if ignored

    return frequency_dict


def plot_frequency(lang, text, title="Character Frequency Analysis", ignore_spaces=False):
    """
    Plot the frequency of characters in the given text using text-based visualization.
    
    Args:
        lang (str): Language ('english' or 'hebrew')
        text (str): Text to analyze
        title (str): Title for the plot
    """
    frequency_dict = frequency_analysis(lang, text, ignore_spaces=ignore_spaces)
    
    characters = list(frequency_dict.keys())
    frequencies = list(frequency_dict.values())
    
    # Calculate total characters to convert to percentages
    total_chars = sum(frequencies)
    if total_chars == 0:
        print("No alphabet characters found in the text.")
        return
    
    percentages = [freq / total_chars * 100 for freq in frequencies]
    
    # Text-based plot
    print(f"\n{title}")
    print("=" * 70)
    
    # Find the maximum percentage for scaling
    max_percentage = max(percentages) if percentages else 0
    
    # Define bar width in characters (50 chars for 100%)
    max_bar_width = 50
    
    # Print each character with its bar
    for char, freq, pct in zip(characters, frequencies, percentages):
        # Calculate bar length
        if max_percentage > 0:
            bar_length = int((pct / max_percentage) * max_bar_width)
        else:
            bar_length = 0
        
        # Create the bar
        bar = '█' * bar_length
        
        # Display character (handle space specially)
        display_char = "'space'" if char == ' ' else char
        
        # Print the bar chart line
        print(f"{display_char:>7} | {bar} {pct:6.2f}% ({freq} chars)")
    
    print("=" * 70)
    print(f"Total characters: {total_chars}\n")




from collections import Counter
import re

# --- Read + clean ciphertext ---
with open("/Users/amichaiblumenfeld/cyber_grade_11/Vigenere_cipher/Vigenere_cipher/assets/jeruslaem_history_encrypted.txt", "r", encoding="utf-8") as f:
    ciphertext = re.sub(r'[^a-zA-Z ]', '', f.read()).lower()

# --- Cribs ---
cribs = ["Jerusalem", "Israel", "second temple", "temple", "David", "Solomon", "Babylon",
         "exile", "covenant", "prophet", "king", "holy", "mountain", "priest", "sacrifice",
         "the", "and", "that", "bce", "jewish", "ce", "acd"]

# --- Collect all fragments ---
all_results = [res for crib in cribs for res in vigenere_crib_search(ciphertext, crib.lower(), lang='english')]
if not all_results: exit("No fragments found from any crib.")

# --- Generate candidate keys & score ---
words = ['jerusalem','the','israel','temple','david']
candidate_keys = []
for key_len in range(4, 17):
    counters = [Counter() for _ in range(key_len)]
    for pos, keyfrag, _ in all_results:
        for j, kch in enumerate(keyfrag):
            counters[(pos + j) % key_len][kch] += 1
    key = ''.join(c.most_common(1)[0][0] if c else 'a' for c in counters)
    score = sum(quick_decrypt_with_key(ciphertext[:2000], key).count(w) for w in words)
    candidate_keys.append((score, key_len, key))

# --- Display top candidates ---
for score, klen, key in sorted(candidate_keys, reverse=True)[:10]:
    sample = quick_decrypt_with_key(ciphertext, key)[:400]
    print(f"\nscore={score}  len={klen}  key='{key}'\nsample: {sample}\n")
