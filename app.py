import streamlit as st
from agente import carregar_agente, responder_agente

# ----------------------------
# Configuração da página
# ----------------------------
st.set_page_config(page_title="RoBECC Agente", page_icon="🤖")

st.title("🤖 RoBECC Agente")
st.subheader("Assistente de Políticas Internas (RH/IT)")
st.write("Digite sua pergunta abaixo e eu responderei com base nos documentos fornecidos.")

# ----------------------------
# Inicializa o agente (uma vez)
# ----------------------------
if "agente" not in st.session_state:
    try:
        st.session_state["agente"] = carregar_agente("DADOS")
        st.success("✅ Agente inicializado com sucesso! PDFs carregados.")
    except Exception as e:
        st.error(f"Erro ao carregar o agente: {e}")
        st.stop()

# ----------------------------
# Campo de input do usuário
# ----------------------------
pergunta = st.text_input("Sua pergunta:")

# ----------------------------
# Botão de envio
# ----------------------------
if st.button("Enviar"):
    if pergunta.strip():
        try:
            resposta = responder_agente(st.session_state["agente"], pergunta)

            # Agora o responder_agente retorna diretamente a resposta final
            st.markdown("### 📝 Resposta")
            st.success(resposta)

        except Exception as e:
            st.error(f"Erro ao processar a pergunta: {e}")
    else:
        st.warning("Por favor, digite uma pergunta.")
