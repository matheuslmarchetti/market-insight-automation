from fastapi import FastAPI
from fastapi import Path
from fastapi import HTTPException
from fastapi.responses import FileResponse
import pandas as pd
import os
from pydantic import BaseModel
from typing import List

class StockResponse(BaseModel):
    ticker: str
    rows: int
    columns: List[str]



app = FastAPI(
    title="Market Insight API",
    description="API para consulta de dados financeiros e métricas",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"status": "ok", "message": "API Market Insight está rodando"}



@app.get("/stocks/{ticker}", response_model=StockResponse)
def get_stock(
    ticker: str = Path(
        ...,
        min_length=1,
        max_length=10,
        regex="^[A-Za-z]+$"
    )
):
    file_path = f"data/processed/{ticker}_stock_processed.csv"

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail=f"Dados do ticker '{ticker}' não encontrados."
        )

    try:
        df = pd.read_csv(file_path, sep=";", parse_dates=True)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao ler dados do ticker '{ticker}'."
        )

    if df.empty:
        raise HTTPException(
            status_code=404,
            detail=f"Arquivo encontrado, mas sem dados para '{ticker}'."
        )

    return {
        "ticker": ticker,
        "rows": len(df),
        "columns": df.columns.tolist()
    }


@app.get("/report/{ticker}")
def generate_report(
    ticker: str = Path(
        ...,
        min_length=1,
        max_length=10,
        regex="^[A-Za-z]+$"
    )
):
    file_path = f"data/processed/{ticker}_stock_processed.csv"

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail=f"Dados do ticker '{ticker}' não encontrados."
        )

    try:
        df = pd.read_csv(file_path, sep=";", parse_dates=True)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Erro ao processar dados para geração do relatório."
        )

    if df.empty:
        raise HTTPException(
            status_code=404,
            detail="Não há dados suficientes para gerar o relatório."
        )

    output_dir = "data/reports"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, f"{ticker}_report.xlsx")

    try:
        with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
            df.to_excel(writer, sheet_name="Market Data")
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Erro ao gerar o arquivo Excel."
        )

    return FileResponse(
        path=output_path,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=f"{ticker}_report.xlsx"
    )

