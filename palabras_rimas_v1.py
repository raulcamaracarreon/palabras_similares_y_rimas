import os
import pathlib
import random
import streamlit as st

def cargar_diccionario(path):
    diccionario = {}
    for letra in "abcdefghijklmnñopqrstuvwxyz":
        with open(os.path.join(path, f"{letra}.txt"), encoding="utf-8") as archivo:
            palabras = archivo.read().splitlines()
            for palabra in palabras:
                diccionario[palabra.lower()] = True
    return diccionario

def palabras_similares(palabra, diccionario):
    similares = []
    for key in diccionario.keys():
        if len(key) == len(palabra):
            diff_count = sum(1 for a, b in zip(palabra, key) if a != b)
            if diff_count == 1 or (diff_count == 2 and sorted(palabra) == sorted(key)):
                similares.append(key)
    return similares

def palabras_rima(palabra, diccionario):
    rimas = []
    for key in diccionario.keys():
        if key[-4:] == palabra[-4:]:
            rimas.append(key)
    return rimas

# Configuración de la aplicación Streamlit
st.set_page_config(
    page_title="Palabras similares y rimas",
    page_icon="🔡",
    layout="centered",
    initial_sidebar_state="auto",
)

# Cargar el diccionario
path = pathlib.Path(__file__).parent / "dict_rae_txt/dics"
diccionario = cargar_diccionario(path)

# Interfaz de usuario
st.title("Palabras similares y rimas")
st.write("Encuentra palabras similares y palabras que riman con la palabra ingresada.")
palabra = st.text_input("Introduce una palabra:")

if palabra:
    if palabra.lower() in diccionario:
        st.write("### Palabras similares")
        similares = palabras_similares(palabra, diccionario)
        if similares:
            st.write(", ".join(similares))
        else:
            st.write("No se encontraron palabras similares.")

        st.write("### Palabras que riman")
        rimas = palabras_rima(palabra, diccionario)
        if rimas:
            st.write(", ".join(rimas))
        else:
            st.write("No se encontraron palabras que rimen.")
    else:
        st.error("La palabra ingresada no se encuentra en el diccionario.")
else:
    st.write("Por favor, ingrese una palabra para buscar palabras similares y rimas.")
