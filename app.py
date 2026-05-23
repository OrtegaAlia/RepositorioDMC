import streamlit as st

import pandas as pd

st.title("Plataforma Integrada de Soluciones Financieras ")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Alia Ortega")

st.sidebar.image("LOGO.png")

Ejercicio = st.sidebar.selectbox("Seleccione un Ejercicio", ["Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"] )

if Ejercicio == "Ejercicio 1":
  st.write("Bienvenido Ejercicio 1")
  st.image("Flujo de Caja.png")

elif Ejercicio == "Ejercicio 2":
  st.write("Bienvenido Ejercicio 2")

elif Ejercicio == "Ejercicio 3":
  st.write("Bienvenido Ejercicio 3")

elif Ejercicio == "Ejercicio 4":
  st.write("Bienvenido Ejercicio 4")

st.subheader("Módulo: Python para Analítica de Datos (Python DMC)")

st.header("📋 Información del Proyecto")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🧑‍💻 Información del Estudiante")
    st.write("**Nombre Completo:** Alia Ortega Alvarado")
    st.write("**Especialidad / Rol:** Analista de Contabilidad")
    st.write("**Año Académico:** 2026")

with col2:
    st.markdown("### 📋 Descripción del Proyecto")
    st.markdown("""Este proyecto es una aplicación interactiva diseñada para centralizar flujos de trabajo clave. 
                   Permite realizar el control de **flujos de caja**, la gestión avanzada de ingresos y gastos, 
                   así como la ejecución de cálculos financieros y operaciones **CRUD** completas mediante módulos y librerías externas de Python.""")

