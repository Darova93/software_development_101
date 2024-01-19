class wordle:

    right = []
    missplaced = []
    wrong = []
    letterCount = {letter : wordOfTheDay.count(letter) for letter in set(wordOfTheDay)}

    def __init__(self, guess: str, wordOfTheDay: str):
        self.guess = guess.upper()
        self.wordOfTheDay = wordOfTheDay.upper()
    
    def _getRightPositions(guess, wordOfTheDay):
        for index in range(0, len(wordOfTheDay)):
            if guess[index] == wordOfTheDay[index]:
                right.append(index)
                letterCount[guess[index]] -= 1
        return right
    
    def _getMissplacedAndWrongPositions(guess, wordOfTheDay):
        for index in range(0,len(wordOfTheDay)):
            if guess[index] != wordOfTheDay[index]:
                if  guess[index] in wordOfTheDay and letterCount[guess[index]] > 0:
                    missplaced.append(index)
                    letterCount[guess[index]] -= 1
                else:
                    wrong.append(index)
        return missplaced, wrong
    
    return (_getRightPositions(guess,wordOfTheDay),_getMissplacedAndWrongPositions(guess,wordOfTheDay))
    print(wordle('atara','maria'))

