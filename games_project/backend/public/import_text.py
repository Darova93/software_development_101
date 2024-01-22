from random import choice
class WordOfTheDay:
    def __init__(self, fileName):
        self.fileName = fileName
    
    def fileDictionary(self):
        with open(self.fileName, "r", newline="\r\n", encoding="utf-8") as file:
            wordsRae = list()
            for word in file:
                wordsRae.append(word.replace("\r\n", "").upper())
        return wordsRae
    
    def randomWord(self):
        accent = ["Á", "É", "Í", "Ó", "Ú"]
        randomWord = choice(self.fileDictionary())
        index = 0
        while True:
            if index == len(randomWord)-1:
                wordOfDay = randomWord
                break
            elif accent[index] not in randomWord:
                index += 1
            else:
                randomWord = choice(self.fileDictionary())
                index = 0
        return wordOfDay

#wordOfTheDay = WordOfTheDay('./palabras_rae.txt')
#wordOfTheDay = WordOfTheDay('./test_doc.txt')
#print(wordOfTheDay.randomWord())
