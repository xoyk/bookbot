def main(path_to_file):
    
    report = generate_report(path_to_file)
    print(report)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def get_num_words(text):
    return len(text.split())

def get_num_letters(text):
    result = {}

    for letter in text:
        key = letter.lower()
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
        
    return result

def generate_report(path_to_file):
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    report = f"--- Begin report of {path_to_file} ---\n"
    report += f"{num_words} words found in the document\n\n"
    for letter in num_letters:
        report += f"The '{letter}' character was found {num_letters[letter]} times\n"

    report += "--- End report ---"
    return report

main("books/frankenstein.txt")