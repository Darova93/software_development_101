from wordle import ValidWords

def isStatusValid(gameStatus):
    if gameStatus == "NEW" or gameStatus == "CONTINUE":
        return True
    return False

def isTheLastAttemptValid(lastAttempt):
    if not isinstance(lastAttempt,str):
        return False
    if not lastAttempt.isalpha():
        return False
    if not len(lastAttempt)==5:
        return False
    if not isAttemptInTheList(lastAttempt):
        return False
    return True

def isLastAttemptAFiveLetterWord(wordleRequest):
    for turn in range(len(wordleRequest["words"])):
        word = wordleRequest["words"][turn]["word"]
        if len(word) != 5:
            return False
    return True

def isAttemptInTheList(attempt):
    validWords = ValidWords()
    playerWords = []
    for turn in range(len(attempt["words"])):
        if (attempt["words"][turn]["word"]).upper() not in validWords.validWordsList:
            return None
    return attempt

def checkSpecialCaractersInValidWords(words):
    validWords = ValidWords()
    specialLetters = ["Á", "É", "Í", "Ó", "Ú", "Ñ", "Ü"]
    normalLetters = ["A", "E", "I", "O", "U", "N", "U"]
    newWords = list()
    for roundWord in words:
        roundWord.upper()
        newRoundWord = list()
        for letter in range(len(specialLetters)):
            if specialLetters[letter] in validWords.todaysAnswerNoAccentMark:
                indexAnswer = validWords.todaysAnswerNoAccentMark.find(specialLetters[letter])
                if normalLetters[letter] == roundWord[indexAnswer]:
                    newRoundWord = list(roundWord)
                    newRoundWord[indexAnswer] = specialLetters[letter]
                    newRoundWord = "".join(newRoundWord)
        if newRoundWord in validWords.validWordsList:
            newWords.append(newRoundWord)
        else:
            newWords.append(roundWord)
    return newWords

def isValid(wordleRequest):
