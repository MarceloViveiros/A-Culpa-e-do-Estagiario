import os
import json
import requests
import html

print("📢 Iniciando o Estagiário Mensageiro...")

# Puxa as chaves do cofre do GitHub Actions
token = os.getenv('TELEGRAM_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')

# Le o banco de dados atualizado
total_vagas = 0
if os.path.exists('../vagas.json'):
    with open('../vagas.json', 'r', encoding='utf-8') as arquivo:
        vagas = json.load(arquivo)
        total_vagas = len(vagas)

# Monta a mensagem de resumo
link_do_site = "https://MarceloViveiros.github.io/A-Culpa-e-do-Estagiario/"

# O html.escape protege o link caso ele tenha caracteres especiais
link_seguro = html.escape(link_do_site)

mensagem = (
    f"🤖 <b>O Estagiário terminou a varredura!</b>\n\n"
    f"Hoje temos <b>{total_vagas} vagas</b> esperando por você.\n\n"
    f"👉 Confira todas aqui: {link_seguro}"
)

# Dispara o alerta para o Telegram
if token and chat_id and total_vagas > 0:
    url_api = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id, 
        "text": mensagem, 
        "parse_mode": "HTML"
    }
    
    resposta = requests.post(url_api, data=payload)
    
    if resposta.status_code == 200:
        print("✅ Alerta enviado com sucesso para o Telegram!")
    else:
        print(f"🚨 Erro ao enviar alerta: {resposta.text}")
else:
    print("⚠️ Faltam as chaves do Telegram no cofre ou não há vagas para notificar.")