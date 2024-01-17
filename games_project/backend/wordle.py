def wordle(word: str, wordOfTheDay: str):
    word.lower()
    missplaced = []
    correct = []
    wordDict = {"M":1, "A":2, "R":1, "I":1}

    fails = []
    if word == wordOfTheDay:
        missplaced = [] 
        fails = []
        correct = [0, 1, 2, 3, 4]
        return missplaced, fails, correct
    else:
    for index in range(0, len(wordOfTheDay)):
        if word[index] == wordOfTheDay[index]:
            correct.append(index)
        elif word[index] in wordOfTheDay:
            missplaced.append(index) #AGUAS CON VARIAS LETRAS IGUALES
        else:
            fails.append(index)
        
    return correct

print(wordle("MARIA", "caras"))
