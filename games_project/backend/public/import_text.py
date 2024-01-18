import random
import time

with open('palabras_rae.txt', 'r', newline="\r\n", encoding="utf-8") as words:
    def read(listWords):
        words_rae = []
        for word in listWords:
            words_rae.append(word.replace("\r\n", ""))
        return words_rae
    
    wordOfDay = random.choice(read(words))

#Palabra random cada que se ejecuta el programa    
print(wordOfDay)

#Hora local, formas de fijarlo a fecha
print(time.localtime())
