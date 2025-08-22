
# get book text from file
def get_book_text(book_name):
    with open(book_name) as file:
        return file.read()

def count_words(text):
    words = text.split()
    return len(words)

def main():
    book_text = get_book_text("books/frankenstein.txt")  # Example book file
    count_words(book_text)
    num_words = count_words(book_text)
    print(f'{num_words} words found in the document')

main()
  