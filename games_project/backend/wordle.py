def wordle(testWord: str, wordOfTheDay: str):
    testWord.upper()
    wordOfTheDay.upper()
    right = []
    missplaced = []
    wrong = []
    #letterCount = {letter : wordOfTheDay.count(letter) for letter in set(wordOfTheDay)}
    testLetters = list(testWord)
    remainingLetters = wordOfTheDay
    for index in range(0, len(wordOfTheDay)):
        if testWord[index] == wordOfTheDay[index]:
            right.append(index)
            testLetters[index] = 0
            remainingLetters.replace(testWord[index],'',1)
    for index in range(0,len(wordOfTheDay)):
        if testLetters[index] in remainingLetters:
            missplaced.append(index)
            remainingLetters.replace(testWord[index],'',1)
        elif testLetters[index] != 0:
            wrong.append(index)
    return right, missplaced, wrong
