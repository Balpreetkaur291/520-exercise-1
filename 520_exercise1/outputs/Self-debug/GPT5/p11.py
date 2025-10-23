def reverse_words(sentence: str) -> str:
    """
    Return a new string with words in reverse order.
    - Collapses any whitespace runs (including multiple spaces/tabs/newlines) to single spaces.
    - Strips leading/trailing whitespace.
    - Returns "" for empty or all-whitespace input.

    Examples:
        "hello world"        -> "world hello"
        "  a   b  c "        -> "c b a"
        "single"             -> "single"
        "" / "   \t  \n"     -> ""
    """
    # .split() with no argument splits on any whitespace and drops empties
    words = sentence.split()
    return ' '.join(reversed(words))
