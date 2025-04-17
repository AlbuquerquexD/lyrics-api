import requests
import streamlit as st

col1, col2, col3 = st.columns([3, 1, 2])

with col1:
    st.title("Pesquisar Lyrics (lyrics.ovh)")
    busca_artista = st.text_input(label='Nome do artista')
    busca_musica = st.text_input(label='Nome da música')

    endpoint = f"https://api.lyrics.ovh/v1/seu jorge/mina do condominio"

    response = requests.get(endpoint)

    key = list(response.json().keys())[0]

    data = response.json()[key]

    print(data)

# with col2:
#     st.write('Coluna2')

with col3:
    with st.container(height=600):
        st.write(data)