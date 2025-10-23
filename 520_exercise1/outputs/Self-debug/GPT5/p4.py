def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower case
    or all keys are strings in upper case, else return False.
    The function should return False if the given dictionary is empty.
    """
    # Empty dictionary -> False
    if not dict:
        return False

    keys = list(dict.keys())

    # All keys must be strings
    if not all(isinstance(k, str) for k in keys):
        return False

    # Either all lowercase or all uppercase (per Python's str.islower/isupper semantics)
    all_lower = all(k.islower() for k in keys)
    if all_lower:
        return True

    all_upper = all(k.isupper() for k in keys)
    return all_upper
