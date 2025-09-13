# 🤖 BECC Agent – Streamlit App (OpenAI)

Este projeto disponibiliza um **agente de IA com 2 ramificações**:  
1. Responde imediatamente se souber a resposta.  
2. Se não souber, pede mais informações ao usuário.  

🚫 Importante: o agente **não encaminha tickets** – ele só responde ou pede mais detalhes.

---

## 📂 Estrutura do projeto
```
app.py              # Interface Streamlit (front-end)
agente.py           # Código do agente (LangChain + OpenAI + FAISS)
requirements.txt    # Dependências do projeto
README.md           # Este guia
DADOS/              # Pasta com documentos PDF usados como base de conhecimento
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
   venv\Scripts\activate   # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure a variável de ambiente da OpenAI:
   ```bash
   export OPENAI_API_KEY="sua_chave_aqui"   # Linux/Mac
   setx OPENAI_API_KEY "sua_chave_aqui"     # Windows
   ```

5. Rode o app:
   ```bash
   streamlit run app.py
   ```

---

## 🌐 Deploy no Streamlit Cloud
1. Crie um repositório no GitHub com os arquivos acima.  
2. Vá em [Streamlit Cloud](https://streamlit.io/cloud), conecte sua conta GitHub.  
3. Escolha o repositório, branch `main` e arquivo principal `app.py`.  
4. Em **Settings > Secrets**, adicione sua chave da OpenAI:
   ```toml
   OPENAI_API_KEY = "sua_chave_aqui"
   ```
5. Clique em **Deploy**.  

O app ficará disponível em:
```
https://beccagent.streamlit.app
```

---

## 🔑 Modelos usados
- **LLM**: `gpt-4o-mini` (rápido, barato, ótimo para testes).  
- **Embeddings**: `text-embedding-3-small` (econômico e eficiente).  

---

## 🧩 Como funciona
- Carrega documentos (ex: PDFs na pasta `DADOS/`) e cria uma base vetorial com FAISS.  
- Usa embeddings da OpenAI.  
- Faz busca semântica e responde baseado na sua base.  
- Se não souber, pede mais detalhes ao usuário.  

---

Feito com 💡 pela **BECC Automação Inteligente**.
