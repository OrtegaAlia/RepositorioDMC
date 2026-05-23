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
    st.markdown("### 🧑‍💻 Información del Estudiante")
    st.write("**Nombre Completo:** Alia Ortega Alvarado")
    st.write("**Especialidad / Rol:** Analista de Contabilidad")
    st.write("**Año Académico:** 2026")

with col2:
st.markdown("### 📋 Descripción del Proyecto")
st.markdown("""Este proyecto es una aplicación interactiva diseñada para centralizar flujos de trabajo clave. 
Permite realizar el control de **flujos de caja**, la gestión avanzada de ingresos y gastos, 
así como la ejecución de cálculos financieros y operaciones **CRUD** completas mediante módulos y librerías externas de Python.""")
