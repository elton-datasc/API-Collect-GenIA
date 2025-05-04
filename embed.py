
import time
import psutil
from sentence_transformers import SentenceTransformer

def load_model(model_name):
    return SentenceTransformer(model_name)

def gerar_embeddings(model, texts):
    process = psutil.Process()
    mem_before = process.memory_info().rss / 1024 / 1024
    start = time.time()

    embeddings = model.encode(texts, normalize_embeddings=True)

    duration = time.time() - start
    mem_after = process.memory_info().rss / 1024 / 1024

    mem_used = mem_after - mem_before
    total_kb = len(embeddings) * len(embeddings[0]) * 4 / 1024

    return embeddings, {
        "tempo": round(duration, 2),
        "memoria": round(mem_used, 2),
        "dim_vetor": len(embeddings[0]),
        "tamanho_total_kb": round(total_kb, 2)
    }
