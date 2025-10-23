import string

def Strongest_Extension(class_name, extensions):
    """
    Finds the strongest extension based on the strength formula (CAP - SM) 
    and returns a formatted string ClassName.StrongestExtensionName. 
    Ties are broken by choosing the extension that appears first in the list.
    """
    if not extensions:
        # Handle the case where the list of extensions is empty.
        # Although the problem implies there will be extensions, this is safe.
        return f"{class_name}.NoExtensionFound"

    # Helper function to calculate the strength of a single extension name
    def calculate_strength(extension_name):
        """Calculates CAP - SM for a given extension name."""
        cap_count = 0  # Number of uppercase letters
        sm_count = 0   # Number of lowercase letters
        
        for char in extension_name:
            if 'A' <= char <= 'Z':  # Check for uppercase
                cap_count += 1
            elif 'a' <= char <= 'z': # Check for lowercase
                sm_count += 1
                
        return cap_count - sm_count

    # 1. Initialize with the first extension
    strongest_extension_name = extensions[0]
    max_strength = calculate_strength(extensions[0])
    
    # 2. Iterate through the remaining extensions
    for i in range(1, len(extensions)):
        current_extension_name = extensions[i]
        current_strength = calculate_strength(current_extension_name)
        
        # 3. Check for a strictly stronger extension
        # The tie-breaker rule ("choose the one that comes first in the list") 
        # means we ONLY update if the current_strength is *strictly greater* # than max_strength.
        if current_strength > max_strength:
            max_strength = current_strength
            strongest_extension_name = current_extension_name
            
    # 4. Return the result in the specified format
    return f"{class_name}.{strongest_extension_name}"