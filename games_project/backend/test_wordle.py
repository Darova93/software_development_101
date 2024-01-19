import pytest
from wordle import wordle
@pytest.mark.parametrize("guess, wordOfTheDay, expectedCorrect, expectedMissplaced, expectedWrong", 
                         [('avara', 'maria', [4], [0,3], [1,2]),
                          ('Burro','perro', [2,3,4], [], [0,1])])

def test_answer(guess, wordOfTheDay, expectedCorrect, expectedMissplaced, expectedWrong):
    
    obj = wordle(guess, wordOfTheDay)
    correctLetterIndices = obj._getCorrectLetterIndices()
    missplacedLetterIndices,wrongLetterIndices = obj._getMissplacedAndWrongLetterIndices()
    assert(correctLetterIndices == expectedCorrect)
    assert(missplacedLetterIndices == expectedMissplaced)
    assert(wrongLetterIndices == expectedWrong)
