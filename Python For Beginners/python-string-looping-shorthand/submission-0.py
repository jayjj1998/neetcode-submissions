def print_string_characters(word1: str, word2: str) -> None:
    print_chars_of_word(word1)
    print_chars_of_word(word2)

def print_chars_of_word(word: str) -> None:
    for char in word:
        print(char)




# do not modify below this line
print_string_characters("Hello, World!", "Good Job!")
