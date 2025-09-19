import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Análisis de los hospitales del Perú", layout="wide")

# Tabs with icons
tab1, tab2, tab3 = st.tabs([
    "Data Description",
    "Static Maps & Department Analysis",
    "Dynamic Maps"
])

with tab1:
    st.header("Descripción de Datos")
    df = pd.read_csv('IPRESS.csv',encoding='latin1')
   
    df = df[df["Condición"] == "EN FUNCIONAMIENTO"]

    df = df.dropna(subset=["NORTE", "ESTE"])           
    df = df[(df["NORTE"] != "") & (df["ESTE"] != "")]    

    df["NORTE"] = pd.to_numeric(df["NORTE"], errors="coerce")
    df["ESTE"]  = pd.to_numeric(df["ESTE"], errors="coerce")

    df = df.dropna(subset=["NORTE", "ESTE"])
    df = df.rename(columns={"NORTE": "longitud", "ESTE": "latitud"})

    total_hospitales = len(df)
    total_publicos = len(df[df["Institución"] != "PRIVADO"])
    total_privados = len(df[df["Institución"] == "PRIVADO"])

    c1, c2, c3 = st.columns(3)

    with c1:
        st.caption("Total de Hospitales en Funcionamiento")
        st.markdown(f"## {total_hospitales}")

    with c2:
        st.caption("Hospitales Públicos en Funcionamiento")
        st.markdown(f"## {total_publicos}")

    with c3:
        st.caption("Hospitales Privados en Funcionamiento")
        st.markdown(f"## {total_privados}")
        
    st.divider()  # línea separadora
    st.markdown("### Distribución por Distrito")    
    # Mostrar gráficos guardados en disco
    st.image("D:\TASK 2\Total Operational Hospitals by District.png", caption="Gráfico 1")

with tab2:
    st.header("Mapas Estáticos y Análisis por Departamento")
    st.image("D:\TASK 2\Hospitales EN FUNCIONAMIENTO por distrito.png", caption="Hospitales en funcionamiento por distrito")
    st.image("D:\TASK 2\Districts with Zero Public Hospitals.png", caption="Distritos sin hospitales públicos")
    st.image("D:\TASK 2\Top 10 Districts by Number of Public Hospitals.png", caption="Top 10 distritos por número de hospitales públicos")
    st.divider()  # línea separadora
    st.image("D:\TASK 2\Total Operational Hospitals by Department.png", caption="Total de hospitales en funcionamiento por departamento")
    st.image("D:\TASK 2\Operational Hospitals per Department.png", caption="Hospitales en funcionamiento por departamento")
with tab3:
    st.header("Mapas Dinámicos")
    # Mostrar mapas HTML guardados en disco
    with open("D:\TASK 2\mapa_nacional_hospitales.html", "r", encoding="utf-8") as f:
        mapa_html = f.read()
    st.components.v1.html(mapa_html, height=600)
    st.markdown("### Proximidad de Hospitales en Centros de Alta Concentración Poblacional")
    
    with open("D:\TASK 2\lima_concentration.html", "r", encoding="utf-8") as f:
        mapa_lima_html = f.read()
    st.components.v1.html(mapa_lima_html, height=600)   
    with open("D:\TASK 2\3.2_mapa_nacional_hospitales_proximity.html", "r", encoding="utf-8") as f:
        mapa_proximidad_html = f.read()
    st.components.v1.html(mapa_proximidad_html, height=600)
