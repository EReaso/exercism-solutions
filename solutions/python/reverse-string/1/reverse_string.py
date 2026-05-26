def reverse(text: str) -> str:
    new_str = ""
    for char in text: new_str = char + new_str
    return new_str
