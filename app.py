import streamlit as st

import pandas as pd

st.title("Plataforma Integrada de Soluciones Financieras ")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Alia Ortega")

st.sidebar.image("LOGO.png")

st.sidebar.subheader("Módulo: Python para Analítica de Datos (Python DMC)")

st.sidebar.write("**Nombre Completo:** Alia Ortega Alvarado")
st.sidebar.write("**Especialidad / Rol:** Analista de Contabilidad")
st.sidebar.write("**Año Académico:** 2026")

Ejercicio = st.sidebar.selectbox("Seleccione un Ejercicio", ["Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"] )

if Ejercicio == "Ejercicio 1":
  st.write("Bienvenido Ejercicio 1")
  st.image("Flujo de Caja.png")

elif Ejercicio == "Ejercicio 2":
  st.write("Bienvenido Ejercicio 2")
  st.image("Numpy.png")

elif Ejercicio == "Ejercicio 3":
  st.write("Bienvenido Ejercicio 3")
  st.image("Libreria.png")

elif Ejercicio == "Ejercicio 4":
  st.write("Bienvenido Ejercicio 4")
  st.image("Crud.png")


