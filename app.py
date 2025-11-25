import streamlit as st

st.set_page_config(page_title="Hello Cloud", page_icon="☁️")

st.title("Hello, world! 🚀")
st.write("Seu primeiro app Streamlit rodando no Google Cloud Run via GitHub.")

nome = st.text_input("Digite seu nome:")
if nome:
    st.success(f"Bem-vinda(o), {nome}! Deploy funcionando certinho 😍")