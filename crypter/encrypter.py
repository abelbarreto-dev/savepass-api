from typing import Generator


def is_str_greater_than_one(w1, w2) -> bool:
    if not isinstance(w1, str) or not isinstance(w2, str):
        return False
    elif w1.__len__() < 2:
        return False
    else:
        return True


def get_len_half(word: str) -> dict:
    return {
        'length': word.__len__(),
        'half': word.__len__() // 2
    }


def str_to_generate(str_word: str = '') -> Generator:
    for wrd in str_word:
        yield ord(wrd)


def mix_half_str(str_word: str) -> str:
    half = get_len_half(str_word)['half']
    str_word = ''.join(reversed(str_word))
    str_word = ''.join((str_word[half:], str_word[:half]))
    return str_word


def get_indexes_tuple(word: tuple, item: int, many: int) -> tuple:
    indexes = ()
    for i in range(many):
        idx = word.index(item)
        indexes += (idx,)
        word = word[idx+1:]
    return indexes


def mix_equal_no_pair_length(str_word: str) -> str:
    if get_len_half(str_word)['length'] % 2 == 0:
        return str_word
    return f'ŧ{str_word}'


class Encrypt:

    @classmethod
    def encrypt_word(cls, word: str, passwd: str = '') -> str:
        if not is_str_greater_than_one(w1=word, w2=passwd):
            return ''
        word = f'{word[0]}{passwd}{word[1:]}'
        passwd = None
        word = mix_equal_no_pair_length(str_word=word)
        word = mix_half_str(str_word=word)
        word = str_to_generate(str_word=word)
        word = cls._encrypt_maker(word_codes=word)
        return f'=={"".join(chr(i) for i in word)}'

    @classmethod
    def _encrypt_maker(cls, word_codes: Generator) -> Generator:
        wd_encrypted = [i for i in word_codes]
        special = (
            get_indexes_tuple(tuple(wd_encrypted), 126, wd_encrypted.count(126)),
            get_indexes_tuple(tuple(wd_encrypted), 32, wd_encrypted.count(32)),
            get_indexes_tuple(tuple(wd_encrypted), 160, wd_encrypted.count(160))
        )
        for spc in special:
            if not spc:
                continue
            for i in spc:
                if wd_encrypted[i] in (32, 161):
                    wd_encrypted = wd_encrypted[:i] + [169] + wd_encrypted[i:]
                elif wd_encrypted[i] == 126:
                    wd_encrypted = wd_encrypted[:i] + [174] + wd_encrypted[i:]
        if wd_encrypted.__len__() % 2 != 0:
            wd_encrypted += [ord('ŧ')]
        index = 0
        length = wd_encrypted.__len__()
        while True:
            if wd_encrypted[index] in (169, 174):
                if wd_encrypted[index] == 169:
                    wd_encrypted[index+1] += 1
                else:
                    wd_encrypted[index+1] -= 1
                index += 1
            elif index % 2 == 0:
                wd_encrypted[index] += 2
            else:
                wd_encrypted[index] += 1
            index += 1
            if index == length:
                break
        return (index for index in wd_encrypted)
