from fuzzywuzzy import fuzz

FRASES = [
    ("hola detecta objeto", 1),
    ("hola detecta emocion", 2),
    ("hola gira derecha", 4),
    ("hola gira izquierda", 3),
    ("hola hora",4),
    ("hola ponte contenta",6),
    ("hola ponte triste",6),
    ("hola ponte enfadada",8),
    ("hola ponte asustada",9),
    ("hola ponte enamorada",13),
    ("hola cuentame chiste",8),
    ("hola gira",11),
    ("hola donde estoy",10),
    ("hola avanza",13),
    ("hola para", -1),
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