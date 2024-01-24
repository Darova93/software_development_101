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

class RandomWordFromDictionary:
    def __init__(self, fileName):
        self.fileName = fileName
        self.listDictionary = self.__createListDictionary()
        self.wordOfDay = self.__getWordofDay()
    
    def __createListDictionary(self):
        with open(self.fileName, "r", newline="\r\n", encoding="utf-8") as file:
            listDictionary = list()
            for word in file:
                listDictionary.append(word.replace("\r\n", "").upper())
        return listDictionary
    
    def __getWordofDay(self):
        startTime = 1704096000 #Enero 01 del 2024 00:00 AM
        #checkTime = 1706083200 Enero 24 del 2024 00:00 AM
        checkTime = int(datetime.timestamp(datetime.now()))
        segundos = checkTime - startTime
        minutos = segundos // 60
        horas = minutos // 60
        dias = horas // 24
        wordOfDay = self.listDictionary[minutos%60]
        return wordOfDay

def dictionaryRaeRandomWord(file="./public/palabras_rae.txt"):
    dictionary = RandomWordFromDictionary(file)
    return dictionary.wordOfDay

def wordleGame(data, answer):
    payload = []
    for guess in range(len(data)):
        playerGuess = data[guess]['word']
        currentWordleComparison = WordleComparison(playerGuess, answer)
        payload.append ({
            "word": playerGuess,
            "correct" : currentWordleComparison.correctLetterIndices,
            "missplaced" : currentWordleComparison.missplacedLetterIndices,
            "wrong" : currentWordleComparison.wrongLetterIndices
        })
    return payload

#def isItPluralWord(playerGuess: str):
#    if playerGuess[-1] == "s" and playerGuess[-2] == "e":
#        threeLetterWords = WordOfTheDay("./public/03.txt")
#        playerGuess.pop()
#        playerGuess.pop()
#        if playerGuess in threeLetterWords.fileDictionary()
#            return True
#    elif playerGuess[-1] == "s":
#        fourLetterWords = WordOfTheDay("./public/04.txt")
#        playerGuess.pop()
#        if playerGuess in fourLetterWords.fileDictionary()
#            return True
#    else:
#        if playerGuess in fiveLetterWords.fileDictionary()
