from luke01.luke01 import get_character_count_of_word, CharCount, WordList
from itertools import filterfalse


def is_an_outright_palindrome(word: str) -> bool:
    return word[::-1] == word


def is_or_could_be_a_palindrome(word: str) -> bool:
    char_count: CharCount = get_character_count_of_word(word)
    odd_character_counts: int = len(list(filter(lambda x: char_count[x] % 2, char_count)))
    return odd_character_counts <= 1


if __name__ == "__main__":
    with open("./anagramlist.txt", "r") as f:
        word_list: WordList = [l.strip() for l in f.readlines()]

    not_already_palindromes: WordList = list(filterfalse(is_an_outright_palindrome, word_list))
    could_be_palindromes: WordList = list(filter(is_or_could_be_a_palindrome, not_already_palindromes))
    print(len(could_be_palindromes))
