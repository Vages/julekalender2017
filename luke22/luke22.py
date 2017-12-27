from typing import List, Tuple

if __name__ == '__main__':
    the_string_we_are_searching: str = "FJKAUNOJDCUTCRHBYDLXKEODVBWTYPTSHASQQFCPRMLDXIJMYPVOHBDUGSMBLMVUMMZYHULSUIZIM" \
                                       "ZTICQORLNTOVKVAMQTKHVRIFMNTSLYGHEHFAHWWATLYAPEXTHEPKJUGDVWUDDPRQLUZMSZOJPSIKA" \
                                       "IHLTONYXAULECXXKWFQOIKELWOHRVRUCXIAASKHMWTMAJEWGEESLWRTQKVHRRCDYXNTLDSUPXMQTQ" \
                                       "DFAQAPYBGXPOLOCLFQNGNKPKOBHZWHRXAWAWJKMTJSLDLNHMUGVVOPSAMRUJEYUOBPFNEHPZZCLPN" \
                                       "ZKWMTCXERPZRFKSXVEZTYCXFRHRGEITWHRRYPWSVAYBUHCERJXDCYAVICPTNBGIODLYLMEYLISEYN" \
                                       "XNMCDPJJRCTLYNFMJZQNCLAGHUDVLYIGASGXSZYPZKLAWQUDVNTWGFFYFFSMQWUNUPZRJMTHACFEL" \
                                       "GHDZEJWFDWVPYOZEVEJKQWHQAHOCIYWGVLPSHFESCGEUCJGYLGDWPIWIDWZZXRUFXERABQJOXZALQ" \
                                       "OCSAYBRHXQQGUDADYSORTYZQPWGMBLNAQOFODSNXSZFURUNPMZGHTAJUJROIGMRKIZHSFUSKIZJJT" \
                                       "LGOEEPBMIXISDHOAIFNFEKKSLEXSJLSGLCYYFEQBKIZZTQQXBQZAPXAAIFQEIXELQEZGFEPCKFPGX" \
                                       "ULLAHXTSRXDEMKFKABUTAABSLNQBNMXNEPODPGAORYJXCHCGKECLJVRBPRLHORREEIZOBSHDSCETT" \
                                       "TNFTSMQPQIJBLKNZDMXOTRBNMTKHHCZQQMSLOAXJQKRHDGZVGITHYGVDXRTVBJEAHYBYRYKJAVXPO" \
                                       "KHFFMEPHAGFOOPFNKQAUGYLVPWUJUPCUGGIXGRAMELUTEPYILBIUOCKKUUBJROQFTXMZRLXBAMHSD" \
                                       "TEKRRIKZUFNLGTQAEUINMBPYTWXULQNIIRXHHGQDPENXAJNWXULFBNKBRINUMTRBFWBYVNKNKDFR"

    shortest_length_so_far: int = float("inf")
    shortest_sequence_indices: Tuple[int, int] = (-1, -1)

    for start_index in range(len(the_string_we_are_searching)):
        the_letters_we_are_looking_for: List[str] = list("ABCDA")

        starting_letter: str = the_string_we_are_searching[start_index]

        if starting_letter not in the_letters_we_are_looking_for:
            continue

        for stop_index in range(start_index + 1, len(the_string_we_are_searching)):

            if (stop_index - start_index) > (shortest_length_so_far - 1):
                break

            current_letter: str = the_string_we_are_searching[stop_index - 1]

            try:
                the_letters_we_are_looking_for.remove(current_letter)
            except ValueError:
                pass

            if len(the_letters_we_are_looking_for) == 0:
                shortest_length_so_far = stop_index - start_index
                shortest_sequence_indices = (start_index, stop_index)

    start_of_shortest_sequence, end_of_shortest_sequence = shortest_sequence_indices

    print(the_string_we_are_searching[start_of_shortest_sequence: end_of_shortest_sequence])
