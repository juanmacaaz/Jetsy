from fuzzywuzzy import fuzz

FRASES = [
    # Desencadenante
    ("hola detecta objeto", 1),
    ("hola detecta emocion", 2),
    ("hola repite", 3),
    ("hola tel me a joke", 4),
    ("hola donde estoy", 5),

    # Repite conmigo

    ("derecha", 20),
    ("izquierda", 21),
    ("adelante", 22),
    ("atras", 23),
    ("brazo izquierdo arriba", 24),
    ("brazo derecho arriba", 25),
    ("brazo izquierdo abajo", 26),
    ("brazo derecho abajo", 27),
    ("Terminamos", -4)
]

def get_all_words(frases):
    
    unique_words = set()
    for frase in frases:
        for word in frase[0].split():
            unique_words.add(word)
    return list(unique_words)

PALABRAS = get_all_words(FRASES)

def etiqueta_frase(frase, threshold = 70):
    lista_final = []
    for palabra in frase.split():
        resultados = [(x, fuzz.ratio(palabra, x)) for x in PALABRAS]
        max_ratio = max(resultados, key=lambda x: x[1])
        lista_final.append(max_ratio)
    resultados = [x[0] for x in lista_final if x[1] > threshold]
    if resultados == []:
        return 0
    print(resultados)
    for frase, id in FRASES:
        if all(x in resultados for x in frase.split()): return id
    return 0