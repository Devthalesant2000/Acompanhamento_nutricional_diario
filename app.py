import os
import json

import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

st.set_page_config(page_title="Streamlit + Google Sheets", page_icon="📊", layout="wide")

st.title("🔐 Google Sheets privado no Streamlit")
st.write("Lendo dados de uma planilha protegida usando Service Account.")

# 👉 Coloque aqui o ID da sua planilha (o que aparece na URL entre /d/ e /edit)
SPREADSHEET_ID = "1Der-KiDRDwwxApcOREQm0zCyBJhBIdB6y2nZlhJmaIY"
SHEET_NAME = "proteinas"  # troque pelo nome real da aba (ex: 'Base', 'Dados', etc.)

# Scopes necessários para acessar o Sheets (apenas leitura)
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# Carrega as credenciais do JSON que vamos passar via variável de ambiente
service_account_info_str = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")

if not service_account_info_str:
    st.error("Variável de ambiente GOOGLE_SERVICE_ACCOUNT_JSON não encontrada.")
else:
    try:
        service_account_info = json.loads(service_account_info_str)

        creds = Credentials.from_service_account_info(
            service_account_info,
            scopes=SCOPES,
        )

        client = gspread.authorize(creds)

        # Abre a planilha pelo ID e pega a aba
        sh = client.open_by_key(SPREADSHEET_ID)
        worksheet = sh.worksheet(SHEET_NAME)

        # Lê todos os registros em forma de lista de dicts
        records = worksheet.get_all_records()
        df = pd.DataFrame(records)

        st.subheader("Dados da planilha 📑")
        st.dataframe(df, use_container_width=True)

        st.write("Primeiras linhas:")
        st.dataframe(df.head(), use_container_width=True)

    except Exception as e:
        st.error("Erro ao carregar dados do Google Sheets 😥")
        st.code(str(e))
