import words
import secrets
from binascii import crc32

def get_checksum(phrase):
    """Given a mnemonic word string, return a string of the computed checksum.
    :rtype: str
    """
    phrase = phrase.split(" ")
    wstr = "".join(word[:3] for word in phrase)
    wstr = bytearray(wstr.encode('utf-8'))
    z = ((crc32(wstr) & 0xffffffff) ^ 0xffffffff ) >> 0
    z2 = ((z ^ 0xffffffff) >> 0) % len(phrase)
    return phrase[z2]

def generate():
    out = [secrets.choice(words.word_list) for i in range(24)]
    checksum = get_checksum(" ".join(out))
    out.append(checksum)
    return " ".join(out)


