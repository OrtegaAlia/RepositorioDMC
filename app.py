import streamlit as st

import pandas as pd

import streamlit as axes

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
  st.markdown("""
    Esta aplicación permite registrar tus movimientos financieros diarios. 
    Ingresa el concepto, el tipo de movimiento y el valor para calcular tu saldo final.
    """)
  if "movimientos" not in st.session_state:
    st.session_state.movimientos = []
  st.subheader("Registrar Nuevo Movimiento")
  Concepto = st.text_input("Concepto", placeholder="Ej. Pago de alquiler, Salario")
  Tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
  Valor = st.number_input("Valor (S/)", min_value=0.0, step=10.0, format="%.2f")
if st.button("Agregar movimiento"):
    if Concepto.strip() == None:
        st.warning("Por favor, ingresa un concepto válido.")
    elif Valor <= 0:
        st.warning("El valor debe ser mayor a cero.")
    else:
        if "movimientos" not in st.session_state:
            st.session_state.movimientos = []
            
        nuevo_movimiento = {
            "Concepto": Concepto,
            "Tipo": Tipo,
            "Valor": Valor
        }
        st.session_state.movimientos.append(nuevo_movimiento)
        st.toast("Movimiento agregado con éxito")
if st.session_state.movimientos:
    df = pd.DataFrame(st.session_state.movimientos)
    st.subheader("Historial de Movimientos")
    st.dataframe(df, use_container_width=True)
    
    total_ingresos = df[df["Tipo"] == "Ingreso"]["Valor"].sum()
    total_gastos = df[df["Tipo"] == "Gasto"]["Valor"].sum()
    saldo_final = total_ingresos - total_gastos

    st.subheader("Resumen Financiero")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Ingresos", f"${total_ingresos:,.2f}")
    col2.metric("Total Gastos", f"${total_gastos:,.2f}")
    col3.metric("Saldo Final", f"${saldo_final:,.2f}")

    if saldo_final >= 0:
        st.success(f"🔴 El flujo de caja está **A FAVOR** con un saldo de ${saldo_final:,.2f}")
    else:
        st.error(f"🚨 El flujo de caja está **EN CONTRA** con un déficit de ${saldo_final:,.2f}")


elif Ejercicio == "Ejercicio 2":
  st.write("Bienvenido Ejercicio 2")
  st.image("Numpy.png")

elif Ejercicio == "Ejercicio 3":
  st.write("Bienvenido Ejercicio 3")
  st.image("Libreria.png")

elif Ejercicio == "Ejercicio 4":
  st.write("Bienvenido Ejercicio 4")
  st.image("Crud.png")


