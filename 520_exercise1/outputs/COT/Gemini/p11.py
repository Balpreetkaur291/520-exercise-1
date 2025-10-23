def reverse_words(sentence: str) -> str:
    """
    Reverses the order of words in a sentence string.

    Words are assumed to be separated by one or more spaces.

    Args:
        sentence: The input string containing words separated by spaces.

    Returns:
        A new string with the words in the reverse order.
    """
    # 1. Split the sentence into a list of words.
    # By calling split() without arguments, it handles multiple spaces 
    # between words and leading/trailing spaces correctly.
    words = sentence.split()

    # 2. Reverse the order of the list of words using slicing [::-1].
    reversed_words = words[::-1]

    # 3. Join the reversed words back together into a single string,
    # using a single space ' ' as the separator.
    result = " ".join(reversed_words)

    return result

# --- Example Usage ---

print("--- Testing reverse_words function ---")

# Example 1: Standard sentence
sentence1 = "the quick brown fox"
reversed1 = reverse_words(sentence1)
print(f"Original: '{sentence1}'")
print(f"Reversed: '{reversed1}'")
# Expected Output: 'fox brown quick the'

print("-" * 20)

# Example 2: Sentence with multiple spaces and leading/trailing spaces
sentence2 = "  hello   world! "
reversed2 = reverse_words(sentence2)
print(f"Original: '{sentence2}'")
print(f"Reversed: '{reversed2}'")
# Expected Output: 'world! hello'

print("-" * 20)

# Example 3: Empty string
sentence3 = ""
reversed3 = reverse_words(sentence3)
print(f"Original: '{sentence3}'")
print(f"Reversed: '{reversed3}'")
# Expected Output: ''

print("-" * 20)

# Example 4: Single word
sentence4 = "Python"
reversed4 = reverse_words(sentence4)
print(f"Original: '{sentence4}'")
print(f"Reversed: '{reversed4}'")
# Expected Output: 'Python'
