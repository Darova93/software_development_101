import random

with open('palabras_rae.txt', 'r', newline="\r\n", encoding="utf-8") as words:
    def read(listWords):
        words_rae = []
        for word in listWords:
            words_rae.append(word.replace("\r\n", ""))
        return words_rae
    dictionary = read(words)
    wordOfDay = (random.choice(dictionary)).upper()

#Palabra random cada que se ejecuta el programa    
print(wordOfDay)
correct = []
missplaced = []
fails = []

guess = str(input())
print(guess.upper())
if guess not in dictionary:
    print("Se necesita agregar una palabra de 5 letras")
elif len(guess) > 5 or len(guess) < 5:
    print("Se necesita una palabra de 5 letras")
elif guess == wordOfDay:
    correct = [0,1,2,3,4]
    missplaced = []
    fails = []
else:
    print(f'La palabra del dia es: {wordOfDay}')
    print(f'La palabra guess es: {guess.upper()}')
    round = 6
    for index in range(5):
        if guess[index] == wordOfDay[index]:
            correct.append(index)
        elif guess[index] != wordOfDay[index]  and guess[index] in wordOfDay:
            missplaced.append(index)
        else:
            fails.append(index)

print(f'Posicion de las letras correctas: {correct}')
print(f'Posicion de las letras incorrectas: {missplaced}')
print(f'Posicion de las letras no encontradas: {fails}')
