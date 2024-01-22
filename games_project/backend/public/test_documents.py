from import_text import WordOfTheDay
import pytest

@pytest.mark.parametrize("document, expectedtext",[('./test_doc.txt', ["hola", "prueba", "número", "uno"]),
                                                   #('./test_doc.txt', ["hola", "prueba", "uno"]),
                                                   ('./test_doc2.txt',["este", "lector", "de", "archivos", "funciona"])])
def test_document(document, expectedtext):
    test_file = WordOfTheDay(document)
    assert(test_file.fileDictionary() == expectedtext)
    #assert(test_file.randomWordWithoutAccent() in expectedtext)
    assert(test_file.fileDictionary() == expectedtext)
