import random
import string

with open('palabras_rae.txt', 'r', newline="\r\n", encoding="utf-8") as words:
    def read(listWords):
        words_rae = []
        for word in listWords:
            words_rae.append(word.replace("\r\n", ""))
        return words_rae
    dictionary = read(words)
    acentos = ["á", "é", "í", "ó", "ú"]
    randomWord = random.choice(dictionary)
    index = 0
    while True:
        if index == len(randomWord):
            wordOfDay = randomWord
            break
        elif acentos[index] not in randomWord:
            index += 1
        else:
            randomWord = random.choice(dictionary)

def playerGuess(word):
    if len(word) > 5 or len(word) <= 4:
        print("La palabra debe contener 5 letras")
        return playerGuess(str(input()))
    else:
        for letter in word:
            if letter not in string.ascii_lowercase:
                print("La palabra solo debe tener letras: ")
                playerGuess(str(input()))
    return word

def wordle(guess, wordOfDay):
    rounds = 1
    while True:
        correct = []
        missplaced = []
        fails = []
        if guess not in dictionary:
            print("Se necesita agregar otra palabra de 5 letras que se encuentre en el diccionario")
            guess = playerGuess(str(input()))
        if guess == wordOfDay:
            correct = [0,1,2,3,4]
            missplaced = []
            fails = []
            return correct, missplaced, fails
        for index in range(len(wordOfDay)):
            if guess[index] == wordOfDay[index]:
                correct.append(index)
            elif guess[index] != wordOfDay[index] and guess[index] in wordOfDay:
                missplaced.append(index)
            else:
                fails.append(index)
        print(f'Ronda {rounds} terminada.\nPosicion letras correctas:{correct}.\nPosicion letras mal ubicadas: {missplaced}.\nPosicion letras incorrectas: {fails}.')
        rounds += 1
        if rounds > 6:
            return correct, missplaced, fails
        elif rounds == 6:
            print("Ultima ronda")
        guess = playerGuess(str(input()))

print(f'La palabra del dia es: {wordOfDay}')
guess = playerGuess(str(input()))
print(f'La palabra del usuario es: {guess}')
correct, missplaced, fails = wordle(guess, wordOfDay)

print(f'Posicion de las letras correctas: {correct}')
print(f'Posicion de las letras incorrectas: {missplaced}')
print(f'Posicion de las letras no encontradas: {fails}')
