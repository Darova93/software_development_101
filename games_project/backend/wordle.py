class wordle:

    correctLetterIndices = []
    missplacedLetterIndices = []
    wrongLetterIndices = []
    

    def __init__(self, guess: str, wordOfTheDay: str):
        self.guess = guess.upper()
        self.wordOfTheDay = wordOfTheDay.upper()
        self.wordOfTheDayLetterCount = {letter : self.wordOfTheDay.count(letter) for letter in set(self.wordOfTheDay)}

    def _getRightPositions(self):
        for index in range(0, len(self.wordOfTheDay)):
            if self.guess[index] == self.wordOfTheDay[index]:
                self.correctLetterIndices.append(index)
                self.wordOfTheDayLetterCount[self.guess[index]] -= 1
        return self.correctLetterIndices
    
    def _getMissplacedAndWrongPositions(self):
        for index in range(0,len(self.wordOfTheDay)):
            if self.guess[index] != self.wordOfTheDay[index]:
                if  self.guess[index] in self.wordOfTheDay and self.wordOfTheDayLetterCount[self.guess[index]] > 0:
                    self.missplacedLetterIndices.append(index)
                    self.wordOfTheDayLetterCount[self.guess[index]] -= 1
                else:
                    self.wrongLetterIndices.append(index)
        return self.missplacedLetterIndices, self.wrongLetterIndices
