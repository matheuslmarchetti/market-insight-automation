import pandas as pd
import os

def clean_market_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

     # se existir coluna Date, usar como índice
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], utc=True)
        df.set_index("Date", inplace=True)
        df.index = df.index.tz_localize(None)


    # remover linhas com valores nulos
    df.dropna(inplace=True)

    return df


def calculate_daily_return(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["daily_return"] = df["Close"].pct_change()

    return df

def calculate_moving_average(df: pd.DataFrame, window: int = 7) -> pd.DataFrame:
    df = df.copy()

    df[f"ma_{window}"] = df["Close"].rolling(window=window).mean()

    return df


def calculate_volatility(df: pd.DataFrame, window: int = 7) -> pd.DataFrame:
    df = df.copy()

    df[f"volatility_{window}"] = (
        df["daily_return"]
        .rolling(window=window)
        .std()
    )

    return df


def process_market_data(df: pd.DataFrame) -> pd.DataFrame:
    df = clean_market_data(df)
    df = calculate_daily_return(df)
    df = calculate_moving_average(df, window=7)
    df = calculate_volatility(df, window=7)

    return df


file = 'AAPL_stock_data'
ticker = file.replace('_data', '')
df = pd.read_csv(fr"data\raw\{file}.csv", sep=";")
processed_df = process_market_data(df)

try:
    # salvar dados
    
    if processed_df.empty:
        print(f"Aviso: Nenhum dado encontrado para {file}")
    else:
        # Define o caminho de saída
        output_dir = fr"data\processed"
        os.makedirs(output_dir, exist_ok=True)
        output_path = f"{output_dir}/{ticker}_processed.csv"
        sep = ";"
        # Cria o diretório se necessário
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Salva em CSV
        processed_df.to_csv(output_path, sep=sep)
        print(f"✅ Dados salvos com sucesso em: {output_path}")
        print(f"   Período: {processed_df.index[0].date()} a {processed_df.index[-1].date()}")
        print(f"   Registros: {len(processed_df)} linhas")
        print(f"   Colunas: {', '.join(processed_df.columns.tolist())}")
            
except Exception as e:
    print(f"❌ Erro ao processar {ticker}: {e}")
