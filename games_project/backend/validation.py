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
        words.append(jsonData[attempt]["word"].upper())
    return words

def checkSpecialCaractersInValidWords(words):
    validWords = ValidWords()
    specialLetters = ["Á", "É", "Í", "Ó", "Ú", "Ñ", "Ü"]
    normalLetters = ["A", "E", "I", "O", "U", "N", "U"]
    newWords = list()
    for roundWord in words:
        roundWord.upper()
        newRoundWord = list()
        for letter in range(len(specialLetters)):
            if specialLetters[letter] in validWords.todaysAnswer:
                indexAnswer = validWords.todaysAnswer.find(specialLetters[letter])
                if normalLetters[letter] == roundWord[indexAnswer]:
                    newRoundWord = list(roundWord)
                    newRoundWord[indexAnswer] = specialLetters[letter]
                    newRoundWord = "".join(newRoundWord)
        if newRoundWord in validWords.validWordsList:
            newWords.append(newRoundWord)
        else:
            newWords.append(roundWord)
    return newWords
