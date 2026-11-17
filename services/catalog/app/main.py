
from fastapi import FastAPI

app = FastAPI(
    title="SwapShelf Catalog Service",
    description="Microserviço responsável pela gestão do catálogo de artigos.",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "catalog"}


@app.get("/items")
def list_items():
    return {"items": []}
