with open('palabras_rae.txt', 'r', newline="\r\n", encoding="utf-8") as words:
    def read(words):
        words_rae = []
        for word in words:
            words_rae.append(word.replace("\r\n", ""))
        return words_rae
