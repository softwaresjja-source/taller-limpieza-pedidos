
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from typing import Optional
import pandas as pd
import json

app = FastAPI(
    title="API Pedidos | Taller de Limpieza de Datos",
    description="API profesional para consultar el dataset de pedidos limpio.",
    version="1.0.0"
)

# Cargar datos
df = pd.read_csv("datos/pedidos_limpios.csv")

with open("resumen.json", "r", encoding="utf-8") as f:
    resumen = json.load(f)


@app.get("/", response_class=HTMLResponse)
def pagina_inicio():
    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>API Pedidos • Taller de Limpieza</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
        <style>
            :root {{
                --bg: #0b0f19;
                --card: #111827;
                --border: #1f2937;
                --primary: #3b82f6;
                --primary-hover: #2563eb;
                --text: #e5e7eb;
                --text-muted: #9ca3af;
            }}

            * {{ margin: 0; padding: 0; box-sizing: border-box; }}

            body {{
                font-family: 'Inter', system-ui, sans-serif;
                background: var(--bg);
                color: var(--text);
                line-height: 1.6;
                min-height: 100vh;
            }}

            .container {{
                max-width: 1000px;
                margin: 0 auto;
                padding: 40px 20px;
            }}

            header {{ text-align: center; margin-bottom: 50px; }}

            .badge {{
                display: inline-block;
                background: rgba(59, 130, 246, 0.15);
                color: #60a5fa;
                font-size: 0.75rem;
                font-weight: 600;
                padding: 6px 14px;
                border-radius: 999px;
                letter-spacing: 0.5px;
                margin-bottom: 16px;
                border: 1px solid rgba(59, 130, 246, 0.3);
            }}

            h1 {{
                font-size: 2.5rem;
                font-weight: 700;
                background: linear-gradient(135deg, #60a5fa, #a78bfa);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 12px;
            }}

            .subtitle {{
                color: var(--text-muted);
                font-size: 1.1rem;
                max-width: 600px;
                margin: 0 auto;
            }}

            .grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 16px;
                margin-bottom: 40px;
            }}

            .stat-card {{
                background: var(--card);
                border: 1px solid var(--border);
                border-radius: 12px;
                padding: 24px;
                text-align: center;
                transition: all 0.2s;
            }}

            .stat-card:hover {{
                border-color: var(--primary);
                transform: translateY(-2px);
            }}

            .stat-value {{
                font-size: 2rem;
                font-weight: 700;
                color: #60a5fa;
                font-family: 'JetBrains Mono', monospace;
            }}

            .stat-label {{
                color: var(--text-muted);
                font-size: 0.85rem;
                margin-top: 6px;
            }}

            .section {{
                background: var(--card);
                border: 1px solid var(--border);
                border-radius: 16px;
                padding: 32px;
                margin-bottom: 28px;
            }}

            .section h2 {{
                font-size: 1.25rem;
                margin-bottom: 20px;
            }}

            .endpoint {{
                background: #0f172a;
                border: 1px solid var(--border);
                border-radius: 10px;
                padding: 18px 20px;
                margin-bottom: 14px;
            }}

            .endpoint-header {{
                display: flex;
                align-items: center;
                gap: 12px;
                margin-bottom: 8px;
            }}

            .method {{
                background: #065f46;
                color: #6ee7b7;
                font-size: 0.7rem;
                font-weight: 700;
                padding: 4px 10px;
                border-radius: 6px;
                font-family: 'JetBrains Mono', monospace;
            }}

            .path {{
                font-family: 'JetBrains Mono', monospace;
                font-size: 0.95rem;
                color: #e2e8f0;
            }}

            .endpoint p {{
                color: var(--text-muted);
                font-size: 0.9rem;
            }}

            .actions {{
                display: flex;
                flex-wrap: wrap;
                gap: 12px;
                margin-top: 24px;
            }}

            .btn {{
                display: inline-flex;
                align-items: center;
                background: var(--primary);
                color: white;
                padding: 12px 20px;
                border-radius: 10px;
                text-decoration: none;
                font-weight: 500;
                font-size: 0.95rem;
                transition: all 0.2s;
            }}

            .btn:hover {{ background: var(--primary-hover); }}

            .btn-secondary {{
                background: transparent;
                border: 1px solid var(--border);
                color: var(--text);
            }}

            .btn-secondary:hover {{
                border-color: var(--primary);
                background: rgba(59, 130, 246, 0.1);
            }}

            .process {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
                gap: 16px;
            }}

            .step {{
                background: #0f172a;
                border-radius: 10px;
                padding: 18px;
                border: 1px solid var(--border);
            }}

            .step-number {{
                width: 28px;
                height: 28px;
                background: var(--primary);
                color: white;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 0.8rem;
                font-weight: 700;
                margin-bottom: 12px;
            }}

            .step h3 {{ font-size: 0.95rem; margin-bottom: 6px; }}
            .step p {{ color: var(--text-muted); font-size: 0.85rem; }}

            footer {{
                text-align: center;
                color: var(--text-muted);
                font-size: 0.85rem;
                margin-top: 50px;
                padding-top: 30px;
                border-top: 1px solid var(--border);
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <div class="badge">API PÚBLICA • DATOS LIMPIOS</div>
                <h1>API de Pedidos</h1>
                <p class="subtitle">
                    Servicio REST construido con FastAPI. Expone el dataset de pedidos después de un proceso de limpieza reproducible versionado con Git.
                </p>
            </header>

            <div class="grid">
                <div class="stat-card">
                    <div class="stat-value">{resumen.get("filas", "-")}</div>
                    <div class="stat-label">Pedidos limpios</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">{resumen.get("duplicados", 0)}</div>
                    <div class="stat-label">Duplicados</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">{resumen.get("metodos_pago_unicos", "-")}</div>
                    <div class="stat-label">Métodos de pago</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">{resumen.get("estados_unicos", "-")}</div>
                    <div class="stat-label">Estados</div>
                </div>
            </div>

            <div class="section">
                <h2>Endpoints disponibles</h2>

                <div class="endpoint">
                    <div class="endpoint-header">
                        <span class="method">GET</span>
                        <span class="path">/salud</span>
                    </div>
                    <p>Verifica que el servicio esté activo y respondiendo correctamente.</p>
                </div>

                <div class="endpoint">
                    <div class="endpoint-header">
                        <span class="method">GET</span>
                        <span class="path">/resumen</span>
                    </div>
                    <p>Devuelve las métricas principales del dataset limpio.</p>
                </div>

                <div class="endpoint">
                    <div class="endpoint-header">
                        <span class="method">GET</span>
                        <span class="path">/pedidos?estado=Entregado&limite=3</span>
                    </div>
                    <p>Consulta pedidos filtrados por estado y con límite de resultados.</p>
                </div>

                <div class="actions">
                    <a class="btn" href="/docs" target="_blank">Documentación interactiva</a>
                    <a class="btn btn-secondary" href="/salud">Probar /salud</a>
                    <a class="btn btn-secondary" href="/resumen">Ver /resumen</a>
                    <a class="btn btn-secondary" href="/pedidos?estado=Entregado&limite=3">3 pedidos entregados</a>
                </div>
            </div>

            <div class="section">
                <h2>Proceso realizado</h2>
                <div class="process">
                    <div class="step">
                        <div class="step-number">1</div>
                        <h3>Exploración</h3>
                        <p>Análisis de forma, tipos, nulos y problemas de calidad.</p>
                    </div>
                    <div class="step">
                        <div class="step-number">2</div>
                        <h3>Limpieza</h3>
                        <p>Reglas reproducibles aplicadas una a una y documentadas.</p>
                    </div>
                    <div class="step">
                        <div class="step-number">3</div>
                        <h3>Versionado</h3>
                        <p>Estados guardados con Git (antes y después de limpiar).</p>
                    </div>
                    <div class="step">
                        <div class="step-number">4</div>
                        <h3>API</h3>
                        <p>Exposición de los datos limpios a través de endpoints REST.</p>
                    </div>
                </div>
            </div>

            <footer>
                Taller de Limpieza de Datos • FastAPI + Render • Datos versionados con Git
            </footer>
        </div>
    </body>
    </html>
    """
    return html


@app.get("/salud")
def salud():
    return {"status": "ok", "mensaje": "La API está funcionando correctamente"}


@app.get("/resumen")
def obtener_resumen():
    return resumen


@app.get("/pedidos")
def obtener_pedidos(
    estado: Optional[str] = Query(None, description="Filtrar por estado (ej: Entregado)"),
    limite: int = Query(5, ge=1, le=50, description="Cantidad máxima de pedidos")
):
    datos = df.copy()
    if estado:
        datos = datos[datos["estado"].str.lower() == estado.lower()]
    resultado = datos.head(limite).to_dict(orient="records")
    return {
        "total_encontrados": len(datos),
        "limite": limite,
        "pedidos": resultado
    }
