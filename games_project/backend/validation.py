from wordle import ValidWords

def validateRequest(jsonData: list):
    for attempt in range(len(jsonData)):
        try:
            if len(jsonData[attempt]["word"]) != 5:
                return None
        except TypeError:
            return None
    return jsonData

def checkDictionaryListWords(jsonData: list):
    validWords = ValidWords()
    words = []
    for attempt in range(len(jsonData)):
        if (jsonData[attempt]["word"]).upper() not in validWords.validWordsList:
            return None
        words.append(jsonData[attempt]["word"])
    return words

def checkingSpecialCaractersInValidWords(words):
    specialLetters = ["Á", "É", "Í", "Ó", "Ú", "Ñ", "Ü"]
    normalLetters = ["A", "E", "I", "O", "U", "N", "U"]
    #validWords = ValidWords()
    #todaysAnswer = validWords.todaysAnswer
    index = 0
    indexLetters = 0
    newWords = list()
    for round in range(len(words)):
        while index < len(specialLetters):
            if specialLetters[indexLetters]
                change = words[round].replace()
        newWords.append(change)
