import sys
from stats import get_num_words, sort_on, get_num_chars, sort_chars

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path) 
    num_words = get_num_words(text)
    chars_dict = get_num_chars(text)
    chars_sort = sort_chars(chars_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")  
    for c in chars_sort:
        if c["char"].isalpha():
            print(f'{c["char"]}: {c["num"]}')
    print("============= END ===============")



# get book text from file
def get_book_text(book_name):
    with open(book_name) as file:
        return file.read()


if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
else:
    main()