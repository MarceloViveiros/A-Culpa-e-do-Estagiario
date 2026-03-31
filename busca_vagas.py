import requests
import json #1 biblioteca pra dar jeito nos arquivos JSON
import time # Ferramenta para dar uns respiros pro robozin
import os #Biblioteca para ler o sistema operacional
from dotenv import load_dotenv #biblioteca para ler o .env


#Carrega as variáveis escondidas no arquivo .env
load_dotenv()
# Pegamos o token
meu_token = os.getenv('GITHUB_TOKEN')

# 2.Cria o cabeçalho de autenticação
headers = {
    'Authorization': f'Bearer {meu_token}',
    'Accept': 'application/vnd.github.v3+json'
}

#Escalabilidade: Lista de URLS
repositorios = [
    'backend-br/vagas',
    'frontendbr/vagas',
    'react-brasil/vagas',
    'androiddevbr/vagas',
    'CocoaHeadsBrasil/vagas',
    'qa-brasil/vagas',
    'vuejs-br/vagas',
    'brasil-php/vagas',
    'pydevbr/vagas',
    'kotlin-br/vagas',
    'remotejobsbr/design-ux-vagas',
    'remotejobsbr/trabalho-remoto-vagas',
]

vagas_filtradas = [] #Bau onde guardar as vagas

print("Ligando a turbina de busca...\n")
print("-" * 40)#linhas fofas

#Lista de palavras chave
palavras_chave = ['estagio', 'estagiario', 'trainee', 'junior']

# Pedi pro Python juntar essas palavras com o '+OR+'
# O resultado disso vai ser: "estágio+OR+estagio..."cls
query_palavras = '+OR+'.join(palavras_chave)

#Loop: para cada repositório da lista execute o seguinte:
for repo in repositorios:
    print(f"Vasculhando o repositório: {repo}")

    #A API vai busccar de acordo com nossa URL montada no query
    url_busca = f"https://api.github.com/search/issues?q={query_palavras}+repo:{repo}+state:open"

    #Manda pro mensageiro
    resposta = requests.get(url_busca, headers=headers)

    if resposta.status_code == 200: #deu bom
        dados = resposta.json()

        #A API já diz quantos resultados achou antes de listar
        total_encontrado = dados.get('total_count', 0)
        print(f"Encontramos {total_encontrado} vagas aqui!")

        #As vagas em si ficam guardadas dentro de uma lista chamada 'items'
        lista_de_vagas = dados.get('items', [])

        #Le cada vaga encontrada e guarda no bau

        for vaga in lista_de_vagas:
            vagas_filtradas.append({
                'titulo': vaga['title'],
                'link': vaga['html_url'],
                'repositorio': repo #guarda de onde a vaga veio
            })
    
    else:
        print(f"Ops! Deu erro no {repo}. Código: {resposta.status_code}")
        print(resposta.json())

        #Rate limit, colocar o robozin pra descansar por 3 segundos pra não dar ruim nas solicitações
    time.sleep(3)
print("-" * 40 )#linha fofa
print(f"Resumo Final: Coletei um total de {len(vagas_filtradas)} vagas de estágio!")

#Salvando no banco de dados
with open('vagas.json', 'w', encoding='utf-8') as arquivo:
    json.dump(vagas_filtradas, arquivo, ensure_ascii=False, indent=4)
    print("Arquivo 'vagas.json' atualizado com sucesso e cheio de vagas!")



