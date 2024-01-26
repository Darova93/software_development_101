from datetime import datetime

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

class RandomWordPicker:
    def __init__(self, fileName):
        self.fileName = fileName
        self.wordList = self.__createListDictionary()
        self.todaysAnswer = self.__getTodaysAnswer()
    
    def __createListDictionary(self) -> list:
        with open(self.fileName, "r", newline="\r\n", encoding="utf-8") as file:
            listDictionary = list()
            for word in file:
                listDictionary.append(word.replace("\r\n", "").upper())
        return listDictionary
    
    def __getTodaysAnswer(self) -> str:
        startTime = 1704096000 #Enero 01 del 2024 00:00 AM
        checkTime = int(datetime.timestamp(datetime.now()))
        segundos = checkTime - startTime
        todaysAnswer = self.wordList[int(segundos/86400)]
        return todaysAnswer

def dictionaryRaeRandomWord(file="./public/palabras_rae.txt"):
    wordList = RandomWordPicker(file)
    return wordList.todaysAnswer

def wordleGame(playerAttempts, answer) -> list:
    payload = []
    for round in range(len(playerAttempts)):
        playerGuess = playerAttempts[round]['word']
        currentWordleComparison = WordleComparison(playerGuess, answer)
        payload.append ({
            "word": playerGuess,
            "correct" : currentWordleComparison.correctLetterIndices,
            "missplaced" : currentWordleComparison.missplacedLetterIndices,
            "wrong" : currentWordleComparison.wrongLetterIndices
        })
    return payload

