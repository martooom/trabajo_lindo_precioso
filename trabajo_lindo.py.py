# -*- coding: utf-8 -*-
"""Untitled27.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lKGLZCpqLTCPHDMeQNQZXGF7bAyHB1A-
"""

import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt

# Título principal de la app
st.title("Cantidad de Terremotos en Chile")

# Cargar y mostrar la imagen
image = Image.open("terremoto.jpg")
st.image(image, caption="Terremoto", use_column_width=True)

# Barra lateral
st.sidebar.title("Información adicional")
st.sidebar.write("Esto es una barra lateral donde puedes encontrar recomendaciones y más.")

# Botón para mostrar tips de seguridad
if st.sidebar.button("Haz clic para ver tips"):
    st.sidebar.write("""
    - Mantente alejado de ventanas, espejos y muebles grandes.
    - Si el edificio es estructuralmente endeble, sal de él lo más rápido posible.
    - Si estás afuera, corre a un área abierta lejos de edificios y cables eléctricos que puedan caer.
    """)

# Entrada de texto en la barra lateral
user_input = st.sidebar.text_input("Escribe algo aquí:")
if user_input:
    st.sidebar.write(f"Has escrito: {user_input}")

# Título de las estadísticas
st.subheader("Estadísticas de terremotos en Chile (2010-2023)")

# Datos sobre la cantidad de terremotos
data = {
    "Años": [2010, 2012, 2014, 2016, 2018, 2020, 2022, 2023],
    "Cantidad de Terremotos": [300, 1500, 2000, 2500, 2300, 2500, 3000, 2800]
}
df = pd.DataFrame(data)

# Mostrar tabla con datos
st.write(df)

# Crear gráfico de barras con Altair
chart = alt.Chart(df).mark_bar().encode(
    x='Años:O',  # Eje X con los años
    y='Cantidad de Terremotos:Q',  # Eje Y con la cantidad de terremotos
    color='Años:O',  # Colorear las barras por el año
    tooltip=['Años', 'Cantidad de Terremotos']  # Mostrar los valores al pasar el mouse
).properties(
    title="Cantidad de Terremotos por Año en Chile"
)

# Mostrar el gráfico
st.altair_chart(chart, use_container_width=True)