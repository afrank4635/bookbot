def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    num_chars = {}
    for char in text:
            char = char.lower()
            if char in num_chars:
                num_chars[char] += 1  # increase the count
            else:
                num_chars[char] = 1   # add character with a first count
    return num_chars