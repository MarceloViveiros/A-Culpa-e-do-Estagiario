A Culpa é do Estagiário - Agregador Automatizado de Vagas TI
Sobre o Projeto
O "A Culpa é do Estagiário" é uma plataforma automatizada de agregação de vagas focada em oportunidades para Estagiários e Desenvolvedores Júnior na área de Tecnologia da Informação. O sistema atua como um pipeline de ETL (Extract, Transform, Load), coletando dados de múltiplas fontes, normalizando as informações em um banco de dados central e apresentando os resultados em uma interface web dinâmica.

A aplicação foi desenvolvida para resolver o problema da dispersão de vagas de entrada em diferentes plataformas e a necessidade de verificação constante por parte dos candidatos.

Arquitetura e Fluxo de Dados
O projeto opera em um ecossistema 100% automatizado na nuvem:

Extração (Scraping e API): Scripts em Python rodam rotinas de extração de dados via consumo de API RESTful (GitHub) e Web Scraping em sites de vagas (Programathor).

Transformação e Carga (ETL): Os dados brutos são filtrados, padronizados e consolidados em um arquivo de banco de dados (vagas.json).

Notificação Ativa: Um serviço de mensageria avalia as atualizações do banco de dados e dispara alertas em tempo real via Telegram.

Interface (Frontend): Uma aplicação web consome o arquivo JSON de forma assíncrona, renderizando os cards de vagas com opções de filtro em tempo real.

Automação (CI/CD): Todo o fluxo é orquestrado via GitHub Actions, configurado com Cron Jobs para executar três vezes ao dia sem intervenção humana.

Tecnologias Utilizadas
Backend: Python

Bibliotecas: requests, cloudscraper, BeautifulSoup4

Frontend: HTML5, CSS3, JavaScript (Vanilla, Fetch API)

Banco de Dados: JSON

DevOps / CI-CD: GitHub Actions, Git

Integrações: GitHub Search API, Telegram Bot API

Hospedagem: GitHub Pages

Desafios Técnicos Superados
Durante o desenvolvimento, diversos obstáculos de infraestrutura e regras de negócio foram resolvidos:

Bypass de WAF (Web Application Firewall): Substituição de requisições padrão HTTP pela biblioteca cloudscraper para contornar bloqueios de segurança (Erro 403) aplicados pela Cloudflare contra IPs de Datacenters (Microsoft/GitHub Actions).

Otimização de Consultas em API: Resolução de erros de validação (HTTP 422) na API do GitHub ao atingir o limite de operadores lógicos. A solução envolveu a reestruturação da query e a delegação da normalização de caracteres (acentuação) para o motor de busca interno da API.

Gestão de Conflitos de Versionamento: Resolução de Merge Conflicts gerados pela concorrência entre modificações locais e atualizações autônomas feitas pelo bot de CI/CD no repositório remoto.

Resiliência de Mensageria: Tratamento de erros de formatação de strings (Bad Request) na API do Telegram através da transição do parse_mode de Markdown para HTML puro, garantindo a entrega dos alertas independentemente de caracteres especiais nos links gerados.

Como Executar o Projeto Localmente
Clone o repositório:

git clone https://github.com/SEU_USUARIO/A-Culpa-e-do-Estagiario.git
Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate # No Windows: venv\Scripts\activate
Instale as dependências:

pip install -r requirements.txt
Execute os scripts de extração para gerar o banco de dados local:

python busca_vagas.py
python busca_programathor.py
Abra o arquivo index.html em seu navegador ou utilize a extensão Live Server.

Sobre o Autor
Após uma sólida vivência de 10 anos na área administrativa, decidi realizar uma transição de carreira para a área de Tecnologia da Informação. Atualmente, sou estudante de Análise e Desenvolvimento de Sistemas (ADS) na Estácio. Este projeto reflete minha proatividade na construção de soluções reais baseadas em software e minha capacidade de integrar diferentes tecnologias para resolver problemas do dia a dia da comunidade de desenvolvedores iniciantes.
