import os
import json
import requests

print("📢 Iniciando o Estagiário Mensageiro...")

# 1. Puxamos as chaves do cofre do GitHub Actions
token = os.getenv('TELEGRAM_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')

# 2. Lemos o nosso banco de dados atualizado
total_vagas = 0
if os.path.exists('vagas.json'):
    with open('vagas.json', 'r', encoding='utf-8') as arquivo:
        vagas = json.load(arquivo)
        total_vagas = len(vagas)

# 3. Montamos a mensagem de resumo
# Troque o link abaixo pelo link real do seu GitHub Pages!
link_do_site = "https://SEU_USUARIO.github.io/A-Culpa-e-do-Estagiario/"

mensagem = (
    f"🤖 O Estagiário Automático terminou a varredura!*\n\n"
    f"Hoje temos *{total_vagas} vagas* de Estágio e Júnior fresquinhas esperando por você na vitrine.\n\n"
    f"👉 Confira todas aqui: {link_do_site}"
)

# 4. Disparamos o alerta para o Telegram
if token and chat_id and total_vagas > 0:
    url_api = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id, 
        "text": mensagem, 
        "parse_mode": "Markdown"
    }
    
    resposta = requests.post(url_api, data=payload)
    
    if resposta.status_code == 200:
        print("✅ Alerta enviado com sucesso para o Telegram!")
    else:
        print(f"🚨 Erro ao enviar alerta: {resposta.text}")
else:
    print("⚠️ Faltam as chaves do Telegram no cofre ou não há vagas para notificar.")