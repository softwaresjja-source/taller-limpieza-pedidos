# Taller de Limpieza de Datos - API Consultable

Proyecto del Taller S04 (Optativa II - 7792).
Se parte de un dataset sucio de pedidos, se aplica un proceso de limpieza reproducible y se expone el resultado a traves de una API publica.

## Que se hizo

1. Exploracion del dataset original (dimensiones, tipos, nulos, problemas de calidad).
2. Limpieza con reglas claras y documentadas (una por una).
3. Versionado con Git (estado antes y despues de limpiar).
4. API con FastAPI publicada en Render.

## Estructura del repositorio

- main.py                 -> Codigo de la API
- requirements.txt        -> Dependencias
- resumen.json            -> Metricas del dataset limpio
- datos/pedidos_limpios.csv -> Dataset despues de la limpieza

## Endpoints de la API

| Ruta | Descripcion |
|------|-------------|
| / | Pagina de inicio con resumen del proyecto |
| /salud | Verifica que la API este funcionando |
| /resumen | Metricas del dataset limpio |
| /pedidos?estado=Entregado&limite=3 | Consulta de pedidos filtrados |
| /docs | Documentacion interactiva (Swagger) |

URL publica: https://taller-limpieza-pedidos.onrender.com

## Como probar localmente

pip install -r requirements.txt
uvicorn main:app --reload

Luego abre: http://127.0.0.1:8000/docs

## Tecnologias usadas

- Python + Pandas
- FastAPI + Uvicorn
- Git + GitHub
- Render (despliegue)

## Autores

Grupo del Taller S04 - Optativa II
