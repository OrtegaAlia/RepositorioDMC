import streamlit as st

import pandas as pd

st.title("Plataforma Integrada de Soluciones Financieras ")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Alia Ortega")

st.sidebar.image("LOGO.png")

st.sidebar.subheader("Módulo 1: Fundamentos de Programación")

st.sidebar.write("**Nombre Completo:** Alia Ortega Alvarado")
st.sidebar.write("**Especialidad / Rol:** Analista de Contabilidad")
st.sidebar.write("**Año Académico:** 2026")

st.sidebar.markdown("### 📋 Descripción del Proyecto")

st.sidebar.markdown("""
    Este proyecto es una aplicación interactiva diseñada para centralizar flujos de trabajo clave. 
    Permite realizar el control de **flujos de caja**, y la gestión avanzada con **Numpy**,
    así como la ejecución de cálculos financieros y operaciones **CRUD** completas mediante módulos 
    y librerías externas de Python.
    """)

st.sidebar.markdown("### 🛠️ Tecnologías Utilizadas")

st.sidebar.write("Streamlit, NumPy, arrays, DataFrame y Pandas")

Ejercicio = st.sidebar.selectbox("📋Seleccione un Ejercicio", ["Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"] )

if Ejercicio == "Ejercicio 1":
  st.write("Bienvenido Ejercicio 1: Flujo de Caja con listas")
  st.image("Flujo de Caja.png")
  st.subheader("Registrar Nuevo Movimiento")
  Concepto = st.text_input("Concepto", placeholder="Ej. Pago de alquiler, Salario")
  Tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
  Valor = st.number_input("Valor (S/)", min_value=0.0, step=10.0, format="%.2f")

elif Ejercicio == "Ejercicio 2":
  st.write("Bienvenido Ejercicio 2")
  st.image("Numpy.png")

elif Ejercicio == "Ejercicio 3":
  st.write("Bienvenido Ejercicio 3")
  st.image("Libreria.png")

elif Ejercicio == "Ejercicio 4":
  st.write("Bienvenido Ejercicio 4")
  st.image("Crud.png")


