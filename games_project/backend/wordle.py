def wordle(testWord: str, wordOfTheDay: str):
    testWord.upper()
    wordOfTheDay.upper()
    right = []
    missplaced = []
    wrong = []
    #letterCount = {letter : wordOfTheDay.count(letter) for letter in set(wordOfTheDay)}
    testLetters = list(testWord)
    for index in range(0, len(wordOfTheDay)):
        if testWord[index] == wordOfTheDay[index]:
            right.append(index)
            testLetters[index] = 0
            wordOfTheDay.replace(testWord[index],'',1)
    for index in range(0,len(wordOfTheDay)):
        if testLetters[index] in wordOfTheDay:
            missplaced.append(index)
            wordOfTheDay.replace(testWord[index],'',1)
        elif testLetters[index] != 0:
            wrong.append(index)
    return right, missplaced, wrong
