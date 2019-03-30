docA = "the quick brown fox jumps over the lazy dog and"
docB = "never jump over the lazy dog quickly"

def bagOfWord(string):
    return string.replace("\n", " ").split(" ")

def allWords(strings):
    """ return all the possible word appeared in all string """
    words = ()
    for string in strings:
        words = set(words).union(bagOfWord(string))
    return words

def allDicts(strings):
    words = allWords(strings)
    return [ wordDict(string, words) for string in strings ]

def wordDict(string, allWords):
    """ 
        Return a (dict, dict) with
        - key: the word
        - value: the occurences of word in string
    """
    bow = bagOfWord(string)
    wordDict = { key : 0 for key in allWords }
    for word in bow:
        wordDict[word] = 1
    return wordDict

def computeTermFrequency(wordDict, string):
    """ compute TF of each word in a given string from the word dictionary """
    bow = bagOfWord(string)
    return { key: wordDict[key]/len(bow) for key in wordDict.keys() }
    

def computeInverseDocumentFrequency(wordDicts):
    """ return the word dictionary 
        - key : word
                                 total documents 
        - value:  log( ---------------------------------------- )
                         number of documents contain the word
    """
    from math import log
    totalDocuments = len(wordDicts)
    #count number of documents that contain this word
    idfDict = { key : 0 for key in wordDicts[0].keys()}
    for word in idfDict.keys():
        for wordDict in wordDicts:
            if wordDict[word]:
                idfDict[word] += 1
    return  { key : log(totalDocuments/idfDict[key]) for key in idfDict.keys()}


def computeTFIDF(TFWordDict, IDFWordDict):
    return { key : TFWordDict[key] * IDFWordDict[key] for key in TFWordDict.keys()}

def vectorize(string, allWords, allDicts):
    wdict = wordDict(string, allWords)
    tfDict = computeTermFrequency(wdict, string)
    idfDict = computeInverseDocumentFrequency(allDicts)
    return computeTFIDF(tfDict, idfDict)





if __name__ == "__main__":
    import os
    strings = []
    for root, dirs, files in os.walk("./ChiNhan/20_newsgroups/sample"):
        for filename in files:
            path = root + '/' + filename
            with open(path, 'r', encoding="ISO-8859-1") as f:
                strings.append(f.read())
    words = allWords(strings)
    dicts = allDicts(strings)
    d = {}
    print(vectorize(strings[0], words, dicts))
    pass


    
    



