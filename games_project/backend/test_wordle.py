import pytest
from wordle import WordleComparison
@pytest.mark.parametrize("playerGuess, correctWord, expectedCorrectLetterIndices, expectedMissplacedLetterIndices, expectedWrongLetterIndices", 
                         [('avara', 'maria', [4], [0,3], [1,2]),
                          ('Burro', 'perro', [2,3,4], [], [0,1]),
                          ('HoYoS', 'huelo', [0], [1], [2,3,4]),
                          ('juego', 'juego', [0,1,2,3,4], [], [])])

def test_answer(playerGuess, correctWord, expectedCorrectLetterIndices, expectedMissplacedLetterIndices, expectedWrongLetterIndices):
    currentWordleComparison = WordleComparison(playerGuess, correctWord)
    assert(currentWordleComparison.correctLetterIndices == expectedCorrectLetterIndices)
    assert(currentWordleComparison.missplacedLetterIndices == expectedMissplacedLetterIndices)
    assert(currentWordleComparison.wrongLetterIndices == expectedWrongLetterIndices)
