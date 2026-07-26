import plotly.express as px
import pandas as pd

# Paleta corporativa en tonalidades azules
PALETTE_BLUE = ["#0A2540", "#1E3A8A", "#2563EB", "#3B82F6", "#60A5FA", "#93C5FD"]

def grafico_ventas_marca(df):
    ventas = df.groupby("marca")["precio_venta"].sum().reset_index()
    fig = px.bar(
        ventas,
        x="marca",
        y="precio_venta",
        title="Volumen de Facturación por Marca Comercial (S/.)",
        labels={"marca": "Marca", "precio_venta": "Ingresos Totales (S/.)"},
        color="precio_venta",
        color_continuous_scale="Blues"
    )
    fig.update_layout(height=360, margin=dict(l=20, r=20, t=40, b=20))
    return fig

def grafico_promedio_marca(df):
    prom = df.groupby("marca")["precio_venta"].mean().reset_index()
    fig = px.bar(
        prom,
        x="marca",
        y="precio_venta",
        title="Comportamiento del Precio Promedio por Marca (S/.)",
        labels={"marca": "Marca", "precio_venta": "Precio Promedio (S/.)"},
        color="precio_venta",
        color_continuous_scale="Cividis"
    )
    fig.update_layout(height=360, margin=dict(l=20, r=20, t=40, b=20))
    return fig

# --- 7 GRÁFICOS ADICIONALES PARA ALTA GERENCIA ---

def grafico_evolucion_temporal(df):
    """G3: Evolución mensual de ventas"""
    df_temp = df.copy()
    df_temp['fecha'] = pd.to_datetime(df_temp['fecha'])
    ventas_tiempo = df_temp.groupby(df_temp['fecha'].dt.to_period('M'))['precio_venta'].sum().reset_index()
    ventas_tiempo['fecha'] = ventas_tiempo['fecha'].astype(str)
    
    fig = px.line(
        ventas_tiempo,
        x="fecha",
        y="precio_venta",
        title="📈 Tendencia Histórica de Facturación Mensual",
        markers=True,
        line_shape="spline",
        color_discrete_sequence=["#1E3A8A"]
    )
    fig.update_layout(height=360, margin=dict(l=20, r=20, t=40, b=20))
    return fig

def grafico_metodo_pago(df):
    """G4: Participación por método de pago"""
    pago = df.groupby("metodo_pago")["precio_venta"].sum().reset_index()
    fig = px.pie(
        pago,
        values="precio_venta",
        names="metodo_pago",
        title="💳 Mix de Facturación por Método de Pago",
        hole=0.4,
        color_discrete_sequence=PALETTE_BLUE
    )
    fig.update_layout(height=360, margin=dict(l=20, r=20, t=40, b=20))
    return fig

def grafico_top_asesores(df):
    """G5: Ranking de asesores comerciales"""
    top = df.groupby("asesor_comercial")["precio_venta"].sum().reset_index().sort_values(by="precio_venta", ascending=True)
    fig = px.bar(
        top.tail(10),
        x="precio_venta",
        y="asesor_comercial",
        orientation="h",
        title="🏆 Ranking Top Asesores por Facturación Total",
        color="precio_venta",
        color_continuous_scale="Blues"
    )
    fig.update_layout(height=360, margin=dict(l=20, r=20, t=40, b=20))
    return fig

def grafico_ventas_sede(df):
    """G6: Facturación por sede/tienda"""
    sedes = df.groupby("tienda")["precio_venta"].sum().reset_index()
    fig = px.bar(
        sedes,
        x="tienda",
        y="precio_venta",
        title="🏢 Desempeño Comercial por Sede / Tienda",
        color="tienda",
        color_discrete_sequence=PALETTE_BLUE
    )
    fig.update_layout(height=360, margin=dict(l=20, r=20, t=40, b=20))
    return fig

def grafico_treemap_marca_sede(df):
    """G7: Treemap multidimensional"""
    fig = px.treemap(
        df,
        path=['tienda', 'marca'],
        values='precio_venta',
        title="🧩 Concentración de Ventas por Sede y Marca (Treemap)",
        color='precio_venta',
        color_continuous_scale='Blues'
    )
    fig.update_layout(height=380, margin=dict(l=20, r=20, t=40, b=20))
    return fig

def grafico_dispersion_precio_volumen(df):
    """G8: Relación Precio vs Cantidad"""
    fig = px.scatter(
        df,
        x="cantidad",
        y="precio_venta",
        color="marca",
        size="precio_venta",
        title="🎯 Distribución de Operaciones (Precio vs. Cantidad)",
        hover_data=['asesor_comercial', 'tienda']
    )
    fig.update_layout(height=380, margin=dict(l=20, r=20, t=40, b=20))
    return fig

def grafico_boxplot_precios(df):
    """G9: Variabilidad y dispersión de precios por marca"""
    fig = px.box(
        df,
        x="marca",
        y="precio_venta",
        color="marca",
        title="📊 Dispersión y Rangos de Precio por Marca"
    )
    fig.update_layout(height=380, margin=dict(l=20, r=20, t=40, b=20), showlegend=False)
    return fig