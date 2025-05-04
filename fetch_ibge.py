
import requests
from langchain_text_splitters import RecursiveCharacterTextSplitter

def fetch_noticias_ibge(qtd=5, termo="inflacao"):
    url = f"http://servicodados.ibge.gov.br/api/v3/noticias?busca={termo}&orderBy=data&sort=desc&qtd={qtd}"
    response = requests.get(url)
    response.raise_for_status()
    noticias = response.json()["items"]

    texts = []
    metadatas = []

    for noticia in noticias:
        conteudo = f"{noticia['titulo']}

{noticia['introducao']}"
        metadata = {
            "id_noticia": noticia.get("id"),
            "data_publicacao": noticia.get("data_publicacao"),
            "link": noticia.get("link"),
            "titulo": noticia.get("titulo")
        }
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_text(conteudo)
        for chunk in chunks:
            texts.append(chunk)
            metadatas.append(metadata)
    return texts, metadatas
