import streamlit as st
from groq import Groq
from PIL import Image
import numpy as np
import io
import pandas as pd

import streamlit as st
import pandas as pd

# --- Configuración de la Página ---
st.set_page_config(
    page_title="BioMentor IA – Tu guía inteligente en biología",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🤖 BioMentor IA – Tu guía inteligente en biología")

# --- Subida de CSV ---
st.sidebar.header("📂 Cargar datos")
uploaded_file = st.sidebar.file_uploader("Sube un archivo CSV", type=["csv"])

# Variable de sesión para el chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Lógica principal ---
if uploaded_file is not None:
    # Leer CSV
    df = pd.read_csv(uploaded_file)
    st.success("✅ Archivo cargado correctamente")

    # Mostrar preview
    st.subheader("📊 Vista previa de los datos")
    st.dataframe(df.head())

    # --- Chat ---
    st.subheader("💬 Chat con BioMentor IA")

    # Mostrar historial de mensajes
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Entrada de usuario
    if prompt := st.chat_input("Hazme una pregunta sobre biología o sobre el dataset..."):
        # Guardar mensaje del usuario
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Respuesta del asistente (aquí por ahora es un placeholder)
        response = f"Estoy procesando tu pregunta: **{prompt}**. Pronto tendré una respuesta."
        st.session_state.messages.append({"role": "assistant", "content": response})

        with st.chat_message("assistant"):
            st.markdown(response)

else:
    st.warning("☝️ Por favor, carga un archivo CSV para habilitar el chat.")
