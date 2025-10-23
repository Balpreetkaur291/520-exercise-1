def check(reverse_words):
    assert reverse_words("I love Python") == "Python love I"     
    assert reverse_words("Hello world") == "world Hello"          
    assert reverse_words("") == ""                               
    assert reverse_words("  hello  world  ") == "world hello"