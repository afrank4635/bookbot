from stats import get_num_words, get_num_chars

def main():
    book_text = get_book_text("books/frankenstein.txt")  # Example book file
    get_num_words(book_text)
    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)
    print(f'{num_words} words found in the document')  
    print(f'{num_chars} words found in the document') 



# get book text from file
def get_book_text(book_name):
    with open(book_name) as file:
        return file.read()



main()