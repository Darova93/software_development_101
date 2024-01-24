class WordleComparison:
    def __init__(self, playerGuess: str, correctWord: str):
        self.playerGuess = playerGuess.upper()
        self.correctWord = correctWord.upper()
        self.answerLetterCount = {letter : self.correctWord.count(letter) for letter in set(self.correctWord)}
        self.correctLetterIndices = self.__getCorrectLetterIndices()
        self.missplacedLetterIndices, self.wrongLetterIndices = self.__getMissplacedAndWrongLetterIndices()
    
    def __getCorrectLetterIndices(self) -> list:
        self.correctLetterIndices = []
        for index in range(0, len(self.correctWord)):
            if self.playerGuess[index] == self.correctWord[index]:
                self.correctLetterIndices.append(index)
                self.answerLetterCount[self.playerGuess[index]] -= 1
        return self.correctLetterIndices
    def __getMissplacedAndWrongLetterIndices(self) -> tuple[list,list]:
        self.missplacedLetterIndices = []
        self.wrongLetterIndices = []
        for index in range(0,len(self.correctWord)):
            if self.playerGuess[index] != self.correctWord[index]:
                if  self.playerGuess[index] in self.correctWord and self.answerLetterCount[self.playerGuess[index]] > 0:
                    self.missplacedLetterIndices.append(index)
                    self.answerLetterCount[self.playerGuess[index]] -= 1
                else:
                    self.wrongLetterIndices.append(index)
        return self.missplacedLetterIndices, self.wrongLetterIndices
