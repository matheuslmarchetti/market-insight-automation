from fastapi import FastAPI
from fastapi import HTTPException
import pandas as pd
import os


app = FastAPI(
    title="Market Insight API",
    description="API para consulta de dados financeiros e métricas",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"status": "ok", "message": "API Market Insight está rodando"}



@app.get("/stocks/{ticker}")
def get_stock(ticker: str):
    file_path = f"data/processed/{ticker}_stock_processed.csv"

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail=f"Ticker {ticker} não encontrado"
        )

    df = pd.read_csv(file_path, sep=";", parse_dates=True)

    return {
        "ticker": ticker,
        "rows": len(df),
        "columns": df.columns.tolist()
    }

