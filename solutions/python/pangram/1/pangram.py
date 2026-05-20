def is_pangram(sentence):
    return len({char for char in sentence.lower() if char.isalpha()}) == 26
