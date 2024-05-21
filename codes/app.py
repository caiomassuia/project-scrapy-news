from google.cloud import bigquery
from gcp_auth import credentials

def query_news():
    client = bigquery.Client(credentials=credentials)
    while True:
        user_input = input("\nDigite a palavra chave: ")
        try:
            query_job = client.query(
                """
                SELECT
                    url,
                    author,
                    date,
                    title,
                    subtitle,
                    text
                FROM `project-scrapy-news.bigquery_news.tb_news_data`
                WHERE
                    title LIKE '%""" + user_input + """%' OR
                    subtitle LIKE '%""" + user_input + """%'
                """
            )

            results = query_job.result()
            
            num_noticia = 0
            if results.total_rows == 0:
                print("\nNenhuma noticia encontrada com a palavra chave digitada.")
            print(f'\n{results.total_rows} Noticias encontradas:')
            for row in results:
                num_noticia += 1
                print(
                    f"{'-' * 180}\n" 
                    f"Noticia {num_noticia}:\n\n"
                    f"url: {row.url}\n\n"
                    f"author: {row.author}\n\n"
                    f"date: {row.date}\n\n"
                    f"title: {row.title}\n\n"
                    f"subtitle: {row.subtitle}\n\n"
                    f"text: {row.text}\n"
                    )
            print(f"{'-' * 180}\n")
            contiuar = input("\nDeseja continuar? Digite S/N:")
            if contiuar.upper() == "N":
                break
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    query_news()
