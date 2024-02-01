from datetime import datetime

class WordleComparison:
    def __init__(self, attempt: str, answer: str):
        self.attempt = attempt.upper()
        self.answer = answer.upper()
        self.answerLetterCount = {letter : self.answer.count(letter) for letter in set(self.answer)}
        self.correctLetterIndices = self.__getCorrectLetterIndices()
        self.missplacedLetterIndices, self.wrongLetterIndices = self.__getMissplacedAndWrongLetterIndices()
    
    def __getCorrectLetterIndices(self) -> list:
        self.correctLetterIndices = []
        for index in range(0, len(self.answer)):
            if self.attempt[index] == self.answer[index]:
                self.correctLetterIndices.append(index)
                self.answerLetterCount[self.attempt[index]] -= 1
        return self.correctLetterIndices
    def __getMissplacedAndWrongLetterIndices(self) -> tuple[list,list]:
        self.missplacedLetterIndices = []
        self.wrongLetterIndices = []
        for index in range(0,len(self.answer)):
            if self.attempt[index] != self.answer[index]:
                if  self.attempt[index] in self.answer and self.answerLetterCount[self.attempt[index]] > 0:
                    self.missplacedLetterIndices.append(index)
                    self.answerLetterCount[self.attempt[index]] -= 1
                else:
                    self.wrongLetterIndices.append(index)
        return self.missplacedLetterIndices, self.wrongLetterIndices

class StartingDate:
    startingDate = None
    def __new__(cls, year, month, day):
        if cls.startingDate is None:
            cls.startingDate = super(StartingDate, cls).__new__(cls)
            cls.year = year
            cls.month = month
            cls.day = day
            cls.timestamp = cls.startingDate.getTimestamp()
        return cls.startingDate
    def getTimestamp(self):
        startingDateTimestamp = datetime(self.year,self.month,self.day).timestamp()
        return int(startingDateTimestamp)

def getDaysSinceStartingDate(startingDateTimestamp):
    secondsInADay = 60*60*24
    daysSinceStartingDate = ((int(datetime.now().timestamp()) - startingDateTimestamp)//(secondsInADay)) + 1
    return daysSinceStartingDate

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

    def __getTodaysAnswer(self) -> str:
        startingDate = StartingDate(2024,1,1)
        todaysAnswer = self.validWordsList[getDaysSinceStartingDate(startingDate.timestamp)]
        return todaysAnswer

def todaysWordleGame(playerAttempts) -> list:
    validWords = ValidWords()
    payload = []
    for round in range(len(playerAttempts)):
        playersAttempt = playerAttempts[round]
        currentWordleComparison = WordleComparison(playersAttempt, validWords.todaysAnswer)
        payload.append ({
            "word": playersAttempt,
            "correct" : currentWordleComparison.correctLetterIndices,
            "missplaced" : currentWordleComparison.missplacedLetterIndices,
            "fails" : currentWordleComparison.wrongLetterIndices
        })
    return payload
