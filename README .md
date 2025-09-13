# 🤖 BECC Agent – Streamlit App

Este projeto disponibiliza um **agente de IA com 2 ramificações**:  
1. Responde imediatamente se souber a resposta.  
2. Se não souber, pede mais informações ao usuário.  

🚫 Importante: o agente **não encaminha tickets** – ele só responde ou pede mais detalhes.

---

## 📂 Estrutura do projeto
```
app.py              # Interface Streamlit (front-end)
agente.py           # Código do agente (LangChain + Gemini + FAISS)
requirements.txt    # Dependências do projeto
README.md           # Este guia
```

---

## 🚀 Como rodar localmente
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Rode o app:
   ```bash
   streamlit run app.py
   ```

---

## 🌐 Deploy no Streamlit Cloud
1. Crie um repositório no GitHub com os arquivos acima.  
2. Vá em [Streamlit Cloud](https://streamlit.io/cloud), conecte sua conta GitHub.  
3. Escolha o repositório, branch `main` e arquivo principal `app.py`.  
4. Clique em **Deploy**.  

O app ficará disponível em:
```
https://beccagent.streamlit.app
```

---

## 🔑 Configuração de APIs
Este agente usa **Google Generative AI (Gemini)** para geração de respostas e embeddings.  
⚠️ Configure sua chave de API no **Secrets** do Streamlit Cloud (não deixe no código).  

No menu do Streamlit Cloud:
1. Vá em **Settings > Secrets**.  
2. Adicione:
   ```toml
   GOOGLE_API_KEY = "sua_chave_aqui"
   ```

---

## 🧩 Como funciona
- Carrega documentos (ex: PDF) e cria uma base vetorial com FAISS.  
- Usa embeddings do **Google Generative AI**.  
- Faz busca semântica e responde baseado na sua base.  
- Se não souber, pede mais detalhes ao usuário.  

---

Feito com 💡 pela **BECC Automação Inteligente**.
