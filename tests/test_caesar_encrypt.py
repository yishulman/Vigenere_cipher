import pytest
import sys
import os

# Add the src directory to the Python path to import caesar_encrypt
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from caesar_encrypt import caesar_encrypt, frequency_analysis
from alphabets import english_alphabet, hebrew_alphabet


class TestFrequencyAnalysis:
    """Test suite for the frequency_analysis function."""
    
    def test_basic_frequency_analysis_english(self):
        """Test basic frequency analysis with English text."""
        result = frequency_analysis("english", "hello")
        expected = {char: 0 for char in english_alphabet}
        expected.update({'h': 1, 'e': 1, 'l': 2, 'o': 1})
        assert result == expected
    
    def test_empty_string_frequency(self):
        """Test frequency analysis with empty string."""
        result = frequency_analysis("english", "")
        expected = {char: 0 for char in english_alphabet}
        assert result == expected
    
    def test_single_character_frequency(self):
        """Test frequency analysis with single character."""
        result = frequency_analysis("english", "a")
        expected = {char: 0 for char in english_alphabet}
        expected['a'] = 1
        assert result == expected
    
    def test_uppercase_frequency(self):
        """Test that uppercase letters are counted correctly."""
        result = frequency_analysis("english", "HELLO")
        expected = {char: 0 for char in english_alphabet}
        expected.update({'h': 1, 'e': 1, 'l': 2, 'o': 1})
        assert result == expected
    
    def test_mixed_case_frequency(self):
        """Test frequency analysis with mixed case."""
        result = frequency_analysis("english", "HeLLo")
        expected = {char: 0 for char in english_alphabet}
        expected.update({'h': 1, 'e': 1, 'l': 2, 'o': 1})
        assert result == expected
    
    def test_non_alphabetic_ignored(self):
        """Test that non-alphabetic characters are ignored."""
        result = frequency_analysis("english", "hello, world! 123")
        expected = {char: 0 for char in english_alphabet}
        expected.update({'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1})
        assert result == expected
    
    def test_all_alphabet_frequency(self):
        """Test frequency analysis with all alphabet letters."""
        text = "abcdefghijklmnopqrstuvwxyz"
        result = frequency_analysis("english", text)
        expected = {char: 1 for char in english_alphabet}
        assert result == expected
    
    def test_repeated_characters_frequency(self):
        """Test frequency analysis with repeated characters."""
        result = frequency_analysis("english", "aaabbbccc")
        expected = {char: 0 for char in english_alphabet}
        expected.update({'a': 3, 'b': 3, 'c': 3})
        assert result == expected
    
    def test_hebrew_frequency_analysis(self):
        """Test basic frequency analysis with Hebrew text."""
        result = frequency_analysis("hebrew", "אבא")
        expected = {char: 0 for char in hebrew_alphabet}
        expected.update({'א': 2, 'ב': 1})
        assert result == expected
    
    def test_hebrew_all_alphabet_frequency(self):
        """Test Hebrew frequency analysis with all alphabet letters."""
        text = "".join(hebrew_alphabet)
        result = frequency_analysis("hebrew", text)
        expected = {char: 1 for char in hebrew_alphabet}
        assert result == expected
    
    def test_unsupported_language_frequency(self):
        """Test that unsupported languages return empty dict."""
        result = frequency_analysis("spanish", "hola")
        assert result == {}
        
        result = frequency_analysis("french", "bonjour")
        assert result == {}
        
        result = frequency_analysis("", "test")
        assert result == {}
    
    def test_spaces_and_punctuation_frequency(self):
        """Test that spaces and punctuation don't affect frequency."""
        result = frequency_analysis("english", "a b c, d; e: f!")
        expected = {char: 0 for char in english_alphabet}
        expected.update({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1})
        assert result == expected
    
    def test_frequency_with_numbers(self):
        """Test frequency analysis ignores numbers."""
        result = frequency_analysis("english", "a1b2c3")
        expected = {char: 0 for char in english_alphabet}
        expected.update({'a': 1, 'b': 1, 'c': 1})
        assert result == expected

    def test_en_bible_frequency(self):
        """Test frequency analysis on a sample of the English Bible text."""
        with open('./tests/bible_en.txt', 'r', encoding='utf-8') as file:
            original_text = file.read()
        result = frequency_analysis("english", original_text)
        expected = {char: 0 for char in english_alphabet}
        expected.update({'a': 56376, 'b': 11613, 'c': 11631, 'd': 33657, 'e': 88229, 'f': 18346, 'g': 11853, 'h': 55492, 'i': 38090, 'j': 1017, 'k': 4007, 'l': 28382, 'm': 17029, 'n': 49495, 'o': 51692, 'p': 8191, 'q': 103, 'r': 36152, 's': 42694, 't': 63933, 'u': 20440, 'v': 6279, 'w': 10940, 'x': 1500, 'y': 12251, 'z': 362})
        assert result == expected
    
    def test_he_bible_frequency(self):
        """Test frequency analysis on a sample of the Hebrew Bible text."""
        with open('./tests/bible_he.txt', 'r', encoding='utf-8') as file:
            original_text = file.read()
        result = frequency_analysis("hebrew", original_text)
        expected = {char: 0 for char in hebrew_alphabet}
        expected.update({'א': 96065, 'ב': 65534, 'ג': 10137, 'ד': 32552, 'ה': 102515, 'ו': 130538, 'ז': 9138, 'ח': 27748, 'ט': 6353, 'י': 139128, 'כ': 34881, 'ל': 88805, 'מ': 57912, 'ם': 41603, 'נ': 40110, 'ן': 15301, 'ס': 9673, 'ע': 45043, 'פ': 17761, 'ף': 2564, 'צ': 11776, 'ץ': 3290, 'ק': 18405, 'ר': 69157, 'ש': 58224, 'ת': 63744})
        assert result == expected
        
class TestFrequencyAnalysisParametrized:
    """Parametrized tests for frequency_analysis function."""
    
    @pytest.mark.parametrize("text,expected_char,expected_count", [
        ("a", "a", 1),
        ("aa", "a", 2),
        ("aaa", "a", 3),
        ("abc", "a", 1),
        ("ABC", "a", 1),  # Should be lowercased
        ("", "a", 0),  # Empty string
    ])
    def test_parametrized_frequency_counts(self, text, expected_char, expected_count):
        """Test various frequency count scenarios."""
        result = frequency_analysis("english", text)
        assert result[expected_char] == expected_count
    
    @pytest.mark.parametrize("lang,text", [
        ("english", "hello world"),
        ("hebrew", "שלום עולם"),
        ("english", "THE QUICK BROWN FOX"),
        ("hebrew", "אבגדהוזחטיכלמנסעפצקרשת"),
    ])
    def test_total_character_count(self, lang, text):
        """Test that total character count matches alphabetic characters in text."""
        result = frequency_analysis(lang, text)
        total_count = sum(result.values())
        
        # Count alphabetic characters manually
        alphabet = english_alphabet if lang == "english" else hebrew_alphabet
        expected_count = sum(1 for char in text.lower() if char in alphabet)
        
        assert total_count == expected_count

class TestIntegrationCaesarAndFrequency:
    """Integration tests combining caesar_encrypt and frequency_analysis."""
    
    def test_frequency_preservation_zero_shift(self):
        """Test that frequency is preserved with zero shift."""
        original_text = "hello world"
        encrypted_text = caesar_encrypt("english", original_text, 0)
        
        original_freq = frequency_analysis("english", original_text)
        encrypted_freq = frequency_analysis("english", encrypted_text)
        
        assert original_freq == encrypted_freq
    
    def test_frequency_shift_consistency(self):
        """Test that frequency analysis reflects character shifts correctly."""
        original_text = "abc"
        encrypted_text = caesar_encrypt("english", original_text, 1)  # Should be "bcd"
        
        original_freq = frequency_analysis("english", original_text)
        encrypted_freq = frequency_analysis("english", encrypted_text)
        
        # Original has a:1, b:1, c:1
        # Encrypted should have b:1, c:1, d:1
        assert original_freq['a'] == 1 and encrypted_freq['a'] == 0
        assert original_freq['b'] == 1 and encrypted_freq['b'] == 1
        assert original_freq['c'] == 1 and encrypted_freq['c'] == 1
        assert original_freq['d'] == 0 and encrypted_freq['d'] == 1
    
    def test_total_character_count_preservation(self):
        """Test that total character count is preserved after encryption."""
        original_text = "hello world"
        encrypted_text = caesar_encrypt("english", original_text, 5)
        
        original_freq = frequency_analysis("english", original_text)
        encrypted_freq = frequency_analysis("english", encrypted_text)
        
        original_total = sum(original_freq.values())
        encrypted_total = sum(encrypted_freq.values())
        
        assert original_total == encrypted_total
    
    def test_hebrew_integration(self):
        """Test integration with Hebrew text."""
        original_text = "אבג"
        encrypted_text = caesar_encrypt("hebrew", original_text, 1)  # Should be "בגד"
        
        original_freq = frequency_analysis("hebrew", original_text)
        encrypted_freq = frequency_analysis("hebrew", encrypted_text)
        
        # Verify total count is preserved
        assert sum(original_freq.values()) == sum(encrypted_freq.values())
        
        # Verify specific character shifts
        assert original_freq['א'] == 1 and encrypted_freq['א'] == 0
        assert original_freq['ב'] == 1 and encrypted_freq['ב'] == 1
        assert original_freq['ג'] == 1 and encrypted_freq['ג'] == 1
        assert original_freq['ד'] == 0 and encrypted_freq['ד'] == 1

class TestCaesarEncrypt:
    """Test suite for the caesar_encrypt function."""
    
    def test_basic_lowercase_encryption(self):
        """Test basic encryption with lowercase letters."""
        assert caesar_encrypt("english", "hello", 3) == "khoor"
        assert caesar_encrypt("english", "world", 3) == "zruog"
        assert caesar_encrypt("english", "abc", 1) == "bcd"
    
    def test_basic_uppercase_encryption(self):
        """Test basic encryption with uppercase letters."""
        assert caesar_encrypt("english", "HELLO", 3) == "KHOOR"
        assert caesar_encrypt("english", "WORLD", 3) == "ZRUOG"
        assert caesar_encrypt("english", "ABC", 1) == "BCD"
    
    def test_mixed_case_encryption(self):
        """Test encryption with mixed case letters."""
        assert caesar_encrypt("english", "Hello World", 3) == "Khoor Zruog"
        assert caesar_encrypt("english", "PyThOn", 5) == "UdYmTs"
        assert caesar_encrypt("english", "TeSt", 1) == "UfTu"
    
    def test_wrap_around_lowercase(self):
        """Test that lowercase letters wrap around correctly."""
        assert caesar_encrypt("english", "xyz", 3) == "abc"
        assert caesar_encrypt("english", "z", 1) == "a"
        assert caesar_encrypt("english", "y", 2) == "a"
    
    def test_wrap_around_uppercase(self):
        """Test that uppercase letters wrap around correctly."""
        assert caesar_encrypt("english", "XYZ", 3) == "ABC"
        assert caesar_encrypt("english", "Z", 1) == "A"
        assert caesar_encrypt("english", "Y", 2) == "A"
    
    def test_non_alphabetic_characters(self):
        """Test that non-alphabetic characters remain unchanged."""
        assert caesar_encrypt("english", "hello, world!", 3) == "khoor, zruog!"
        assert caesar_encrypt("english", "123", 5) == "123"
        assert caesar_encrypt("english", "!@#$%", 10) == "!@#$%"
        assert caesar_encrypt("english", "", 3) == ""
    
    def test_spaces_and_punctuation(self):
        """Test that spaces and punctuation are preserved."""
        assert caesar_encrypt("english", "hello world", 3) == "khoor zruog"
        assert caesar_encrypt("english", "a.b,c;d:e", 1) == "b.c,d;e:f"
        assert caesar_encrypt("english", "test-case_example", 2) == "vguv-ecug_gzcorng"
    
    def test_zero_shift(self):
        """Test that zero shift returns the original text."""
        assert caesar_encrypt("english", "hello", 0) == "hello"
        assert caesar_encrypt("english", "HELLO", 0) == "HELLO"
        assert caesar_encrypt("english", "Hello World!", 0) == "Hello World!"
    
    def test_large_positive_shift(self):
        """Test that large shifts work correctly (should wrap around)."""
        assert caesar_encrypt("english", "abc", 26) == "abc"  # 26 shifts = full alphabet
        assert caesar_encrypt("english", "abc", 27) == "bcd"  # 27 shifts = 1 shift
        assert caesar_encrypt("english", "xyz", 29) == "abc"  # 29 shifts = 3 shifts
    
    def test_negative_shift(self):
        """Test that negative shifts work correctly."""
        assert caesar_encrypt("english", "def", -3) == "abc"
        assert caesar_encrypt("english", "abc", -1) == "zab"
        assert caesar_encrypt("english", "ABC", -1) == "ZAB"
    
    def test_large_negative_shift(self):
        """Test that large negative shifts work correctly."""
        assert caesar_encrypt("english", "abc", -26) == "abc"  # -26 shifts = full alphabet
        assert caesar_encrypt("english", "abc", -27) == "zab"  # -27 shifts = -1 shift
        assert caesar_encrypt("english", "def", -29) == "abc"  # -29 shifts = -3 shifts
    
    def test_empty_string(self):
        """Test that empty string returns empty string."""
        assert caesar_encrypt("english", "", 1) == ""
        assert caesar_encrypt("english", "", 0) == ""
        assert caesar_encrypt("english", "", -5) == ""
    
    def test_single_character(self):
        """Test encryption of single characters."""
        assert caesar_encrypt("english", "a", 1) == "b"
        assert caesar_encrypt("english", "A", 1) == "B"
        assert caesar_encrypt("english", "z", 1) == "a"
        assert caesar_encrypt("english", "Z", 1) == "A"
        assert caesar_encrypt("english", "1", 5) == "1"
    
    def test_numbers_and_symbols(self):
        """Test that numbers and symbols are preserved."""
        assert caesar_encrypt("english", "test123!@#", 5) == "yjxy123!@#"
        assert caesar_encrypt("english", "a1b2c3", 2) == "c1d2e3"
        assert caesar_encrypt("english", "x+y=z", 1) == "y+z=a"
    
    def test_all_alphabet_lowercase(self):
        """Test encryption of the entire lowercase alphabet."""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        expected = "defghijklmnopqrstuvwxyzabc"
        assert caesar_encrypt("english", alphabet, 3) == expected
    
    def test_all_alphabet_uppercase(self):
        """Test encryption of the entire uppercase alphabet."""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        expected = "DEFGHIJKLMNOPQRSTUVWXYZABC"
        assert caesar_encrypt("english", alphabet, 3) == expected
    
    def test_known_example_from_main(self):
        """Test the specific example from the main function."""
        assert caesar_encrypt("english", "hello world", 3) == "khoor zruog"
    
    def test_unsupported_language(self):
        """Test that unsupported languages return original text."""
        assert caesar_encrypt("spanish", "hola", 3) == "hola"
        assert caesar_encrypt("french", "bonjour", 5) == "bonjour"
        assert caesar_encrypt("", "test", 1) == "test"
    
    def test_hebrew_basic_encryption(self):
        """Test basic Hebrew encryption."""
        # Test first few Hebrew letters with shift of 1
        assert caesar_encrypt("hebrew", "א", 1) == "ב"
        assert caesar_encrypt("hebrew", "ב", 1) == "ג"
        assert caesar_encrypt("hebrew", "ג", 1) == "ד"
    
    def test_hebrew_wrap_around(self):
        """Test Hebrew alphabet wrap around."""
        # Test wrap around from last letter to first
        assert caesar_encrypt("hebrew", "ת", 1) == "א"
        assert caesar_encrypt("hebrew", "ש", 2) == "א"
    
    def test_mixed_hebrew_non_hebrew(self):
        """Test Hebrew text with non-Hebrew characters."""
        assert caesar_encrypt("hebrew", "א1ב2ג", 1) == "ב1ג2ד"
        assert caesar_encrypt("hebrew", "שלום!", 1) == "תמזנ!"


# Parametrized tests for additional coverage
class TestCaesarEncryptParametrized:
    """Parametrized tests for caesar_encrypt function."""
    
    @pytest.mark.parametrize("text,shift,expected", [
        ("a", 1, "b"),
        ("z", 1, "a"),
        ("A", 1, "B"),
        ("Z", 1, "A"),
        ("hello", 0, "hello"),
        ("test", 13, "grfg"),  # ROT13
        ("grfg", 13, "test"),  # ROT13 reverse
    ])
    def test_parametrized_cases(self, text, shift, expected):
        """Test various text and shift combinations."""
        assert caesar_encrypt("english", text, shift) == expected
    
    @pytest.mark.parametrize("shift", [26, 52, 78, 104])
    def test_multiple_alphabet_shifts(self, shift):
        """Test that multiples of 26 return original text."""
        text = "Hello World"
        assert caesar_encrypt("english", text, shift) == text
    
    @pytest.mark.parametrize("char", "!@#$%^&*()_+-=[]{}|;:'\",.<>?/`~")
    def test_special_characters_unchanged(self, char):
        """Test that special characters remain unchanged."""
        assert caesar_encrypt("english", char, 10) == char
    
    @pytest.mark.parametrize("lang,text,shift,expected", [
        ("english", "abc", 1, "bcd"),
        ("english", "xyz", 1, "yza"),
        ("hebrew", "אבג", 1, "בגד"),
        ("unsupported", "test", 5, "test"),  # Unsupported language returns original
    ])
    def test_language_parametrized_cases(self, lang, text, shift, expected):
        """Test various language, text and shift combinations."""
        assert caesar_encrypt(lang, text, shift) == expected


if __name__ == "__main__":
    pytest.main([__file__])
