def Strongest_Extension(class_name, extensions):
    """
    Return "ClassName.StrongestExtensionName" where strength = (#uppercase - #lowercase)
    If multiple have the same strength, pick the earliest in the list.
    """
    if not extensions:
        raise ValueError("extensions must be a non-empty list")

    def strength(ext):
        caps = sum(1 for ch in ext if ch.isalpha() and ch.isupper())
        lows = sum(1 for ch in ext if ch.isalpha() and ch.islower())
        return caps - lows

    # Track the best extension seen so far (keep the first on ties)
    best_ext = extensions[0]
    best_val = strength(best_ext)

    for ext in extensions[1:]:
        val = strength(ext)
        if val > best_val:
            best_val = val
            best_ext = ext

    return f"{class_name}.{best_ext}"
