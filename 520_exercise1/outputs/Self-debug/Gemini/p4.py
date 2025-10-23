def check_dict_case(input_dict):
    """
    Given a dictionary, return True if all keys that are strings are either 
    all in lower case or all in upper case. Returns False otherwise.
    The function returns False if the given dictionary is empty.

    Args:
        input_dict (dict): The dictionary to check.

    Returns:
        bool: True if key cases are consistent (all lower or all upper), False otherwise.
    """
    # 1. Handle the mandatory empty dictionary case first.
    if not input_dict:
        return False

    # 2. Extract only the string keys from the dictionary.
    string_keys = [key for key in input_dict.keys() if isinstance(key, str)]

    # 3. Edge Case: If the dictionary is not empty, but contains no string keys 
    # (e.g., {1: 'a', 2: 'b'}).
    # The condition "all keys are strings in lower case or all keys are strings in upper case" 
    # is vacuously true if there are no string keys to violate it.
    if not string_keys:
        return True

    # 4. Check if ALL string keys are lowercase.
    # The all() function short-circuits, improving efficiency.
    is_all_lower = all(key.islower() for key in string_keys)

    # 5. Check if ALL string keys are uppercase.
    is_all_upper = all(key.isupper() for key in string_keys)

    # 6. Return True if either condition is met (all lower OR all upper).
    # If the keys contain a mix of lower/upper, or a mix of cases (e.g., 'Mixed'), 
    # both is_all_lower and is_all_upper will be False.
    return is_all_lower or is_all_upper