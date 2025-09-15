# 🎮 Jogo da Velha para dois jogadores

def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tabuleiro(tabuleiro):
    print("\nTabuleiro:")
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    # Verifica linhas e colunas
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or \
           all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True
    # Verifica diagonais
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or \
       all([tabuleiro[i][2 - i] == jogador for i in range(3)]):
        return True
    return False

def verificar_empate(tabuleiro):
    return all([celula != " " for linha in tabuleiro for celula in linha])

def jogo_da_velha():
    tabuleiro = criar_tabuleiro()
    jogador_atual = "X"

    print("🎯 Bem-vindo ao Jogo da Velha!")
    mostrar_tabuleiro(tabuleiro)

    while True:
        try:
            linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0, 1 ou 2): "))
            coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1 ou 2): "))
        except ValueError:
            print("❌ Entrada inválida. Digite números inteiros.")
            continue

        if linha not in range(3) or coluna not in range(3):
            print("❌ Posição fora do tabuleiro.")
            continue

        if tabuleiro[linha][coluna] != " ":
            print("❌ Posição já ocupada. Tente outra.")
            continue

        tabuleiro[linha][coluna] = jogador_atual
        mostrar_tabuleiro(tabuleiro)

        if verificar_vitoria(tabuleiro, jogador_atual):
            print(f"🏆 Jogador {jogador_atual} venceu!")
            break

        if verificar_empate(tabuleiro):
            print("🤝 Empate! Ninguém venceu.")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

jogo_da_velha()
