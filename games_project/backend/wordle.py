def wordle(word: str, wordOfTheDay: str):
    word.lower()
    missplaced = []
    
    fails = []
    correct = []
    if word == wordOfTheDay:
        missplaced = [] 
        fails = []
        correct = [0, 1, 2, 3, 4]
        return missplaced, fails, correct
    for idx in word:



print(wordle("Tacos", "lunes"))
