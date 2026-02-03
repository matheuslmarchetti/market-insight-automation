"""
Módulo responsável pela coleta de notícias financeiras
utilizando Google News RSS.
"""

import feedparser
from typing import List, Dict
import pandas as pd


def get_news(ticker: str, limit: int = 10) -> List[Dict]:
    """
    Coleta notícias recentes relacionadas a um ativo.

    Parâmetros
    ----------
    ticker : str
        Código do ativo (ex: AAPL, MSFT).
    limit : int
        Número máximo de notícias retornadas.

    Retorno
    -------
    List[Dict]
        Lista de notícias com título, data, link e fonte.
    """
    rss_url = f"https://news.google.com/rss/search?q={ticker}+stock"
    feed = feedparser.parse(rss_url)

    news = []

    for entry in feed.entries[:limit]:
        news.append({
            "ticker": ticker,
            "title": entry.get("title"),
            "published": entry.get("published"),
            "link": entry.get("link"),
            "source": entry.get("source", {}).get("title")
        })

    return news


news = get_news("AAPL", limit=20)
df_news = pd.DataFrame(news)

df_news.to_csv(fr"data\processed\AAPL_news.csv", index=False, sep=";")