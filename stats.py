def get_book_text(file_path):
    file_contents = ""
    with open (file_path) as f:
        file_contents = f.read()
        return file_contents
    
def get_num_words(path):


    file_contents = []
    file_contents = get_book_text(path).split()

    num_words = len(file_contents)
    print(f"Found {num_words} total words")

def count_chars(text_from_book):

    dict_frank = {}
    char = ""
    book_text = text_from_book
    for i in range(0, len(book_text)):
        char = book_text[i].lower()
        if char in dict_frank:
            dict_frank[char] += 1
        else:
            dict_frank[char] = 1
    
    return dict_frank

def sort_dict(dictionary, count):
    sorted_list = []

    for char, count in dictionary.items():
        sorted_list.append({"char": char, "num": count})

    sorted_list.sort(reverse = True, key=lambda x: x["num"])

    return sorted_list