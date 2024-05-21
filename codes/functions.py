import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def content_title(page):
    """
    Função para extrair o título de um elemento da página da web identificado pela classe "content-head__title".

    Argumentos:
        page (objeto BeautifulSoup): O conteúdo HTML analisado da notícia.

    Retorna:
        str: O título extraído da notícia se encontrado, caso contrário "título não encontrado".
    """
    
    title = page.find("h1", class_="content-head__title")
    if title is not None:
        return title.get_text().lower()
    return "título não encontrado"
#------------------------------------------------------------------------------------------------------------------------------------------
def content_subtitle(page):
    """
    Função para extrair o subtítulo de um elemento da página da web identificado pela classe "content-head__subtitle".

    Argumentos:
        page (objeto BeautifulSoup): O conteúdo HTML analisado da notícia.

    Retorna:
        str: O subtítulo extraído da notícia se encontrado, caso contrário "subtítulo não encontrado".
    """
    subtitle = page.find("h2", class_="content-head__subtitle")
    if subtitle is not None:
        return subtitle.get_text().lower()
    return "subtítulo não encontrado"
#------------------------------------------------------------------------------------------------------------------------------------------
def content_text(page):
    """
    Extrai e limpa o conteúdo textual com a funcao `remove_text` de um elemento da página da web identificado pela classe "content-text__container".

    Argumentos:
        page (objeto BeautifulSoup): Um objeto BeautifulSoup que representa o conteúdo HTML analisado da página da web.

    Retorna:
        str: O conteúdo textual extraído e limpo, ou "texto não encontrado" se nenhum elemento correspondente for encontrado.
    """
    text = page.find_all('p', class_="content-text__container")
    if text is not None:
        text = " ".join([t.get_text().lower() for t in text])
        clean_text = remove_text(text)
        return clean_text
    return "texto não encontrado"
#------------------------------------------------------------------------------------------------------------------------------------------
def content_author(page):
    """
    Função para extrair o nome do autor de uma notícia a partir do conteúdo HTML fornecido (page).

    Tenta encontrar o nome do autor usando diferentes abordagens, pois a estrutura HTML pode variar entre sites.

    Argumentos:
        page (objeto BeautifulSoup): O conteúdo HTML analisado da notícia.

    Retorna:
        str: O nome do autor extraído da notícia se encontrado, caso contrário "autor não encontrado".
    """

    author = page.find("span", class_="content-publication-data__from")
    if author is not None:
        return author.get_text().lower()
    author = page.find("a", class_="multi_signatures")
    if author is not None:
        return author.get_text().lower()
    author = page.find("span", itemprop="name")
    if author is not None:
        return author.get_text().lower()
    author = page.find("p", class_="content-publication-data__from")
    if author is not None:
        return author.get("title").lower()
    return "autor não encontrado"
#------------------------------------------------------------------------------------------------------------------------------------------
def content_date(page):
    """
    Função para extrair a data de publicação de um elemento da página da web identificado pelo itemprop "datePublished".

    Argumentos:
        page (objeto BeautifulSoup): O conteúdo HTML analisado da notícia.

    Retorna:
        str: A data de publicação extraída da notícia se encontrada, caso contrário "data não encontrada".
    """
    date = page.find("time", itemprop="datePublished")
    if date is not None:
        return date.get_text()
    return "data não encontrada"
#------------------------------------------------------------------------------------------------------------------------------------------
def df_news_data(lista_urls):
    """
    Coleta dados de notícias a partir de uma lista de URLs e retorna um DataFrame.

    Parâmetros:
        news_url_list (lista): Lista de URLs de notícias.

    Retorno:
        DataFrame: DataFrame contendo os dados coletados das notícias.
    """
    print("Inicio da raspagem de dados")
    list_url = []
    list_date = []
    list_author = []
    list_title = []  
    list_subtitle = []
    list_text = []

    for url in lista_urls:
        try:
            response = requests.get(url)
            page = BeautifulSoup(response.text, "html.parser")

            list_url.append(url)
            list_date.append(content_date(page))
            list_author.append(content_author(page))
            list_title.append(content_title(page))
            list_subtitle.append(content_subtitle(page))
            list_text.append(content_text(page))

        except Exception as e:
            print(f"Erro ao fazer scraping da URL {url}: {e}")

    print("Coleta finalizada")      
    return pd.DataFrame({"url": list_url, "date": list_date, "author": list_author, "title": list_title, "subtitle": list_subtitle, "text": list_text})
#------------------------------------------------------------------------------------------------------------------------------------------
def remove_text(text):
    """
    Função para remover textos indesejados do conteúdo da notícia

    Argumentos:
        text (str): O texto da notícia a ser processado.

    Retorna:
        str: O texto da notícia após a remoção dos textos indesejados.
    """
    
    parts_to_remove = [
    r"✅ siga o canal do g1 pr no whatsapp",
    r"✅ siga o canal do g1 pr no telegram",
    r"vídeos mais assistidos do g1 pr:",
    r"leia mais notícias em g1 paraná.",
    r"vídeos mais assistidos do g1 pr:",
    r"leia mais:",
    r"leia mais notícias em g1 paraná.",
    r"🔎aplicativo de inteligência artificial para foto: veja 9 opções",
    r"📲canal do techtudo no whatsapp: acompanhe as principais notícias, tutoriais e reviews",
    r"📝 Quais os melhores chatbots para conversar com inteligência artificial?",
    r"veja no fórum do techtudo",
    r"veja também: google gemini: veja protótipo de ia que sabe e lembra de tudo",
    r"📝como liberar espaço no celular android? usuários respondem no fórum techtudo.",
    r"mais do techtudo",
    r"📲 acesse o canal do g1 rs no whatsapp",
    r"✅ clique aqui para se inscrever no canal do g1 sp no whatsapp",
    r"📲 participe do canal do g1 sul de minas no whatsapp",
    r"📲 canal do techtudo no whatsapp: acompanhe as principais notícias, tutoriais e reviews",
    r"✅ clique aqui para seguir o canal de notícias internacionais do g1 no whatsapp",
    r"✅clique e siga o canal do g1 go no whatsapp",
    r"✅ clique aqui e participe do canal do gshow no whatsapp",
    r"🎧 ouça o podcast ge corinthians🎧",
    r"🔔 canal do techtudo no whatsapp: acompanhe as principais notícias, tutoriais e reviews",
    r""

]
    for part in parts_to_remove:
        text = re.sub(part, "", text)
    return text