import streamlit as st

# Função simples do agente (2 ramificações)
def agente_resposta(pergunta: str):
    conhecimento = {
        "horário de atendimento": "Nosso horário é de segunda a sexta, das 9h às 18h.",
        "produtos": "Oferecemos soluções de automação inteligente com IA."
    }

    for chave, resposta in conhecimento.items():
        if chave in pergunta.lower():
            return resposta
    
    return "Não tenho certeza sobre isso. Pode me dar mais detalhes?"

# Configuração da página
st.set_page_config(page_title="Agente BECC", page_icon="🤖")

st.title("🤖 Olá, sou seu agente BECC!")
st.write("Em que posso te ajudar hoje?")

pergunta = st.text_input("Digite sua intenção:")

if st.button("Enviar"):
    if pergunta.strip():
        resposta = agente_resposta(pergunta)
        st.success(resposta)
    else:
        st.warning("Por favor, digite uma pergunta.")
