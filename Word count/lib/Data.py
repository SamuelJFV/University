
import pickle

def Save(fileName : str, data):
    file = open("Data/"+fileName, "wb")
    pickle.dump(data, file)
    file.close()

def Load(fileName : str):
    file = open("Data/"+fileName, "rb")
    output = pickle.load(file)
    file.close()
    return output