# Projeto de raspagem de dados com BigQuery

Este projeto visa coletar notícias do site da Globo, armazená-las no BigQuery e utiliza um script Python para consumir a API do BigQuery para acessar o banco de dados e pesquisar artigos com base em palavras-chave.
## Conteudo da pasta
```app.py``` Arquivo principal, responsável por acessar a API do BigQuery e fazer pesquisas utilizando palavras-chave. <br>
```functions.py``` Arquivo utilizado para armazenar as principais funções utilizadas no projeto. <br>
```gcp_auth.py``` Arquivo utilizado para armazenas as credencias da Google Cloud Platform. <br>
```scrapy_news.ipynb``` Notebook utilizado para fazer as Raspagem de dados. <br>

## Ferramentas e Tecnologias:
* Python 3.10.4
* Pandas
* Pandas-gbq
* BeautifoulSoup
* Request
* BigQuery
* Google Cloud Platform (GCP)
  
## Instalação

Para instalar o projeto, siga estas etapas:

1. Clone o repositório do GitHub:
```
git clone https://github.com/caiomassuia/project-scrapy-news.git
```
2. Instale os requisitos:
```
pip install -r requirements.txt
```

## Execução

Para executar o projeto, execute os seguintes comando: <br>
1. Para acessar o banco de dados e fazer pesquisas utilizando palavras chaves: <br>
⚠ ATENCAO: somente palavras chaves encontradas no Titulo ou no Subtitulo
   * Executa o script ```python app.py``` <br>
2. Coletar novos dados por raspagem: <br>
   * Executa o notebook ```scrapy_news.ipynb``` <br>
