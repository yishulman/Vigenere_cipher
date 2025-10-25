import pytest
import sys
import os

# Add the src directory to the Python path to import vigenere_cipher
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from vigenere_cipher import (
    vigenere_encrypt, 
    vigenere_decrypt
)


class TestVigenereEncrypt:
    """Test suite for the vigenere_encrypt function."""
    
    def test_basic_english_encryption(self):
        """Test basic Vigenère encryption with English text."""
        assert vigenere_encrypt("english", "hello", "key") == "rijvs"
        assert vigenere_encrypt("english", "world", "abc") == "wptle"
        assert vigenere_encrypt("english", "test", "xyz") == "qcrq"
    
    def test_basic_uppercase_encryption(self):
        """Test encryption with uppercase letters."""
        assert vigenere_encrypt("english", "HELLO", "KEY") == "RIJVS"
        assert vigenere_encrypt("english", "WORLD", "ABC") == "WPTLE"
    
    def test_mixed_case_encryption(self):
        """Test encryption with mixed case letters."""
        assert vigenere_encrypt("english", "Hello World", "Key") == "Rijvs Uyvjn"
    
    def test_keyword_repetition(self):
        """Test that keyword repeats correctly for longer text."""
        # "abc" repeated: a=0, b=1, c=2, a=0, b=1, c=2, ...
        assert vigenere_encrypt("english", "abcdef", "abc") == "acedfh"
        assert vigenere_encrypt("english", "aaaa", "ab") == "abab"
    
    def test_non_alphabetic_characters(self):
        """Test that non-alphabetic characters remain unchanged and don't advance keyword."""
        assert vigenere_encrypt("english", "a b c", "xyz") == "x z b"  # spaces don't advance keyword
        assert vigenere_encrypt("english", "a,b,c", "xyz") == "x,z,b"  # punctuation doesn't advance keyword
        assert vigenere_encrypt("english", "a1b2c", "xyz") == "x1z2b"  # numbers don't advance keyword
    
    def test_empty_inputs(self):
        """Test edge cases with empty inputs."""
        assert vigenere_encrypt("english", "", "key") == ""
        assert vigenere_encrypt("english", "hello", "") == "hello"
        assert vigenere_encrypt("english", "", "") == ""
    
    def test_unsupported_language(self):
        """Test that unsupported languages return original text."""
        assert vigenere_encrypt("spanish", "hola", "key") == "hola"
        assert vigenere_encrypt("french", "bonjour", "key") == "bonjour"
    
    def test_keyword_with_non_alphabetic_chars(self):
        """Test keyword cleaning - non-alphabetic characters should be ignored."""
        assert vigenere_encrypt("english", "abc", "k1e2y") == vigenere_encrypt("english", "abc", "key")
        assert vigenere_encrypt("english", "abc", "k!e@y#") == vigenere_encrypt("english", "abc", "key")
        assert vigenere_encrypt("english", "abc", "123") == "abc"  # No valid chars in keyword
    
    def test_hebrew_encryption(self):
        """Test basic Hebrew encryption."""
        # Simple test with Hebrew characters
        assert vigenere_encrypt("hebrew", "א", "א") == "א"  # א + א = א (0 + 0 = 0)
        assert vigenere_encrypt("hebrew", "א", "ב") == "ב"  # א + ב = ב (0 + 1 = 1)
    
    def test_wrap_around(self):
        """Test alphabet wrap-around."""
        # Test English wrap-around: z + b = a (25 + 1 = 0)
        assert vigenere_encrypt("english", "z", "b") == "a"
        # Test multiple wraps: x(23)+z(25)=w(22), y(24)+z(25)=x(23), z(25)+z(25)=y(24)
        assert vigenere_encrypt("english", "xyz", "zzz") == "wxy"


class TestVigenereDecrypt:
    """Test suite for the vigenere_decrypt function."""
    
    def test_basic_decryption(self):
        """Test that decryption reverses encryption."""
        original = "hello world"
        keyword = "key"
        encrypted = vigenere_encrypt("english", original, keyword)
        decrypted = vigenere_decrypt("english", encrypted, keyword)
        assert decrypted == original
    
    def test_case_preservation_in_decryption(self):
        """Test that case is preserved during decryption."""
        original = "Hello World"
        keyword = "Key"
        encrypted = vigenere_encrypt("english", original, keyword)
        decrypted = vigenere_decrypt("english", encrypted, keyword)
        assert decrypted == original
    
    def test_decrypt_known_values(self):
        """Test decryption of known encrypted values."""
        assert vigenere_decrypt("english", "rijvs", "key") == "hello"
        assert vigenere_decrypt("english", "wptle", "abc") == "world"
    
    def test_decrypt_empty_inputs(self):
        """Test decryption edge cases with empty inputs."""
        assert vigenere_decrypt("english", "", "key") == ""
        assert vigenere_decrypt("english", "hello", "") == "hello"
        assert vigenere_decrypt("english", "", "") == ""
    
    def test_decrypt_with_punctuation(self):
        """Test decryption preserves punctuation and spacing."""
        original = "hello, world!"
        keyword = "test"
        encrypted = vigenere_encrypt("english", original, keyword)
        decrypted = vigenere_decrypt("english", encrypted, keyword)
        assert decrypted == original


class TestEncryptDecryptRoundTrip:
    """Test that encryption followed by decryption returns original text."""
    
    @pytest.mark.parametrize("text,keyword", [
        ("hello", "key"),
        ("Hello World", "Test"),
        ("The quick brown fox", "secretkey"),
        ("a", "z"),
        ("", "key"),
        ("test", ""),
        ("Test with 123 numbers!", "keyword"),
        ("Mixed CASE text", "MixedKey"),
    ])
    def test_roundtrip_english(self, text, keyword):
        """Test encrypt-decrypt roundtrip for various English inputs."""
        encrypted = vigenere_encrypt("english", text, keyword)
        decrypted = vigenere_decrypt("english", encrypted, keyword)
        assert decrypted == text
    
    def test_roundtrip_hebrew(self):
        """Test encrypt-decrypt roundtrip for Hebrew text."""
        text = "אבג"
        keyword = "דה"
        encrypted = vigenere_encrypt("hebrew", text, keyword)
        decrypted = vigenere_decrypt("hebrew", encrypted, keyword)
        assert decrypted == text

class TestVigenereParametrized:
    """Parametrized tests for Vigenère cipher."""
    
    @pytest.mark.parametrize("lang,text,keyword,expected", [
        ("english", "a", "a", "a"),  # a + a = a (0 + 0 = 0)
        ("english", "a", "b", "b"),  # a + b = b (0 + 1 = 1)
        ("english", "b", "a", "b"),  # b + a = b (1 + 0 = 1)
        ("english", "ab", "aa", "ab"),  # No shift with 'a' key
        ("english", "z", "b", "a"),  # Wrap around test
        ("unsupported", "test", "key", "test"),  # Unsupported language
    ])
    def test_vigenere_encrypt_parametrized(self, lang, text, keyword, expected):
        """Test various encryption combinations."""
        assert vigenere_encrypt(lang, text, keyword) == expected
    
    @pytest.mark.parametrize("text", [
        "Hello World",
        "The Quick Brown Fox",
        "123 Test with numbers!",
        "MiXeD cAsE tExT",
        "",
        "a",
        "Single word",
    ])
    def test_roundtrip_various_texts(self, text):
        """Test encrypt-decrypt roundtrip for various texts."""
        keyword = "testkey"
        encrypted = vigenere_encrypt("english", text, keyword)
        decrypted = vigenere_decrypt("english", encrypted, keyword)
        assert decrypted == text


if __name__ == "__main__":
    pytest.main([__file__])