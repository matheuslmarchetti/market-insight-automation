import pandas as pd
import os

"""
Módulo responsável pelo processamento e cálculo de métricas
de dados financeiros de mercado.
"""


def clean_market_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpa e padroniza dados de mercado.

    - Converte a coluna Date para datetime
    - Define Date como índice
    - Normaliza timezone
    - Remove valores nulos

    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame com dados brutos de mercado.

    Retorno
    -------
    pd.DataFrame
        DataFrame limpo e pronto para análise.
    """
    df = df.copy()

    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], utc=True)
        df.set_index("Date", inplace=True)

    if df.index.tz is not None:
        df.index = df.index.tz_localize(None)

    df.dropna(inplace=True)

    return df



def calculate_daily_return(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula o retorno percentual diário com base no preço de fechamento.
    """
    df = df.copy()
    df["daily_return"] = df["Close"].pct_change()
    return df


def calculate_moving_average(df: pd.DataFrame, window: int = 7) -> pd.DataFrame:
    """
    Calcula a média móvel simples do preço de fechamento.

    Parâmetros
    ----------
    window : int
        Número de dias da janela móvel.
    """
    df = df.copy()
    df[f"ma_{window}"] = df["Close"].rolling(window=window).mean()
    return df


def calculate_volatility(df: pd.DataFrame, window: int = 7) -> pd.DataFrame:
    """
    Calcula a volatilidade simples como o desvio padrão dos retornos.
    """
    df = df.copy()
    df[f"volatility_{window}"] = df["daily_return"].rolling(window).std()
    return df



def process_market_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Executa o pipeline completo de processamento dos dados de mercado.
    """
    df = clean_market_data(df)
    df = calculate_daily_return(df)
    df = calculate_moving_average(df, window=7)
    df = calculate_volatility(df, window=7)

    return df


# Nome do arquivo base e ticker
file = 'AAPL_stock_data'
ticker = file.replace('_data', '')

# Carrega dados brutos
df = pd.read_csv(fr"data\raw\{file}.csv", sep=";")

# Processa dados
processed_df = process_market_data(df)

try:
    # Verifica se há dados processados    
    if processed_df.empty:
        print(f"Aviso: Nenhum dado encontrado para {file}")
    else:
        # Define diretório de saída
        output_dir = fr"data\processed"
        os.makedirs(output_dir, exist_ok=True)
        output_path = f"{output_dir}/{ticker}_processed.csv"
        sep = ";"

        # Cria o diretório se necessário
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Salva CSV tratado
        processed_df.to_csv(output_path, sep=sep)
        
        print(f"✅ Dados salvos com sucesso em: {output_path}")
        print(f"   Período: {processed_df.index[0].date()} a {processed_df.index[-1].date()}")
        print(f"   Registros: {len(processed_df)} linhas")
        print(f"   Colunas: {', '.join(processed_df.columns.tolist())}")
            
except Exception as e:
    print(f"❌ Erro ao processar {ticker}: {e}")
