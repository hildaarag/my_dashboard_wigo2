import streamlit as st
import os
from conexion_02 import cargar_datos
from indicadores_02 import *
from graficos_02 import *

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Wigo Motors - Control Comercial Ejecutivo",
    page_icon="📊",
    layout="wide"
)

# 2. ESTILOS CSS PERSONALIZADOS (Guía de Marca Oficial Wigo Motors)
st.markdown("""
    <style>
        .block-container {padding-top: 1rem; padding-bottom: 0rem;}
        
        /* Paleta Primaria: Navy #0A1F44 y Black #0E0E0E */
        h1 {
            color: #0A1F44; 
            font-weight: 800; 
            font-family: 'Montserrat', 'Inter', 'Segoe UI', sans-serif;
        }
        h3 {
            color: #0A1F44; 
            font-weight: 600; 
            border-bottom: 2px solid #8B95A1; 
            padding-bottom: 5px;
        }
        div[data-testid="stMetricValue"] {
            font-size: 1.8rem; 
            font-weight: 700; 
            color: #111827;
        }
        
        /* Botones con estilo corporativo Navy */
        .stButton>button {
            background-color: #0A1F44; 
            color: #FFFFFF; 
            border-radius: 6px; 
            font-weight: 600;
        }
        .stButton>button:hover {
            background-color: #111827; 
            color: #FFFFFF;
        }
        
        /* Contenedor del Tagline */
        .tagline {
            color: #8B95A1;
            font-size: 0.9rem;
            font-weight: 600;
            letter-spacing: 0.15em;
            text-transform: uppercase;
        }
    </style>
""", unsafe_allow_html=True)

# 3. CONTROL DE ACCESO (LOGIN EN SIDEBAR)
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def login():
    st.sidebar.title("🔐 Control de Acceso")
    user = st.sidebar.text_input("Usuario")
    password = st.sidebar.text_input("Contraseña", type="password")
    
    if st.sidebar.button("Iniciar Sesión"):
        if user == "admin" and password == "wigo2026":
            st.session_state["authenticated"] = True
            st.sidebar.success("¡Bienvenido!")
            st.rerun()
        else:
            st.sidebar.error("Usuario o contraseña incorrectos")

if not st.session_state["authenticated"]:
    # Encabezado del Login con Logo Oficial
    col_login_logo, col_login_texto = st.columns([1, 4], vertical_alignment="center")
    
    directorio_actual = os.path.dirname(__file__)
    ruta_logo = os.path.join(directorio_actual, "wigo_motors_logo.png")
    
    with col_login_logo:
        if os.path.exists(ruta_logo):
            st.image(ruta_logo, width=180)
        elif os.path.exists("wigo_motors_logo.png"):
            st.image("wigo_motors_logo.png", width=180)
        else:
            st.markdown("## **WIGO MOTORS**")
            
    with col_login_texto:
        st.title("WIGO MOTORS S.A.C.")
        st.markdown("<p class='tagline'>VENTA DE UNIDADES VEHICULARES A NIVEL NACIONAL</p>", unsafe_allow_html=True)
    
    st.info("Por favor, ingrese sus credenciales en la barra lateral para acceder al Dashboard de Alta Gerencia.")
    login()
    st.stop()

# Botón para cerrar sesión si ya está autenticado
if st.sidebar.button("Cerrar Sesión"):
    st.session_state["authenticated"] = False
    st.rerun()

import base64

def cargar_imagen_base64(ruta):
    with open(ruta, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")

directorio_actual = os.path.dirname(__file__)
ruta_banner = os.path.join(directorio_actual, "banner_wigo.png")
ruta_logo = os.path.join(directorio_actual, "wigo_motors_logo.png")

# Configurar imagen del banner de fondo
if os.path.exists(ruta_banner):
    banner_b64 = cargar_imagen_base64(ruta_banner)
    fondo_style = f"background-image: linear-gradient(rgba(10, 25, 50, 0.65), rgba(10, 25, 50, 0.75)), url('data:image/png;base64,{banner_b64}'); background-size: cover; background-position: center;"
else:
    fondo_style = "background-color: #0A192F;"

# Cargar logo
logo_html = ""
if os.path.exists(ruta_logo):
    logo_b64 = cargar_imagen_base64(ruta_logo)
    logo_html = f"<img src='data:image/png;base64,{logo_b64}' style='height: 80px; width: auto; margin-right: 25px; border-radius: 6px; box-shadow: 0px 4px 10px rgba(0,0,0,0.5);'>"

# SVG vectorizado para forzar texto blanco brillante independiente de Streamlit
svg_texto = """
<svg xmlns="http://www.w3.org/2000/svg" width="600" height="130" viewBox="0 0 600 130">
  <text x="0" y="35" font-family="Arial, Helvetica, sans-serif" font-size="32" font-weight="900" fill="#FFFFFF">WIGO MOTORS S.A.C.</text>
  <text x="0" y="65" font-family="Arial, Helvetica, sans-serif" font-size="20" font-weight="600" fill="#FFFFFF">Hilda Aragon</text>
  <text x="0" y="90" font-family="Arial, Helvetica, sans-serif" font-size="12" font-weight="800" fill="#93C5FD" letter-spacing="2">VENTA DE UNIDADES VEHICULARES A NIVEL NACIONAL</text>
  <rect x="0" y="102" width="410" height="24" rx="12" fill="rgba(255,255,255,0.2)" stroke="rgba(255,255,255,0.4)"/>
  <text x="12" y="118" font-family="Arial, Helvetica, sans-serif" font-size="11" font-weight="600" fill="#FFFFFF">Dashboard Ejecutivo de Control Comercial | Reporte Gerencial</text>
</svg>
"""
svg_b64 = base64.b64encode(svg_texto.encode('utf-8')).decode('utf-8')

# 4. ENCABEZADO INDESTRUCTIBLE POR CSS
st.markdown(f"""
    <div style="
        {fondo_style}
        border-radius: 12px;
        padding: 25px 35px;
        margin-bottom: 25px;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.4);
        display: flex;
        align-items: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
    ">
        {logo_html}
        <div style="background: rgba(10, 20, 35, 0.6); padding: 15px 20px; border-radius: 10px; backdrop-filter: blur(5px);">
            <img src="data:image/svg+xml;base64,{svg_b64}" style="display: block; height: 120px; width: auto;" />
        </div>
    </div>
""", unsafe_allow_html=True)

# 5. CARGA DE DATOS DESDE LA BASE DE DATOS
df = cargar_datos()

if df.empty:
    st.error("No se pudieron cargar los datos comerciales desde la base de datos.")
    st.stop()

# 6. PANEL LATERAL DE FILTROS
st.sidebar.header("🎯 Filtros de Selección")

# Filtro 1: Marca (Audi, BMW, Chevrolet, Glory, Hyundai, Kia, Mazda, Subaru, Suzuki, Toyota)
marcas_disponibles = sorted(df["marca"].unique())
marcas_seleccionadas = st.sidebar.multiselect("Filtrar por Marca", marcas_disponibles, default=marcas_disponibles)

df_pre_filtrado = df[df["marca"].isin(marcas_seleccionadas)]

if not df_pre_filtrado.empty:
    precio_min_dinamico = float(df_pre_filtrado["precio_venta"].min())
    precio_max_dinamico = float(df_pre_filtrado["precio_venta"].max())
else:
    precio_min_dinamico = float(df["precio_venta"].min())
    precio_max_dinamico = float(df["precio_venta"].max())

if precio_min_dinamico == precio_max_dinamico:
    precio_min_dinamico -= 1.0

rango_precios = st.sidebar.slider(
    "Filtrar por Rango de Precios (S/.)",
    min_value=precio_min_dinamico,
    max_value=precio_max_dinamico,
    value=(precio_min_dinamico, precio_max_dinamico),
    step=500.0,
    format="S/.%,.0f"
)

sedes_disponibles = sorted(df["tienda"].unique())
sedes_seleccionadas = st.sidebar.multiselect("Filtrar por Sede", sedes_disponibles, default=sedes_disponibles)

asesores_disponibles = sorted(df["asesor_comercial"].unique())
asesores_seleccionadas = st.sidebar.multiselect("Filtrar por Asesor", asesores_disponibles, default=asesores_disponibles)

pagos_disponibles = sorted(df["metodo_pago"].unique())
pagos_seleccionadas = st.sidebar.multiselect("Filtrar por Método de Pago", pagos_disponibles, default=pagos_disponibles)

# APLICACIÓN DE FILTROS
df_filtrado = df[
    (df["marca"].isin(marcas_seleccionadas)) &
    (df["tienda"].isin(sedes_seleccionadas)) &
    (df["asesor_comercial"].isin(asesores_seleccionadas)) &
    (df["metodo_pago"].isin(pagos_seleccionadas)) &
    (df["precio_venta"] >= rango_precios[0]) &
    (df["precio_venta"] <= rango_precios[1])
]

# 7. LOGOS DE MARCAS EN MÉTRICAS
st.subheader("🏎️ Marcas Seleccionadas")

# URLs probadas y directas en formato PNG/WEBP
LOGOS_MARCAS = {
    "Audi": "https://www.carlogos.org/car-logos/audi-logo.png",
    "BMW": "https://www.carlogos.org/car-logos/bmw-logo.png",
    "Chevrolet": "https://www.carlogos.org/car-logos/chevrolet-logo.png",
    # Enlace oficial de DFSK Perú
    "Glory": "glory_logo.png",
    "Hyundai": "https://www.carlogos.org/car-logos/hyundai-logo.png",
    "Kia": "https://www.carlogos.org/car-logos/kia-logo.png",
    "Mazda": "https://www.carlogos.org/car-logos/mazda-logo.png",
    "Subaru": "https://www.carlogos.org/car-logos/subaru-logo.png",
    "Suzuki": "https://www.carlogos.org/car-logos/suzuki-logo.png",
    "Toyota": "https://www.carlogos.org/car-logos/toyota-logo.png"
}

if marcas_seleccionadas:
    cols_logos = st.columns(min(len(marcas_seleccionadas), 10), vertical_alignment="center")
    for idx, marca in enumerate(marcas_seleccionadas[:10]):
        with cols_logos[idx]:
            url = LOGOS_MARCAS.get(marca)
            if url:
                st.image(url, caption=marca, use_container_width=True)
            else:
                st.markdown(f"**🚘 {marca}**")

st.markdown("---")

# 8. CUADRO DE KPIS
st.subheader("📈 Indicadores Clave de Rendimiento (KPIs)")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Facturación Total", f"S/. {facturacion_total(df_filtrado):,.2f}")
with col2:
    st.metric("Volumen de Ventas", f"{volumen_ventas(df_filtrado):,}")
with col3:
    st.metric("Precio Promedio", f"S/. {precio_promedio(df_filtrado):,.2f}" if not df_filtrado.empty else "S/. 0.00")
with col4:
    st.metric("Transacciones Totales", transacciones_totales(df_filtrado))

col5, col6, col7, col8 = st.columns(4)
with col5:
    st.metric("Precio Máximo", f"S/. {df_filtrado['precio_venta'].max():,.2f}" if not df_filtrado.empty else "S/. 0.00")
with col6:
    st.metric("Precio Mínimo", f"S/. {df_filtrado['precio_venta'].min():,.2f}" if not df_filtrado.empty else "S/. 0.00")
with col7:
    st.metric("Ticket Unitario Promedio", f"S/. {ticket_promedio_unidad(df_filtrado):,.2f}")
with col8:
    st.metric("Unidades por Operación", f"{unidades_por_operacion(df_filtrado):.2f}")

# 9. PANEL DE 9 GRÁFICOS
st.subheader("📊 Panel de Inteligencia Comercial y Análisis Gerencial")

# Fila 1: Gráficos Originales
g1, g2 = st.columns(2)
with g1:
    st.plotly_chart(grafico_ventas_marca(df_filtrado), use_container_width=True)
with g2:
    st.plotly_chart(grafico_promedio_marca(df_filtrado), use_container_width=True)

# Fila 2: Tendencia Histórica y Desempeño por Sede
g3, g4 = st.columns(2)
with g3:
    st.plotly_chart(grafico_evolucion_temporal(df_filtrado), use_container_width=True)
with g4:
    st.plotly_chart(grafico_ventas_sede(df_filtrado), use_container_width=True)

# Fila 3: Métodos de Pago y Ranking de Asesores
g5, g6 = st.columns(2)
with g5:
    st.plotly_chart(grafico_metodo_pago(df_filtrado), use_container_width=True)
with g6:
    st.plotly_chart(grafico_top_asesores(df_filtrado), use_container_width=True)

# Fila 4: Analítica Avanzada (Treemap, Scatter y Boxplot)
g7, g8, g9 = st.columns(3)
with g7:
    st.plotly_chart(grafico_treemap_marca_sede(df_filtrado), use_container_width=True)
with g8:
    st.plotly_chart(grafico_dispersion_precio_volumen(df_filtrado), use_container_width=True)
with g9:
    st.plotly_chart(grafico_boxplot_precios(df_filtrado), use_container_width=True)

# 10. MATRIZ DE DATOS AUDITABLES
st.subheader("📋 Matriz de Datos Filtrados")
st.info(f"Filtros aplicados con éxito. Mostrando {len(df_filtrado)} registros comerciales validados.")

if not df_filtrado.empty:
    st.dataframe(df_filtrado.sort_values(by="fecha", ascending=False), use_container_width=True)
else:
    st.warning("No se encontraron registros comerciales para la combinación de filtros seleccionada.")