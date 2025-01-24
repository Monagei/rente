import streamlit as st
import pandas as pd

st.title("Datos movies.csv")

data = pd.read_csv("Ejercicio/movies.csv")

st.dataframe(data)