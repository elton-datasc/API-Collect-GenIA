
# IBGE Vector Search + RAG 🧠

Este projeto demonstra um pipeline completo de indexação vetorial de notícias do IBGE e resposta a perguntas usando RAG (Retrieval-Augmented Generation) com um modelo open-source de linguagem.

---

## 📦 Instalação

1. Clone ou extraia o repositório:

```
unzip ibge_vec_project.zip
cd ibge_vec
```

2. Instale as dependências (idealmente em um ambiente virtual):

```
pip install -r requirements.txt
```

---

## ⚙️ Estrutura do Projeto

```
ibge_vec/
├── config.py            # Configurações globais e logger
├── db.py                # Criação do banco vetorial com SQLite + sqlite-vec
├── embed.py             # Geração de embeddings com SentenceTransformer
├── fetch_ibge.py        # Coleta e chunking das notícias da API do IBGE
├── llm.py               # Carregamento do modelo de linguagem (ex: Mistral)
├── metrics.py           # Registro de métricas de uso e embeddings
├── rag.py               # Pipeline de RAG: recuperação + geração
├── search.py            # Busca vetorial simples
├── main.py              # Pipeline de ingestão e indexação
├── run_rag.py           # Executa uma pergunta via RAG
└── requirements.txt     # Dependências do projeto
```

---

## 🚀 Como Usar

### 1. Indexar as notícias (com embeddings)
```
python main.py
```

Isso irá:
- Buscar as últimas 5 notícias do IBGE sobre "inflação"
- Gerar embeddings com `all-MiniLM-L6-v2`
- Criar um banco `ibge_noticias_local.db`
- Registrar métricas em `metricas.csv`

### 2. Fazer perguntas com RAG (modelo local)
```
python run_rag.py
```

Você poderá digitar perguntas como:
- `Qual foi o impacto da inflação nos alimentos?`
- `O que o IBGE divulgou recentemente sobre preços?`

---

## 🧪 Métricas

As métricas de uso são salvas em `metricas.csv`, incluindo:
- Tempo de geração de embeddings
- Memória utilizada
- Tamanho dos vetores

---

## 🧠 Modelos Suportados

O código usa o modelo `all-MiniLM-L6-v2` para embeddings e está preparado para usar o LLM `mistralai/Mistral-7B-Instruct-v0.1` (ou outro via Transformers) para RAG.

Se não quiser usar um modelo pesado, você pode ajustar o `load_llm()` em `llm.py` para carregar outro mais leve como `tiiuae/falcon-rw-1b`.

---

## ✅ Requisitos

- Python 3.9+
- `sqlite-vec` instalado (ver `requirements.txt`)
- (Opcional) CUDA se for usar um modelo LLM com GPU

---

## 📄 Licença

MIT - sinta-se à vontade para usar e modificar.

---

Desenvolvido com ❤️ usando [LangChain](https://www.langchain.com), [sqlite-vec](https://github.com/sqlite/sqlite-vec), [HuggingFace Transformers](https://huggingface.co/), e [IBGE API](https://servicodados.ibge.gov.br/api/docs/).


---

## 🐳 Rodando com Docker

### 1. Build da imagem

Na raiz do projeto:

```
docker build -t ibge-rag .
```

### 2. Executar a indexação

```
docker run --rm -v $(pwd):/app ibge-rag python main.py
```

### 3. Fazer perguntas com RAG

```
docker run -it --rm -v $(pwd):/app ibge-rag python run_rag.py
```

### Dockerfile de exemplo (adicione como `Dockerfile` na raiz):

```
FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y gcc && \ 
    pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
```
