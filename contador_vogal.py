def contar_vogais(frase):
    vogais = 'aeiouAEIOU'
    contagem = 0
    for char in frase:
        if char in vogais:
            contagem += 1
    return contagem

frase = input("Digite uma frase: ")
print("Número de vogais na frase:", contar_vogais(frase))
