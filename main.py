
from fastapi import FastAPI, Query
from typing import Optional
import pandas as pd
import json

app = FastAPI(title="API Pedidos", version="1.0")

# Cargar datos al iniciar
df = pd.read_csv("datos/pedidos_limpios.csv")

with open("resumen.json", "r", encoding="utf-8") as f:
    resumen = json.load(f)


@app.get("/salud")
def salud():
    """Confirma que la aplicación está funcionando"""
    return {"status": "ok", "mensaje": "La API está funcionando correctamente"}


@app.get("/resumen")
def obtener_resumen():
    """Devuelve las métricas del archivo limpio"""
    return resumen


@app.get("/pedidos")
def obtener_pedidos(
    estado: Optional[str] = Query(None, description="Filtrar por estado (ej: Entregado)"),
    limite: int = Query(5, ge=1, le=50, description="Cantidad máxima de pedidos a devolver")
):
    """
    Devuelve pedidos.  
    Ejemplo: /pedidos?estado=Entregado&limite=3
    """
    datos = df.copy()

    if estado:
        datos = datos[datos["estado"].str.lower() == estado.lower()]

    # Convertir a diccionario para que FastAPI pueda devolverlo
    resultado = datos.head(limite).to_dict(orient="records")
    return {
        "total_encontrados": len(datos),
        "limite": limite,
        "pedidos": resultado
    }
