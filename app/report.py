"""
Módulo responsável pela geração de relatórios Excel
com dados de mercado e notícias financeiras.
"""

import os
import pandas as pd
from typing import List, Dict
from news import get_news
import pandas as pd



def generate_excel_report(
    ticker: str,
    market_df: pd.DataFrame,
    news: List[Dict],
    output_dir: str = "data/reports"
) -> str:
    """
    Gera um relatório Excel com dados de mercado e notícias.

    Parâmetros
    ----------
    ticker : str
        Código do ativo (ex: AAPL).
    market_df : pd.DataFrame
        DataFrame com preços e métricas calculadas.
    news : List[Dict]
        Lista de notícias estruturadas.
    output_dir : str
        Diretório onde o relatório será salvo.

    Retorno
    -------
    str
        Caminho do arquivo Excel gerado.
    """
    # Cria o diretório se necessário
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, f"{ticker}_report.xlsx")

    news_df = pd.DataFrame(news)

    with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
        # Aba 1: preços e métricas completas
        market_df.to_excel(writer, sheet_name="Market Data")

        # Aba 2: métricas (somente colunas calculadas)
        metric_cols = [col for col in market_df.columns if col not in ["Open", "High", "Low", "Close", "Volume", "Dividends", "Stock Splits", "daily_return", "ma_7", "volatility_7"]]
        market_df[metric_cols].to_excel(writer, sheet_name="Metrics")

        # Aba 3: notícias
        if not news_df.empty:
            news_df.to_excel(writer, sheet_name="News", index=False)

    return output_path




# Carregar dados processados
df = pd.read_csv(fr"data\processed\AAPL_stock_processed.csv", sep=";", index_col=0, parse_dates=True)

# Coletar notícias
news = get_news("AAPL", limit=15)

# Gerar relatório
path = generate_excel_report("AAPL", df, news)

print(f"📊 Relatório gerado em: {path}")
