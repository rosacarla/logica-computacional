# 🎯 Jogo da Forca com desenho do boneco
palavra = "tecnologia"
letras_descobertas = ["_"] * len(palavra)
tentativas = 6
letras_usadas = []

def mostrar_boneco(t):
    bonecos = [
        """
         _______
        |       |
        |       😵
        |      /|\\
        |      / \\
        |
        """,
        """
         _______
        |       |
        |       😟
        |      /|\\
        |      / 
        |
        """,
        """
         _______
        |       |
        |       😐
        |      /|\\
        |      
        |
        """,
        """
         _______
        |       |
        |       😕
        |      /|
        |      
        |
        """,
        """
         _______
        |       |
        |       🙂
        |       |
        |      
        |
        """,
        """
         _______
        |       |
        |       😀
        |       
        |      
        |
        """
    ]
    print(bonecos[6 - t])

print("🎯 Jogo da Forca! Adivinhe a palavra letra por letra.")

while tentativas > 0:
    print("\nPalavra:", " ".join(letras_descobertas))
    mostrar_boneco(tentativas)
    letra = input("Digite uma letra (ou 'sair' para desistir): ").lower()

    if letra == "sair":
        print("Você desistiu do jogo.")
        break

    if not letra.isalpha() or len(letra) != 1:
        print("Entrada inválida. Digite apenas uma letra.")
        continue

    if letra in letras_usadas:
        print("Você já tentou essa letra.")
        pass
    else:
        letras_usadas.append(letra)

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_descobertas[i] = letra
        print("✅ Boa! Letra correta.")
    else:
        tentativas -= 1
        print("❌ Letra errada. Tentativas restantes:", tentativas)

    if "_" not in letras_descobertas:
        print("\n🏆 Parabéns! Você descobriu a palavra:", palavra)
        break

if tentativas == 0:
    mostrar_boneco(tentativas)
    print("\n💀 Fim de jogo! A palavra era:", palavra)
