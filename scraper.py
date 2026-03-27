import requests
import json #1 biblioteca pra dar jeito nos arquivos JSON

url_api = 'https://api.github.com/repos/backend-br/vagas/issues'
print(f"Acessando o GitHub: {url_api} ...")

resposta = requests.get(url_api)

if resposta.status_code == 200:
    lista_de_vagas = resposta.json()
    print(f"Sucesso! o GitHub entregou {len(lista_de_vagas)} vagas brutas. \n")

    #O FILTRO
    vagas_filtradas = [] #lista vazia pra guardar vagas que eu procuro
    palavras_chave = ['estágio', 'estagio', 'estagiário', 'estagiario']

    for vaga in lista_de_vagas:
        #vamos pegar o titulo minúsculo e o link
        titulo = vaga['title'].lower()
        url_vaga = vaga['html_url']

        #Tem alguma das palavras chaves no titulo?
        eh_estagio = any(palavra in titulo for palavra in palavras_chave)

        #Se for estagio guarda o titulo e o link
        if eh_estagio:
            vagas_filtradas.append({
                'titulo': vaga['title'],
                'link': url_vaga
            })

    #O RELATATÓRIO
    print("-" * 40)#linha fofa
    print(f"Vagas de Estágio que passaram no filtro: {len(vagas_filtradas)}")
    for v in vagas_filtradas:
        print(f"{v['titulo']}")
        print(f"{v['link']}\n")
    print("-" * 40)#linha fofa

    #ARMAZENAMENTO
    #Vamos criar um arquivo 'vagas.json' e jogamos nossa lista filtrada nele
    with open('vagas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(vagas_filtradas, arquivo,ensure_ascii=False, indent=4)
        print("Arquivo 'vagas.json' atualizado com sucesso!")
        
else:
    print(f"Ops! A API bloqueou o acesso. Erro Código: {resposta.status_code}")