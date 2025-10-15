def get_book_text(path):
    with open(path) as file:
        return file.read()

def count_words(text):
    return len(text.split())

def count_characters(text):
    characters = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in characters:
            characters[lowered_char] += 1 
        else:
            characters[lowered_char] = 1
    return characters

def sort_on(char):
    return char["value"]

def sort_dict(characters):
    list_of_dict = []
    for key in characters:
        list_of_dict.append({
            "char": key,
            "value": characters[key]
        })
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict