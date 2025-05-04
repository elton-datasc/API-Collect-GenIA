
from config import get_logger, DB_PATH, MODEL_NAME
from embed import load_model
import sqlite3
from rag import responder_com_rag

logger = get_logger()

def main():
    logger.info("🔍 Iniciando RAG...")
    db = sqlite3.connect(DB_PATH)
    embed_model = load_model(MODEL_NAME)

    pergunta = input("Digite sua pergunta: ")
    resposta = responder_com_rag(db, embed_model, pergunta)

    print("\n🤖 Resposta do RAG:")
    print(resposta)

if __name__ == "__main__":
    main()
