# -*- coding: utf-8 -*-
"""
agente.py – Agente com 2 ramificações (responde ou pede mais detalhes)
Agora configurado para usar OpenAI (gpt-4o-mini + text-embedding-3-small),
com variáveis corrigidas para evitar erro de input/context/query.
"""

import asyncio
from pathlib import Path
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import RetrievalQA

# Garante que o event loop exista no Streamlit
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())


def carregar_documentos(folder_path="DADOS"):
    """Carrega todos os PDFs da pasta fornecida e retorna lista de documentos."""
    docs = []
    for n in Path(folder_path).glob("*.pdf"):
        try:
            loader = PyMuPDFLoader(str(n))
            docs.extend(loader.load())
            print(f"Carregado com sucesso arquivo {n.name}")
        except Exception as e:
            print(f"Erro ao carregar arquivo {n.name}: {e}")
    print(f"Total de documentos carregados: {len(docs)}")
    return docs


def carregar_agente(folder_path="DADOS"):
    """Inicializa o agente baseado nos documentos PDF da pasta especificada."""
    docs = carregar_documentos(folder_path)
    if not docs:
        raise ValueError("Nenhum documento PDF encontrado na pasta DADOS/")

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    splits = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vectorstore = FAISS.from_documents(splits, embeddings)
    retriever = vectorstore.as_retriever()

    llm = ChatOpenAI(
        model="gpt-4o-mini",  # rápido e econômico
        temperature=0.0
    )

    # 🔑 Atenção: usamos {query} para alinhar com RetrievalQA
    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "Você é um Assistente de Políticas Internas (RH/IT). "
         "Responda SOMENTE com base no contexto fornecido entre <<< >>>. "
         "Se não houver base suficiente, responda apenas 'Não sei'.\n\nContexto: <<<{context}>>>"),
        ("human", "{query}")
    ])

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={
            "prompt": prompt,
            "document_variable_name": "context"
        },
        input_key="query"   # 👈 chave de entrada oficial
    )
    return chain


def responder_agente(agente, pergunta: str) -> str:
    """Recebe uma pergunta e retorna a resposta do agente."""
    resposta = agente.invoke({"query": pergunta})
    if isinstance(resposta, dict) and "result" in resposta:
        return resposta["result"]
    return str(resposta)
