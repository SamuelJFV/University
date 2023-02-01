
from unidecode import unidecode
from random import uniform
import string

def IncrementCount(probability : float = 0.5):

    value = uniform(0,1)
    return int(value < probability)

def ExactCount(characters : str):

    counts = dict.fromkeys(string.ascii_uppercase, 0)

    for character in characters:
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1

    return counts

def FilterLetters(characters : str):

        characters = unidecode(characters)
        characters = ''.join(filter(str.isalpha, characters))
        return characters.upper()

def Load(fileName : str):

        file = open("Books/" + fileName, "r", encoding = 'utf-8')
        fileString = file.read()
        file.close()
        return fileString