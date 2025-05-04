
import logging

def get_logger(name="ibge_vec"):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

DB_PATH = "ibge_noticias_local.db"
MODEL_NAME = "all-MiniLM-L6-v2"
EMBEDDING_DIM = 384
