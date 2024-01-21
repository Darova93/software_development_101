import pytest
from wordle import WordleAttempt
@pytest.mark.parametrize("guess, answer, expectedCorrect, expectedMissplaced, expectedWrong", 
                         [('avara', 'maria', [4], [0,3], [1,2]),
                          ('Burro', 'perro', [2,3,4], [], [0,1]),
                          ('HoYoS', 'huelo', [0], [1], [2,3,4]),
                          ('juego', 'juego', [0,1,2,3,4], [], [])])

def test_answer(guess, answer, expectedCorrect, expectedMissplaced, expectedWrong):
    attempt = WordleAttempt(guess, answer)
    #attempt.testPlayersGuess()
    assert(attempt.correctLetterIndices == expectedCorrect)
    assert(attempt.missplacedLetterIndices == expectedMissplaced)
    assert(attempt.wrongLetterIndices == expectedWrong)
