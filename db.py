
import sqlite3
import sqlite_vec
import struct

def serialize(vector):
    return struct.pack("%sf" % len(vector), *vector)

def criar_banco(db_path, dim):
    db = sqlite3.connect(db_path)
    db.enable_load_extension(True)
    sqlite_vec.load(db)
    db.enable_load_extension(False)

    db.execute("DROP TABLE IF EXISTS noticias;")
    db.execute("DROP TABLE IF EXISTS vec_noticias;")

    db.execute("""
        CREATE TABLE noticias(
            id INTEGER PRIMARY KEY,
            texto TEXT,
            id_noticia TEXT,
            data_publicacao TEXT,
            link TEXT,
            titulo TEXT
        );
    """)

    db.execute(f"""
        CREATE VIRTUAL TABLE vec_noticias USING vec0(
            id INTEGER PRIMARY KEY,
            embedding FLOAT[{dim}]
        );
    """)

    return db

def salvar_dados(db, texts, metadatas, embeddings):
    with db:
        for i, (texto, meta) in enumerate(zip(texts, metadatas)):
            db.execute(
                "INSERT INTO noticias(id, texto, id_noticia, data_publicacao, link, titulo) VALUES (?, ?, ?, ?, ?, ?)",
                (i, texto, meta["id_noticia"], meta["data_publicacao"], meta["link"], meta["titulo"])
            )
            db.execute(
                "INSERT INTO vec_noticias(id, embedding) VALUES (?, ?)",
                (i, serialize(embeddings[i]))
            )
