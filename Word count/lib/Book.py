
from unidecode import unidecode
import string
from nltk.corpus import stopwords

def Load(path : str):
        
        """Returns a string of a file from a given path"""
        
        with open(path, "r", encoding = 'utf-8') as file:
            fileString = file.read()

        return fileString

def FilterLetters(rawString: str):

        """Returns a string containing lowercase letters without any punctuation, given string as the argument"""

        filteredString = rawString.translate(str.maketrans('', '', string.punctuation))
        return filteredString.lower()

def RemoveStopWords(words: list, language : str = "english"):

    """Returns a new list of words without stop-words from a given list of words"""

    stopWords = set(stopwords.words(language))
    newWords = [word for word in words if word not in stopWords]

    return newWords

def __main():
    print(FilterLetters("Hélló World! #?123"))
    return

if __name__ == "__main__":
    
    # Used for debbuging
    
    __main()