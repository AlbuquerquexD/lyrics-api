# 🎤 App de Busca de Letras de Músicas (lyrics.ovh)

Este é um aplicativo simples feito com **Streamlit** para buscar letras de músicas usando a [API lyrics.ovh](https://lyrics.ovh/). Ele permite ao usuário inserir o nome do artista e da música e exibe a letra correspondente — se encontrada.

👉 [Clique aqui para abrir no Streamlit Cloud](https://lyrics-api-music.streamlit.app/)

---

## 🚀 Como usar

1. **Instale as dependências (caso ainda não tenha)**:
   ```bash
   pip install streamlit requests

2. **Rode o aplicativo:**  
    ```bash
    streamlit run app.py

3. **No navegador:**

    * Digite o nome do artista.
    * Digite o nome da música.
    * Pressione Enter para buscar a letra.

## 🧪 Finalidade

Este projeto é apenas para **fins educacionais**, com o objetivo de:
- Fazer requisições HTTP com `requests`
- Consumir uma API pública simples ([lyrics.ovh](https://lyrics.ovh))

---

## 📦 Tecnologias usadas

- **Streamlit** – para criar a interface web
- **Requests** – para consumir a API REST
- **lyrics.ovh API** – fonte de dados das letras