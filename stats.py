

def get_num_words(book_text):
    word_count = len(book_text.split())
    #return f"{word_count} words found in the document"
    return word_count

def get_num_chars(book_text):
    book_text = book_text.lower()
    char_count = {}
    for char in book_text:
        try :
            char_count[char] += 1
        except KeyError:
            char_count[char] = 1
    return char_count

def get_sorted_list(char_dict):
    list_dict = []
    for key in char_dict:
        if not key.isalpha():
            continue
        list_dict.append({"char": key, "num": char_dict[key]})
    list_dict.sort(reverse=True, key=sort_on)
    #formatted_list = []
    #for element in list_dict:
    #    formatted_list.append({element["char"], element["num"]})
    #return formatted_list
    return list_dict


def sort_on(dict):
    return dict["num"]