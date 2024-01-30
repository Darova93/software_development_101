from datetime import datetime

#Tenemos que decidir si queremos que el archivo de las validWords y de las answers sea el mismo o no (probablemente no)
class WordleComparison:
    def __init__(self, playerGuess: str, answer: str):
        self.playerGuess = playerGuess.upper()
        self.answer = answer.upper()
        self.answerLetterCount = {letter : self.answer.count(letter) for letter in set(self.answer)}
        self.correctLetterIndices = self.__getCorrectLetterIndices()
        self.missplacedLetterIndices, self.wrongLetterIndices = self.__getMissplacedAndWrongLetterIndices()
    
    def __getCorrectLetterIndices(self) -> list:
        self.correctLetterIndices = []
        for index in range(0, len(self.answer)):
            if self.playerGuess[index] == self.answer[index]:
                self.correctLetterIndices.append(index)
                self.answerLetterCount[self.playerGuess[index]] -= 1
        return self.correctLetterIndices
    def __getMissplacedAndWrongLetterIndices(self) -> tuple[list,list]:
        self.missplacedLetterIndices = []
        self.wrongLetterIndices = []
        for index in range(0,len(self.answer)):
            if self.playerGuess[index] != self.answer[index]:
                if  self.playerGuess[index] in self.answer and self.answerLetterCount[self.playerGuess[index]] > 0:
                    self.missplacedLetterIndices.append(index)
                    self.answerLetterCount[self.playerGuess[index]] -= 1
                else:
                    self.wrongLetterIndices.append(index)
        return self.missplacedLetterIndices, self.wrongLetterIndices

class ValidWords:
    def __init__(self):
        raeFile = "./public/palabras_rae.txt"
        self.fileName = raeFile
        self.validWordsList = self.__createValidWordsList()
        self.todaysAnswer = self.__getTodaysAnswer()
    
    def __createValidWordsList(self) -> list:
        with open(self.fileName, "r", newline="\r\n", encoding="utf-8") as file:
            validWords = list()
            for word in file:
                validWords.append(word.replace("\r\n", "").upper())
        return validWords

#Eventualmente __getAnswer(self)
    def __getTodaysAnswer(self) -> str:
        startTime = 1704096000 #Enero 01 del 2024 00:00 AM
        checkTime = int(datetime.timestamp(datetime.now()))
        segundos = checkTime - startTime
        todaysAnswer = self.validWordsList[int(segundos/86400)]
        return todaysAnswer

#def dictionaryRaeRandomWord(file="./public/palabras_rae.txt"):
#    validWords = ValidWords(file)
#    return validWords.todaysAnswer

#Eventualmente wordleGame() o wordleGameNumber()
def todaysWordleGame(playerAttempts) -> list:
    validWords = ValidWords()
    #playersLastAttempt = playerAttempts[-1]['word']
    #currentWordleComparison = WordleComparison(playersLastAttempt, validWords.todaysAnswer)
    #playerAttempts[-1] = {
    #    "word": playersLastAttempt,
    #    "correct" : currentWordleComparison.correctLetterIndices,
    #    "missplaced" : currentWordleComparison.missplacedLetterIndices,
    #    "wrong" : currentWordleComparison.wrongLetterIndices
    #}
    #return playerAttempts
    payload = []
    for round in range(len(playerAttempts)):
        playersAttempt = playerAttempts[round]['word']
        currentWordleComparison = WordleComparison(playersAttempt, validWords.todaysAnswer)
        payload.append ({
            "word": playersAttempt,
            "correct" : currentWordleComparison.correctLetterIndices,
            "missplaced" : currentWordleComparison.missplacedLetterIndices,
            "wrong" : currentWordleComparison.wrongLetterIndices
        })
    return payload

