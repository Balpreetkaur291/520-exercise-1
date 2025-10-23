def check_dict_case(dict):
    """
    Return True if all keys are strings and are either all lowercase or all uppercase.
    Return False otherwise (including when the dictionary is empty).
    """
    d = dict  # avoid shadowing built-in name in the body

    if not isinstance(d, dict) or not d:
        return False

    keys = d.keys()

    # All keys must be strings
    if not all(isinstance(k, str) for k in keys):
        return False

    # Either all lowercase or all uppercase
    return all(k.islower() for k in keys) or all(k.isupper() for k in keys)
