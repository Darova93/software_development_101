import pytest
from import_text import WordOfTheDay
from unittest import mock

@pytest.mark.parametrize("document, expectedText", [('./test_doc.txt', ["HOLA", "PRUEBA", "NÚMERO", "UNO"]),
                                                    ('./test_doc2.txt',["ESTE", "LECTOR", "DE", "ARCHIVOS", "FUNCIONA"])])
def test_document(document, expectedText):
    testFile = WordOfTheDay(document)
    assert(testFile.fileDictionary() == expectedText)
    assert(testFile.fileDictionary() == expectedText)
    

@pytest.mark.parametrize("document, mockValue, expectedText", [('./test_doc.txt', ["PRUEBA"], ["PRUEBA"]),
                                                               ('./test_doc.txt', ["HOLA"], ["HOLA"]),
                                                               ('./test_doc.txt', ["UNO"], ["UNO"]),
                                                               ('./palabras_rae.txt', ["ACASO"], ["ACASO"])])
@mock.patch("import_text.choice", autospec=True)
def test_randomWord(mockTest, mockValue, document, expectedText):
    testFile = WordOfTheDay(document)
    for _ in range(4):
        mockTest.return_value = mockValue
        assert(testFile.randomWord() == expectedText)
