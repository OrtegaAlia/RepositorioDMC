import streamlit as st

st.title("Plataforma Integrada de Soluciones Financieras ")

URL_LOGO = "https://python.org"

st.image(URL_LOGO, width=200, caption="Python DMC")

st.write("Elaborado por Alia Ortega")

st.subheader("Módulo: Python para Analítica de Datos (Python DMC)")

st.sidebar.title("Parámetros")

st.header("📋 Información del Proyecto")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Estudiante:**")
    st.text("Alia Ortega Alvarado")

with col2:
    st.markdown("**Información General:**")
    st.text("Analista de Contabilidad / Administración y Finanzas / ME Elecmetal Comercial Perú S.A.C.")
    
    st.markdown("**Año:**")
    st.text("2026")
