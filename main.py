import sys
from stats import get_num_words, get_book_text
from stats import count_chars, sort_dict

def main():
    

    if len(sys.argv) != 2:
    # We don't have exactly 2 items in the list
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]

    dict_frank = count_chars(get_book_text(path_to_book))
    sorted = sort_dict(dict_frank, len(dict_frank))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print("----------- Word Count ----------")
    get_num_words(path_to_book)
    print("--------- Character Count -------")
    for s in sorted:
        if s["char"].isalpha():
            print(f"{s["char"]}: {s["num"]}")


    print("============= END ===============")
main()