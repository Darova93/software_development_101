class WordleAttempt:
 #   answer = ''
 #   guess = ''
 #   correctLetterIndices = []
 #   missplacedLetterIndices = []
 #   wrongLetterIndices = []
    def __init__(self, guess: str, answer: str):
        self.guess = guess.upper()
        self.answer = answer.upper()
        self.answerLetterCount = {letter : self.answer.count(letter) for letter in set(self.answer)}
        self.correctLetterIndices = self.__getCorrectLetterIndices()
        self.missplacedLetterIndices, self.wrongLetterIndices = self.__getMissplacedAndWrongLetterIndices()
    
    def __getCorrectLetterIndices(self) -> list:
        self.correctLetterIndices = []
        for index in range(0, len(self.answer)):
            if self.guess[index] == self.answer[index]:
                self.correctLetterIndices.append(index)
                self.answerLetterCount[self.guess[index]] -= 1
        return self.correctLetterIndices
    def __getMissplacedAndWrongLetterIndices(self) -> tuple[list,list]:
        self.missplacedLetterIndices = []
        self.wrongLetterIndices = []
        for index in range(0,len(self.answer)):
            if self.guess[index] != self.answer[index]:
                if  self.guess[index] in self.answer and self.answerLetterCount[self.guess[index]] > 0:
                    self.missplacedLetterIndices.append(index)
                    self.answerLetterCount[self.guess[index]] -= 1
                else:
                    self.wrongLetterIndices.append(index)
        return self.missplacedLetterIndices, self.wrongLetterIndices
