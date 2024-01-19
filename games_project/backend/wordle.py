class wordle:
    wordOfTheDay = ''
    guess = ''
    def __init__(self, guess: str, wordOfTheDay: str):
        self.guess = guess.upper()
        self.wordOfTheDay = wordOfTheDay.upper()
        self.wordOfTheDayLetterCount = {letter : self.wordOfTheDay.count(letter) for letter in set(self.wordOfTheDay)}
    def _getCorrectLetterIndices(self):
        correctLetterIndices = []
        for index in range(0, len(self.wordOfTheDay)):
            if self.guess[index] == self.wordOfTheDay[index]:
                correctLetterIndices.append(index)
                self.wordOfTheDayLetterCount[self.guess[index]] -= 1
        return correctLetterIndices
    def _getMissplacedAndWrongLetterIndices(self):
        missplacedLetterIndices = []
        wrongLetterIndices = []
        for index in range(0,len(self.wordOfTheDay)):
            if self.guess[index] != self.wordOfTheDay[index]:
                if  self.guess[index] in self.wordOfTheDay and self.wordOfTheDayLetterCount[self.guess[index]] > 0:
                    missplacedLetterIndices.append(index)
                    self.wordOfTheDayLetterCount[self.guess[index]] -= 1
                else:
                    wrongLetterIndices.append(index)
        return missplacedLetterIndices, wrongLetterIndices
