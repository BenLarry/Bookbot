PATH="books/frankestein.txt"

def main():
    with open(PATH) as f:
        txt = f.read()

    print_report(PATH, count_words(txt), sort_dict(count_characters(txt)))

def count_words(text):
    return len(text.split())

def count_characters(text):
    char_dict = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in char_dict:
            char_dict[lowered_char] += 1
        else:
            char_dict[lowered_char] = 1
    return char_dict

def sort_dict(dict):
    sorted_dict = {key: value for key, value in sorted(dict.items(), reverse=True, key=lambda x: x[1])}
    return sorted_dict

def print_report(PATH, word_count, char_dict):
    print(f"Begin report of {PATH}")
    print(f"{word_count} words was found in document")

    for char in char_dict:
        if char.isalpha():
            print(f"The {char} character was found {char_dict[char]} times")
    print("-- End Report --")

main()