from stats import count_words, get_book_text, count_characters, sort_dict


def main():
    PATH = "books/frankenstein.txt"
    text = get_book_text(PATH)
    sorted_characters_values = sort_dict(count_characters(text))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {PATH}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    for char in sorted_characters_values:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["value"]}")

main()
