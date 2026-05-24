import streamlit as st

import pandas as pd

import streamlit as axes

import numpy as np

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
    col1.metric("Total Ingresos", f"S/{total_ingresos:,.2f}")
    col2.metric("Total Gastos", f"S/{total_gastos:,.2f}")
    col3.metric("Saldo Final", f"S/{saldo_final:,.2f}")

    if saldo_final >= 0:
        st.success(f"🔴 El flujo de caja está **A FAVOR** con un saldo de S/{saldo_final:,.2f}")
    else:
        st.error(f"🚨 El flujo de caja está **EN CONTRA** con un déficit de S/{saldo_final:,.2f}")


elif Ejercicio == "Ejercicio 2":
  st.write("Bienvenido Ejercicio 2: Registro con NumPy y DataFrames")
  st.image("Numpy.png")
  if "np_nombres" not in st.session_state:
    st.session_state.np_nombres = np.array([], dtype=str)
    st.session_state.np_categorias = np.array([], dtype=str)
    st.session_state.np_precios = np.array([], dtype=float)
    st.session_state.np_cantidades = np.array([], dtype=int)
    st.session_state.np_totales = np.array([], dtype=float)
  st.markdown("""
Este módulo implementa un formulario de control y registro de inventario automatizado. 
A diferencia del almacenamiento clásico, los datos capturados se procesan vectorialmente 
mediante arreglos unidimensionales de **NumPy**. Al confirmar la operación, las estructuras 
numéricas se consolidan y transforman dinámicamente en un objeto **DataFrame** indexado.
""")

  st.markdown("---")

  st.subheader("🛒 Formulario de Alta de Productos")
  col_nom, col_cat, col_pre, col_can = st.columns(4)

  with col_nom:
      prod_nombre = st.text_input("Nombre del Producto:", placeholder="Ej. Monitor Gamer", key="np_prod_nom")

  with col_cat:
      prod_categoria = st.selectbox("Categoría:", ["Electrónica", "Línea Blanca", "Oficina", "Ferretería"], key="np_prod_cat")

  with col_pre:
      prod_precio = st.number_input("Precio Unitario (S/):", min_value=0.0, step=0.5, format="%.2f", key="np_prod_pre")

  with col_can:
      prod_cantidad = st.number_input("Cantidad Mínima:", min_value=1, step=1, key="np_prod_can")

  if st.button("Agregar Nuevo Registro", type="primary", use_container_width=True):
    if prod_nombre.strip() == "":
        st.warning("⚠️ Ingrese un nombre válido para el producto antes de continuar.")
    elif prod_precio <= 0:
        st.warning("⚠️ El precio unitario asignado debe ser mayor a cero.")
    else:
        prod_total = prod_precio * prod_cantidad
        
        st.session_state.np_nombres = np.append(st.session_state.np_nombres, prod_nombre)
        st.session_state.np_categorias = np.append(st.session_state.np_categorias, prod_categoria)
        st.session_state.np_precios = np.append(st.session_state.np_precios, prod_precio)
        st.session_state.np_cantidades = np.append(st.session_state.np_cantidades, prod_cantidad)
        st.session_state.np_totales = np.append(st.session_state.np_totales, prod_total)
        
        st.success(f"✅ ¡Producto '{prod_nombre}' registrado y transformado en array NumPy!")

  st.markdown("---")

  st.subheader("📋 Tabla General de Inventario Actualizada")

  if len(st.session_state.np_nombres) > 0:

    df_inventario = pd.DataFrame({
        "Nombre del Producto": st.session_state.np_nombres,
        "Categoría": st.session_state.np_categorias,
        "Precio (S/)": st.session_state.np_precios,
        "Cantidad": st.session_state.np_cantidades,
        "Total (S/)": st.session_state.np_totales
    })
    
    st.dataframe(df_inventario, use_container_width=True)
    
    total_invertido = np.sum(st.session_state.np_totales)
    total_articulos = np.sum(st.session_state.np_cantidades)
    st.info(f"💡 **Resumen operativo:** Contamos con {total_articulos} artículos en bodega, representando un valor de inversión total de S/ {total_invertido:,.2f}")
  else:
    st.info("💡 No existen registros vectoriales almacenados. Use el formulario superior para añadir artículos.")


elif Ejercicio == "Ejercicio 3":
   st.write("Bienvenido Ejercicio 3: Uso de funciones desde una librería externa")
   st.image("Libreria.png")
   try:
    from libreria_funciones_proyecto1 import calcular_interes_compuesto
   except Exception:
    def calcular_interes_compuesto(capital: float, tasa: float, periodos: int) -> float:
        return round(capital * (1 + (tasa / 100)) ** periodos, 2)
    if "historico_funciones" not in st.session_state:
        st.session_state.historico_funciones = pd.DataFrame(columns=[
        "Función Ejecutada", "Parámetro 1", "Parámetro 2", "Parámetro 3", "Resultado Final"
        ])


elif Ejercicio == "Ejercicio 4":
   st.write("Bienvenido Ejercicio 4")
   st.image("Crud.png")


