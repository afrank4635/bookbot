def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(items):
    return items["num"]

def get_num_chars(text):
    chars = {}
    for c in text:
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1  # increase the count
            else:
                chars[lowered] = 1   # add character with a first count
    return chars

def sort_chars(chars):
    chars_sort = []

    for key, value in chars.items():
        unsordict = {
            "char": key, 
            "num": value
        }
        chars_sort.append(unsordict)
    chars_sort.sort(reverse=True, key=sort_on)
    return chars_sort