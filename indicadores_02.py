
# OBTENIENDO INDICADORES GENERALES
#_________________________________

def facturacion_total(df):
    return df["precio_venta"].sum()

def volumen_ventas(df):
    return df["cantidad"].sum()

def precio_promedio(df):
    return df["precio_venta"].mean()

def transacciones_totales(df):
    return len(df)

def precio_maximo(df):
    return df["precio_venta"].max()

def precio_minimo(df):
    return df["precio_venta"].min()

def ticket_promedio_unidad(df):
    if not df.empty and df["cantidad"].sum() > 0:
        return df["precio_venta"].sum() / df["cantidad"].sum()
    return 0.0

def unidades_por_operacion(df):
    if not df.empty and len(df) > 0:
        return df["cantidad"].sum() / len(df)
    return 0.0



