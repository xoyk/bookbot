def main(path_to_file):
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    print(num_words)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def get_num_words(text):
    return len(text.split())


main("books/frankenstein.txt")