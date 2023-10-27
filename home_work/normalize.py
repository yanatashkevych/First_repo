import re

CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "yo", "zh", "z", "i", "ji", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", 
               "f", "h", "ts", "ch", "sh", "shch", "", "y", "'", "e", "yu", "ya", "ye", "i", "yi", "g")

TRANS = dict()

for cyrillic, latin in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cyrillic)] = latin
    TRANS[(ord(cyrillic.upper()))] = latin.upper()

def normalize(name:str) -> str:
    translate_name = re.sub(r'[^a-zA-Z0-9_\.]', '_', name.translate(TRANS))
    return translate_name

if __name__ == "__main__":
    print(normalize('розширення.не зникають.txt'))
