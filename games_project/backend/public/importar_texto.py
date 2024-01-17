with open('palabras_rae.txt', 'r', newline="\r\n", encoding="utf-8") as palabras:
    def leer(palabras):
        palabras_rae = []
        for palabra in palabras:
            palabras_rae.append(palabra.replace("\r\n", ""))
        return palabras_rae
