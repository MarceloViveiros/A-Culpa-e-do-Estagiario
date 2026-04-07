import cloudscraper
from bs4 import BeautifulSoup
import time
<<<<<<< HEAD:scripts/busca_programathor.py
import json #  ferramenta para lidar com obanco de dados
=======
import json #  Nova ferramenta para lidar com o banco de dados
>>>>>>> ab2db62e27d662248430ac57a1f1bc701a436fba:busca_programathor.py
import os   #  Ferramenta para checar se o arquivo json já existe

dominio_base = 'https://programathor.com.br'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

palavras_chave = ['estagio', 'estagiario', 'trainee', 'junior']

print("Iniciando a varredura profunda no Programathor...\n")

<<<<<<< HEAD:scripts/busca_programathor.py
# A lista vazia para guardar as vagas
=======
# guardar as vagas dessa caçada
>>>>>>> ab2db62e27d662248430ac57a1f1bc701a436fba:busca_programathor.py
vagas_programathor = []

scraper = cloudscraper.create_scraper()

for pagina in range(1, 6):
    url = f"https://programathor.com.br/jobs/page/{pagina}"
    print(f"📄 Vasculhando a página {pagina}...")
    
    resposta = scraper.get(url, headers=headers)
    
    if resposta.status_code == 200:
        sopa = BeautifulSoup(resposta.text, 'html.parser')
        caixas_vagas = sopa.find_all('div', class_='cell-list')
        
        for caixa in caixas_vagas:
            tag_link = caixa.find('a')
            tag_titulo = caixa.find('h3', class_='text-24')
            
            if tag_link and tag_titulo:
                titulo_original = tag_titulo.text.strip().replace('NOVA', '').strip()
                titulo_minusculo = titulo_original.lower()
                
                if 'vencida' in titulo_minusculo:
                    continue 
                    
                if any(palavra in titulo_minusculo for palavra in palavras_chave):
                    link_completo = dominio_base + tag_link['href']
                    
                    print(f"  ✅ ENCONTRADA: {titulo_original}")
                    
                    # Em vez de só imprimir o link, guarda no formato exato que o site espera!
                    vagas_programathor.append({
                        "titulo": titulo_original,
                        "repositorio": "Programathor", # Usa a chave 'repositorio' para manter o padrão do Front-end
                        "link": link_completo
                    })
        
        time.sleep(1)
        
    else:
        print(f"Fomos bloqueados na página {pagina}. Código: {resposta.status_code}")
        break 

print(f"\nVarredura concluída! Pescamos {len(vagas_programathor)} vagas.")

# ==========================================
# A UNIFICAÇÃO DOS DADOS
# ==========================================
print("\n Unindo os dados com as vagas do GitHub...")

todas_as_vagas = []

# Passo 1: O arquivo vagas.json já existe? Se sim, le o que tem dentro dele
<<<<<<< HEAD:scripts/busca_programathor.py
if os.path.exists('../vagas.json'):
    with open('../vagas.json', 'r', encoding='utf-8') as arquivo:
=======
if os.path.exists('vagas.json'):
    with open('vagas.json', 'r', encoding='utf-8') as arquivo:
>>>>>>> ab2db62e27d662248430ac57a1f1bc701a436fba:busca_programathor.py
        todas_as_vagas = json.load(arquivo)

# Passo 2: Junta as vagas velhas (GitHub) com as vagas novas (Programathor)
todas_as_vagas.extend(vagas_programathor)

# Passo 3: Salva tudo de volta no mesmo arquivo
with open('../vagas.json', 'w', encoding='utf-8') as arquivo:
    json.dump(todas_as_vagas, arquivo, indent=4, ensure_ascii=False)

print("Unificação concluída com sucesso! O vagas.json foi atualizado.")
