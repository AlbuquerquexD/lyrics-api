import requests
import streamlit as st

st.set_page_config(layout="wide")  # ou "centered"

col1, col2, col3 = st.columns([2, 0.2, 3])

with col1:
    st.title("Pesquisar Lyrics (lyrics.ovh)")

    busca_artista = st.text_input(label='Nome do artista')
    busca_musica = st.text_input(label='Nome da música')
    
    st.write("")
    st.info("📢 Pressione 'Enter' para buscar")

    try:
        # st.info('Pressione "ENTER" para pesquisar')
        endpoint = f"https://api.lyrics.ovh/v1/{busca_artista}/{busca_musica}"

        response = requests.get(endpoint)

        if response.status_code == 200:
            data = response.json().get("lyrics")
            # data = response.json()[key]

        else:
            data = "No lyrics found"
    except Exception as e:
        print(e)        

with col2:
    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjRrdTB5enFocHJ4cTlnM21kc2Nka2YxOGZhbmh6ZmRqamtsdzJldyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/vybWlRniCXzZC/giphy.gif", width=200)

with col3:
    with st.container(height=600):
        st.text_area(label=" ", value=data, height=600)