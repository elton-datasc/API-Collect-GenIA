
from search import busca_vetorial
from llm import load_llm

def responder_com_rag(db, model, pergunta, top_k=3):
    documentos = busca_vetorial(db, model, pergunta, k=top_k)
    contexto = "\n\n".join([f"{doc[4]}:\n{doc[2]}" for doc in documentos])
    prompt = f"""
Baseado nas informações abaixo, responda à pergunta de forma clara e precisa.

Contexto:
{contexto}

Pergunta: {pergunta}
Resposta:
"""
    llm = load_llm()
    resposta = llm(prompt, max_new_tokens=300, do_sample=False)[0]["generated_text"]
    return resposta[len(prompt):].strip()
