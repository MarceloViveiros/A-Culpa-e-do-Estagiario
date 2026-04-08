import cloudscraper
from bs4 import BeautifulSoup
import time
import json
import os

dominio_base = 'https://www.vagas.com.br'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

palavras_chave = ['estágio', 'estagio', 'estagiário', 'estagiario', 'trainee', 'júnior', 'junior']

print("🕵️‍♂️ Iniciando a varredura no Vagas.com.br...\n")

vagas_encontradas = []
scraper = cloudscraper.create_scraper()

# varrer as páginas de "Tecnologia", que é a categoria principal deles para TI
for pagina in range(1, 6):
    url = f"https://www.vagas.com.br/vagas-de-tecnologia?pagina={pagina}"
    print(f"📄 Vasculhando a página {pagina}...")
    
    resposta = scraper.get(url, headers=headers)
    
    if resposta.status_code == 200:
        sopa = BeautifulSoup(resposta.text, 'html.parser')
        
        # todos os links que tenham essa classe específica
        links_vagas = sopa.find_all('a', class_='link-detalhes-vaga')
        
        for link_tag in links_vagas:
            # O Vagas.com costuma colocar o título da vaga no atributo 'title' do link
            titulo_original = link_tag.get('title', link_tag.text).strip()
            titulo_minusculo = titulo_original.lower()
            
            # O FILTRO
            if any(palavra in titulo_minusculo for palavra in palavras_chave):
                link_relativo = link_tag.get('href')
                link_completo = dominio_base + link_relativo
                
                print(f"  ✅ ENCONTRADA: {titulo_original}")
                
                vagas_encontradas.append({
                    "titulo": titulo_original,
                    "repositorio": "Vagas.com.br", # Nome da fonte para a vitrine
                    "link": link_completo
                })
                
        time.sleep(3) # pausa ética
        
    else:
        print(f"🚨 Fomos bloqueados ou deu erro na página {pagina}. Código: {resposta.status_code}")
        break 

print(f"\n🎉 Varredura concluída! Pescamos {len(vagas_encontradas)} vagas no Vagas.com.")


# UNIFICAÇÃO DOS DADOS

if vagas_encontradas:
    print("\n💾 Unindo os dados com o nosso banco (vagas.json)...")
    todas_as_vagas = []

    if os.path.exists('vagas.json'):
        with open('vagas.json', 'r', encoding='utf-8') as arquivo:
            todas_as_vagas = json.load(arquivo)

    # Adiciona as vagas do Vagas.com à lista existente
    todas_as_vagas.extend(vagas_encontradas)

    with open('vagas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(todas_as_vagas, arquivo, indent=4, ensure_ascii=False)

    print("Vagas.com.br adicionado com sucesso!")
else:
    print("\n Nenhuma vaga de Estágio/Júnior encontrada nesta rodada.")