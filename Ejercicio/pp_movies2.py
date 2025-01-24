import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt


st.title("Datos movies.csv")

data = pd.read_csv("Ejercicio/movies.csv", index_col="id")
del data["index"]
st.dataframe(data)

col1, col2 = st.columns(2)

# Gráfico 1: Gráfico de barras de colesterol
with col1:
    st.write("Gráfico de barras de colesterol:")
    grafico = data['cholesterol'].value_counts().plot(kind="bar")
    st.pyplot(grafico.figure)  # Mostrar el gráfico en la primera columna


# Gráfico 2: Boxplot de ap_hi por cardio
with col2:
    st.write("Boxplot de presión arterial (ap_hi) en función de (cardio):")
    grafico2 = data.boxplot(column="ap_hi", by="cardio", ax=None, fontsize=None, rot=90, grid=True)
    st.pyplot(grafico2.figure)  # Mostrar el gráfico en la segunda columna


