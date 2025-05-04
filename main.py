
from config import get_logger, DB_PATH, MODEL_NAME, EMBEDDING_DIM
from fetch_ibge import fetch_noticias_ibge
from embed import load_model, gerar_embeddings
from db import criar_banco, salvar_dados
from metrics import salvar_metricas

logger = get_logger()

def main():
    logger.info("🔍 Buscando notícias do IBGE...")
    texts, metadatas = fetch_noticias_ibge()

    logger.info("📦 Carregando modelo...")
    model = load_model(MODEL_NAME)

    logger.info("🧠 Gerando embeddings...")
    embeddings, metricas = gerar_embeddings(model, texts)

    logger.info("🗃️ Criando banco de dados...")
    db = criar_banco(DB_PATH, EMBEDDING_DIM)

    logger.info("💾 Salvando dados...")
    salvar_dados(db, texts, metadatas, embeddings)

    logger.info("📊 Salvando métricas...")
    salvar_metricas(metricas)

if __name__ == "__main__":
    main()
