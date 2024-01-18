def wordle(testingWord: str, wordOfTheDay: str):
    testingWord.upper()
    wordOfTheDay.upper()
    right = []
    missplaced = []
    wrong = []
    letterCount = {letter : wordOfTheDay.count(letter) for letter in set(wordOfTheDay)}
    testLetters = list(testingWord)
    remainingLetters = wordOfTheDay
    for index in range(0, len(wordOfTheDay)):
        if testingWord[index] == wordOfTheDay[index]:
            right.append(index)
            testLetters[index] = 0
            remainingLetters.replace(testingWord[index],'',1)
            letterCount[testingWord[index]] -= 1
            
    for index in range(0,len(wordOfTheDay)):
        if testLetters[index] in remainingLetters:
            missplaced.append(index)
            remainingLetters.replace(testingWord[index],'',1)
        elif testLetters[index] != 0:
            wrong.append(index)

        if letterCount[testingWord[index]] > 0 and testingWord[index] in wordOfTheDay:
            missplaced.append(index)
        else:
            wrong.append(index)


    return right, missplaced, wrong
