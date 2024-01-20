import pytest
from wordle import Wordle
@pytest.mark.parametrize("guess, wordOfTheDay, expectedCorrect, expectedMissplaced, expectedWrong", 
                         [('avara', 'maria', [4], [0,3], [1,2]),
                          ('Burro','perro', [2,3,4], [], [0,1]),
                          ('HoYoS','huelo', [0], [1], [2,3,4])])

def test_answer(guess, wordOfTheDay, expectedCorrect, expectedMissplaced, expectedWrong):
    obj = Wordle(guess, wordOfTheDay)
    correctLetterIndices, missplacedLetterIndices, wrongLetterIndices = obj.testPlayersGuess()
    assert(correctLetterIndices == expectedCorrect)
    assert(missplacedLetterIndices == expectedMissplaced)
    assert(wrongLetterIndices == expectedWrong)
