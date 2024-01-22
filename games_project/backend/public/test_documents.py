import pytest
from import_text import WordOfTheDay
from unittest import mock

@pytest.mark.parametrize("document, expectedText", [('./test_doc.txt', ["hola", "prueba", "número", "uno"]),
                                                    ('./test_doc2.txt',["este", "lector", "de", "archivos", "funciona"])])
def test_document(document, expectedText):
    testFile = WordOfTheDay(document)
    assert(testFile.fileDictionary() == expectedText)
    assert(testFile.fileDictionary() == expectedText)
    

@pytest.mark.parametrize("document, mockValue, expectedText", [('./test_doc.txt', ["prueba"], ["prueba"]),
                                                               ('./test_doc.txt', ["hola"], ["hola"]),
                                                               ('./test_doc.txt', ["uno"], ["uno"])])
@mock.patch("import_text.choice", autospec=True)
def test_randomWordWithoutAccent(mockTest, mockValue, document, expectedText):
    testFile = WordOfTheDay(document)
    for _ in range(3):
        mockTest.return_value = mockValue
        assert(testFile.randomWordWithoutAccent() == expectedText)
    
