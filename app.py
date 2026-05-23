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
  st.write("Bienvenido Ejercicio 1")
  st.image("Flujo de Caja.png")

if "lista_movimientos" not in st.session_state:
st.session_state.lista_movimientos = []
st.markdown("""
Este módulo permite registrar de forma dinámica tus movimientos financieros. 
Cada registro captura el concepto, tipo de operación y monto. Las transacciones se 
almacenan de manera secuencial para procesar balances económicos en tiempo real.
""")
st.subheader("📥 Registro de Nuevo Movimiento")
col_concepto, col_tipo, col_valor = st.columns(3)

with col_concepto:
    concepto = st.text_input("Concepto:", placeholder="Ej. Pago de Consultoría", key="input_concepto")

with col_tipo:
    tipo_movimiento = st.selectbox("Tipo de Movimiento:", ["Ingreso", "Gasto"], key="sb_tipo")

with col_valor:
    valor = st.number_input("Valor (S/):", min_value=0.0, step=10.0, format="%.2f", key="num_valor")


elif Ejercicio == "Ejercicio 2":
  st.write("Bienvenido Ejercicio 2")
  st.image("Numpy.png")

elif Ejercicio == "Ejercicio 3":
  st.write("Bienvenido Ejercicio 3")
  st.image("Libreria.png")

elif Ejercicio == "Ejercicio 4":
  st.write("Bienvenido Ejercicio 4")
  st.image("Crud.png")


