from vectorize import *


def readAllDocs(path):
    import os
    docs = {}
    for root, dirs, files in os.walk(path):
        for filename in files:
            path = root + '/' + filename
            with open(path, 'r', encoding="ISO-8859-1") as f:
                docs.setdefault(path, f.read())
    return docs


def vectorizeAllDocs(docs):
    words = allWords(list(docs.values()))
    dicts = allDicts(list(docs.values()))
    vectorizedDocs = {}
    for path in docs.keys():
        vectorizedDocs.setdefault(path, vectorize(docs[path], words, dicts))
    return vectorizedDocs

if __name__ == "__main__":
    print(vectorizeAllDocs(readAllDocs('./samples')))
