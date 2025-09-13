import streamlit as st
import os
from agente import carregar_agente, responder_agente

# ----------------------------
# Configuração da página
# ----------------------------
st.set_page_config(page_title="RoBECC Agente", page_icon="🤖")

st.title("🤖 RoBECC Agente")
st.subheader("Assistente de Políticas Internas (RH/IT)")
st.write("Digite sua pergunta abaixo e eu responderei com base nos documentos fornecidos.")

# ----------------------------
# Inicializa o agente (uma vez) e gerencia o estado da sessão
# ----------------------------
if "agente" not in st.session_state:
    try:
        # Tenta carregar o agente da pasta DADOS
        if not os.path.exists("DADOS") or not any(Path("DADOS").glob("*.pdf")):
            st.error("❌ A pasta 'DADOS' não foi encontrada ou está vazia. Por favor, adicione os arquivos PDF.")
            st.stop()
        
        st.session_state["agente"] = carregar_agente("DADOS")
        st.success("✅ Agente inicializado com sucesso! PDFs carregados.")
        
    except Exception as e:
        st.error(f"❌ Erro ao carregar o agente: {e}")
        st.stop()

# Inicializa o histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe o histórico de mensagens
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------
# Processa a nova pergunta do usuário
# ----------------------------
if pergunta := st.chat_input("Sua pergunta:"):
    
    # Adiciona a pergunta ao histórico e exibe
    st.session_state.messages.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)

    # Gera a resposta com o agente
    with st.chat_message("assistant"):
        with st.spinner("Buscando a resposta..."):
            try:
                # Chama a função de resposta
                resposta = responder_agente(st.session_state["agente"], pergunta)
                
                # Adiciona a resposta ao histórico e exibe
                st.session_state.messages.append({"role": "assistant", "content": resposta})
                st.markdown(resposta)

            except Exception as e:
                st.error(f"❌ Erro ao processar a pergunta: {e}")
