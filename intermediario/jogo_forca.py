
import random

palavras = [
    "python",
    "computador",
    "programacao",
    "dados",
    "tecnologia"
]

palavra = random.choice(palavras)

letras_descobertas = ["_"] * len(palavra)

tentativas = 6

letras_usadas = []

print("===== JOGO DA FORCA =====")

while tentativas > 0:

    print("\nPalavra:")
    print(" ".join(letras_descobertas))

    print(f"\nTentativas restantes: {tentativas}")
    print(f"Letras usadas: {letras_usadas}")

    letra = input("Digite uma letra: ").lower()

    if letra in letras_usadas:
        print("Você já tentou essa letra.")
        continue

    letras_usadas.append(letra)

    if letra in palavra:

        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_descobertas[i] = letra

        print("\nLetra correta!")

    else:
        tentativas -= 1
        print("\nLetra incorreta!")

    if "_" not in letras_descobertas:
        print("\nParabéns! Você venceu!")
        print(f"A palavra era: {palavra}")
        break

else:
    print("\nVocê perdeu!")
    print(f"A palavra era: {palavra}")
