meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "POKEO": "Hacer pequeñas cantidades de daño mientras el enemigo hace algo mas",
            "FARMEO": "Obtener dinero o experiencia",
            "KITEO": "Moverse mientras haces daño"}


for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("la palabra no se encontro")
