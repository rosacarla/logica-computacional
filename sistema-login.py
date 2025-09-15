# 🔐 Sistema de Login com tempo e tentativas
import time

senha_correta = "1234"
tentativas_restantes = 3
tempo_limite = 30  # segundos
inicio = time.time()
acesso_concedido = False

print("🔐 Bem-vindo! Você tem 3 tentativas e 30 segundos para digitar a senha correta.")

while tentativas_restantes > 0 and (time.time() - inicio) < tempo_limite:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("✅ Acesso concedido!")
        acesso_concedido = True
        break
    else:
        tentativas_restantes -= 1
        print(f"❌ Senha incorreta. Tentativas restantes: {tentativas_restantes}")

# Verifica motivo do encerramento
tempo_total = time.time() - inicio

if not acesso_concedido:
    if tentativas_restantes == 0:
        print("💀 Acesso negado: número de tentativas esgotado.")
    elif tempo_total >= tempo_limite:
        print("⏰ Acesso negado: tempo expirado.")
