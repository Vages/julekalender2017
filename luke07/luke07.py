from typing import List, Dict

THE_ALPHABET: List[str] = list('abcdefghijklmnopqrstuvwxyz')
LETTER_INDEX: Dict[str, int] = dict([(l, i) for i, l in enumerate(THE_ALPHABET)])


def shift_letter_by_n_places(letter: str, n: int) -> str:
    if letter not in LETTER_INDEX:
        return letter
    original_index: int = LETTER_INDEX[letter]
    new_index: int = (original_index + n) % len(THE_ALPHABET)
    return THE_ALPHABET[new_index]


ENCIPHERING_TABLE: Dict[str, str] = dict(
    [(c, shift_letter_by_n_places(c, ord(c) + LETTER_INDEX[c] + 21)) for c in THE_ALPHABET])
DECIPHERING_TABLE: Dict[str, str] = dict([(ENCIPHERING_TABLE[k], k) for k in ENCIPHERING_TABLE])


def decipher_string(string: str) -> str:
    return ''.join([DECIPHERING_TABLE[l] if l in LETTER_INDEX else l for l in string.lower()])


if __name__ == '__main__':
    print(decipher_string('OTUJNMQTYOQOVVNEOXQVAOXJEYA'))
