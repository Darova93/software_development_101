import random
class WordOfTheDay:
    def __init__(self, fileName):
        self.fileName = fileName
    
    def fileDictionary(self):
        with open(self.fileName, "r", newline="\r\n", encoding="utf-8") as file:
            wordsRae = list()
            for word in file:
                wordsRae.append(word.replace("\r\n", ""))
        return wordsRae
    
    def randomWordWithoutAccent(self):
        accent = ["á", "é", "í", "ó", "ú"]
        randomWord = random.choice(self.fileDictionary())
        index = 0
        while True:
            if index == len(randomWord)-1:
                wordOfDay = randomWord
                break
            elif accent[index] not in randomWord:
                index += 1
            else:
                randomWord = random.choice(self.fileDictionary())
                index = 0
        return wordOfDay

#wordOfTheDay = WordOfTheDay('./palabras_rae.txt')
wordOfTheDay = WordOfTheDay('./test_doc.txt')
print(wordOfTheDay.randomWordWithoutAccent())
