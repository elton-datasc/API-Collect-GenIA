
from .embed import serialize

def busca_vetorial(db, model, query, k=3):
    query_vector = model.encode([query], normalize_embeddings=True)[0]
    results = db.execute("""
        SELECT noticias.id, distance, texto, link, titulo
        FROM vec_noticias
        LEFT JOIN noticias ON noticias.id = vec_noticias.id
        WHERE embedding MATCH ?
        AND k = ?
        ORDER BY distance
    """, [serialize(query_vector), k]).fetchall()
    return results
