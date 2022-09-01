import re


CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ja", "e", "je", "ji", "g")

TRANSLATER = {}

for k, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANSLATER[ord(k)] = l
    TRANSLATER[ord(k.upper())] = l.upper()


def normalize(string: str) -> str:
    new_string = string.translate(TRANSLATER)
    new_string = re.sub(r'\W', '_', new_string)
    return new_string


if __name__ == "__main__":
    print(normalize('Привет-Мир!123.jpg'))