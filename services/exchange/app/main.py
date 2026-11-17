
from fastapi import FastAPI

app = FastAPI(
    title="SwapShelf Exchange Service",
    description="Microserviço responsável pela gestão de propostas e trocas.",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "exchange"}


@app.get("/exchanges")
def list_exchanges():
    return {"exchanges": []}
