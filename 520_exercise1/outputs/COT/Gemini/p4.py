def check_dict_case(d):
    """
    Given a dictionary, return True if all keys are strings in lower case 
    or all keys are strings in upper case, else return False. 
    The function should return False is the given dictionary is empty.
    """
    # 1. Handle the empty dictionary case
    if not d:
        return False

    # 2. Filter out non-string keys
    string_keys = [k for k in d.keys() if isinstance(k, str)]
    
    # If there are no string keys, the condition of uniform casing is vacuously True, 
    # as no string keys exist to violate it.
    if not string_keys:
        return True

    # 3. Check if all string keys are lowercase
    # all(k == k.lower() checks if the key is composed entirely of lowercase 
    # characters or non-alphabetic characters (which are case-insensitive).
    all_lower = all(k == k.lower() for k in string_keys)

    # 4. Check if all string keys are uppercase
    # all(k == k.upper() checks if the key is composed entirely of uppercase
    # characters or non-alphabetic characters.
    all_upper = all(k == k.upper() for k in string_keys)
    
    # 5. Return True if either condition is met, False otherwise (including mixed case)
    return all_lower or all_upper