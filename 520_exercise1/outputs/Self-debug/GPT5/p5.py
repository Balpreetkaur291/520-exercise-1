def Strongest_Extension(class_name, extensions):
    """
    Return "ClassName.StrongestExtensionName" where strength = (#uppercase) - (#lowercase).
    Ties are broken by first occurrence in the list.
    Non-letter characters do not contribute to strength.
    """
    if not extensions:
        # Assumption: if there are no extensions, return just the class name (no trailing dot).
        return class_name

    def strength(ext: str) -> int:
        caps = sum(1 for ch in ext if ch.isalpha() and ch.isupper())
        lows = sum(1 for ch in ext if ch.isalpha() and ch.islower())
        return caps - lows

    best_ext = None
    best_val = None

    for ext in extensions:
        val = strength(ext)
        if best_val is None or val > best_val:
            best_val = val
            best_ext = ext
        # Tie: keep the first one encountered (do nothing)

    return f"{class_name}.{best_ext}"
