"""
Function to reverse the order of words in a sentence.
This solution handles multiple spaces between words and leading/trailing spaces correctly
by using the default split() behavior.
"""

def reverse_words(sentence: str) -> str:
    """
    Reverses the order of words in an input sentence.

    Args:
        sentence: The input string containing words separated by spaces.

    Returns:
        A new string with the order of words reversed, using a single space
        as a separator between the reversed words.
    """
    # Use split() without arguments:
    # 1. It splits the string by *any* sequence of whitespace (spaces, tabs, newlines).
    # 2. It automatically handles and discards empty strings, which resolves issues 
    #    related to multiple spaces between words or leading/trailing spaces.
    words = sentence.split()

    # 2. Reverse the list of words in place.
    words.reverse()

    # 3. Join the list back into a string, separated by a single space.
    return ' '.join(words)

# --- Examples and Test Cases ---
if __name__ == '__main__':
    # Standard Case
    sentence_1 = "the quick brown fox"
    print(f"Original: '{sentence_1}'")
    print(f"Reversed: '{reverse_words(sentence_1)}'\n")

    # Case with multiple internal/external spaces (robustness test)
    sentence_2 = "   Python  is  fun!   "
    print(f"Original: '{sentence_2}'")
    print(f"Reversed: '{reverse_words(sentence_2)}'\n")

    # Empty string
    sentence_3 = ""
    print(f"Original: '{sentence_3}'")
    print(f"Reversed: '{reverse_words(sentence_3)}'\n")

    # String with only spaces
    sentence_4 = "   "
    print(f"Original: '{sentence_4}'")
    print(f"Reversed: '{reverse_words(sentence_4)}'\n")

    # Single word
    sentence_5 = "Programming"
    print(f"Original: '{sentence_5}'")
    print(f"Reversed: '{reverse_words(sentence_5)}'")
