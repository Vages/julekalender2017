import typing
from collections import Counter

CharSet = typing.Set[str]
CharCount = typing.Counter
WordList = typing.List[str]


def get_character_set_of_word(word: str) -> CharSet:
    return set(word)


def get_character_count_of_word(word: str) -> CharCount:
    return Counter(word)


def character_sets_are_the_same(charset1: CharSet, charset2: CharSet) -> bool:
    return charset1 == charset2


def character_counts_are_the_same(char_count1: CharCount, char_count2: CharCount) -> bool:
    return char_count1 == char_count2


def find_words_that_have_same_charset_as_riddle(riddle: str, word_list: WordList) -> WordList:
    riddle_charset: CharSet = get_character_set_of_word(riddle)
    return list(filter(lambda x: character_sets_are_the_same(riddle_charset, get_character_set_of_word(x)), word_list))


def generate_n_gram_string(word: str, n: int = 1) -> str:
    n_gram_list: typing.List[str] = [word[i:i + n] for i in range(len(word) - (n - 1))]
    return ''.join(n_gram_list)


def get_all_n_gram_strings_for_a_word(word: str) -> typing.List[str]:
    return [generate_n_gram_string(word, i) for i in range(1, len(word))]


def word_has_matching_n_gram_string(riddle: str, word: str) -> typing.Tuple[bool, int]:
    n_grams: typing.List[str] = get_all_n_gram_strings_for_a_word(word)
    riddle_charcount: CharCount = get_character_count_of_word(riddle)
    for n, word in enumerate(n_grams, start=1):
        if character_counts_are_the_same(riddle_charcount, get_character_count_of_word(word)):
            return True, n

    return False, 0

if __name__ == '__main__':
    the_word_list: WordList = [w.strip() for w in open('wordlist.txt')]

    the_riddle: str = 'aeteesasrsssstaesersrrsse'

    the_suspects: WordList = find_words_that_have_same_charset_as_riddle(the_riddle, the_word_list)

    for a_word in the_suspects:
        has_match, m = word_has_matching_n_gram_string(the_riddle, a_word)
        if has_match:
            print(m, '-', a_word, sep='')
