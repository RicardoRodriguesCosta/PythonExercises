
def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    if len(text) > len(text[0:text.find(" ")]) +1:
        return text[0:text.find(" ")]
    else:
        return text


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print(first_word("hi"))
    print("Coding complete? Click 'Check' to earn cool rewards!")
    text = "hi"
    print(len(text))
    print(len(text[0:text.find(" ")]))
