from math import ceil, log2
from typing import Dict

from luke01.luke01 import get_character_count_of_word, CharCount
from luke02.luke02 import int_to_binary


def binary_enumerate(some_string: str) -> Dict[str, str]:
    bits_needed_for_longest_number: int = ceil(log2(len(some_string)))

    return dict([(character, int_to_binary(i).zfill(bits_needed_for_longest_number)) for (i, character) in
                 enumerate(some_string)])


def binary_to_int(binary_string: str) -> int:
    return int(binary_string, 2)


def binary_string_to_character(binary_string: str) -> str:
    return chr(binary_to_int(binary_string))


def decode_binary_string_to_unicode(binary_string: str) -> str:
    bits_in_a_unicode_character: int = 8
    return ''.join([binary_string_to_character(binary_string[start:start + bits_in_a_unicode_character]) for start in
                    range(0, len(binary_string), bits_in_a_unicode_character)])


def xor(a: str, b: str) -> str:
    y = int(a, 2) ^ int(b, 2)
    return bin(y)[2:].zfill(len(a))


if __name__ == '__main__':
    encrypted_message: str = "111001010100000101100000001110111010010101001101101010110110000001000111110100000101001" \
                             "0001011101001100100100011010000110101111101010011100010110001100111110010"

    national_hymn: [str] = ''.join([line.strip() for line in open('./ogudvorslands.txt', encoding='utf8')])
    character_count_of_national_hymn: CharCount = get_character_count_of_word(national_hymn)
    icelandic_alphabet: str = 'AÁBDÐEÉFGHIÍJKLMNOÓPRSTUÚVXYÝÞÆÖ'
    enumerated_alphabet: Dict[str, str] = binary_enumerate(icelandic_alphabet)

    decryption_key = ''.join(
        [enumerated_alphabet[character] for (character, _) in character_count_of_national_hymn.most_common()])

    decoded_binary_message: str = xor(decryption_key, encrypted_message)
    print(decode_binary_string_to_unicode(decoded_binary_message))
