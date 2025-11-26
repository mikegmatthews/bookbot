from stats import get_num_words
from stats import count_characters
from stats import get_sorted_counts

import sys

def get_book_text(filepath):
    with open(filepath) as f:
        fileContents = f.read()
        return fileContents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")

    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}...")
    
    print("----------- Word Count ----------")
    
    bookText = get_book_text(book_path)
    numWords = get_num_words(bookText)
    print(f"Found {numWords} total words")

    print("--------- Character Count -------")

    counts = count_characters(bookText)
    sorted_counts = get_sorted_counts(counts)

    for i in range(0, len(sorted_counts)):
        if sorted_counts[i]["char"].isalpha():
            print(f"{sorted_counts[i]["char"]}: {sorted_counts[i]["num"]}")
    
    print("============= END ===============")
    
main()
