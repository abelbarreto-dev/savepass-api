from typing import Generator


def get_word_out_pass(word: str, passwd: str) -> str:
    if word[0] == 'ŧ':
        word = word[1:]
    if word[-1] == 'ŧ':
        word = word[:-1]
    start = word.index(passwd)
    length = passwd.__len__() + start
    pass_check = word[start: length]
    return word[:start] + word[length:] if pass_check == passwd else ''


def get_len_half(word: str) -> dict:
    return {
        'length': word.__len__(),
        'half': word.__len__() // 2
    }


def mix_half_str(str_word: str) -> str:
    half = get_len_half(str_word)['half']
    str_word = ''.join(reversed(str_word))
    str_word = ''.join((str_word[half:], str_word[:half]))
    return str_word


def get_out_special(word: Generator) -> Generator:
    return (wd for wd in word if wd not in (169, 174))


def str_to_generate(str_word: str = '') -> Generator:
    for wrd in str_word:
        yield ord(wrd)


class Decrypt:

    @classmethod
    def decrypt_word(cls, word: str, passwd: str) -> str:
        word = word[2:]
        word = str_to_generate(str_word=word)
        word = cls.decrypt_maker(word_codes=word)
        word = get_out_special(word=word)
        word = ''.join(chr(i) for i in word)
        word = mix_half_str(str_word=word)
        word = get_word_out_pass(word=word, passwd=passwd)
        return word

    @classmethod
    def decrypt_maker(cls, word_codes: Generator) -> Generator:
        wd_decrypted = [i for i in word_codes]
        length = wd_decrypted.__len__()
        index = 0
        while True:
            if wd_decrypted[index] in (169, 174):
                if wd_decrypted[index] == 169:
                    wd_decrypted[index + 1] -= 1
                else:
                    wd_decrypted[index + 1] += 1
                index += 1
            elif index % 2 == 0:
                wd_decrypted[index] -= 2
            else:
                wd_decrypted[index] -= 1
            index += 1
            if index == length:
            break
        return get_out_special(word=(i for i in wd_decrypted))
