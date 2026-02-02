import yfinance as yf
import os
import pandas as pd

def get_and_save_stock_data(ticker, start, end, output_path=None):
    """
    Fetch historical stock data and save to CSV.
    
    Parameters:
    ticker (str): The stock ticker symbol.
    start (str): The start date in 'YYYY-MM-DD' format.
    end (str): The end date in 'YYYY-MM-DD' format.
    output_path (str): Custom output path. If None, uses default path.
    
    Returns:
    pandas.DataFrame: A DataFrame containing the historical stock data.
    """
    try:
        # Baixa os dados
        stock = yf.Ticker(ticker)
        data = stock.history(start=start, end=end)
        
        if data.empty:
            print(f"Aviso: Nenhum dado encontrado para {ticker} no período {start} a {end}")
            return data
        
        # Define o caminho de saída
        if output_path is None:
            output_dir = fr"data\raw"
            os.makedirs(output_dir, exist_ok=True)
            output_path = f"{output_dir}/{ticker}_stock_data.csv"
            sep = ";"
        else:
            # Cria o diretório se necessário
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Salva em CSV
        data.to_csv(output_path, sep=sep)
        print(f"✅ Dados salvos com sucesso em: {output_path}")
        print(f"   Período: {data.index[0].date()} a {data.index[-1].date()}")
        print(f"   Registros: {len(data)} linhas")
        print(f"   Colunas: {', '.join(data.columns.tolist())}")
        
        return data
        
    except Exception as e:
        print(f"❌ Erro ao processar {ticker}: {e}")
        return pd.DataFrame()

# Exemplo de uso
data = get_and_save_stock_data("AAPL", "2025-01-01", "2025-12-31")
print("\nPrimeiras linhas dos dados:")
print(data.head())


def get_multiple_stocks_and_save(tickers, start, end):
    """
    Fetch historical stock data for multiple tickers and save each to CSV.
    
    Parameters:
    tickers (list): List of stock ticker symbols.
    start (str): The start date in 'YYYY-MM-DD' format.
    end (str): The end date in 'YYYY-MM-DD' format.
    
    Returns:
    dict: Dictionary with tickers as keys and DataFrames as values.
    """
    all_data = {}
    output_dir = fr"data\raw"
    os.makedirs(output_dir, exist_ok=True)
    
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            data = stock.history(start=start, end=end)
            
            if not data.empty:
                # Salva em CSV
                filename = f"{output_dir}/{ticker}_stock_data.csv"
                sep = ";"
                data.to_csv(filename, sep=sep)
                all_data[ticker] = data
                print(f"✅ {ticker}: {len(data)} registros salvos em {filename}")
            else:
                print(f"⚠️  {ticker}: Nenhum dado encontrado")
                
        except Exception as e:
            print(f"❌ {ticker}: Erro - {e}")
    
    return all_data

# Exemplo com múltiplos tickers
tickers = ["MSFT", "GOOGL", "TSLA"]
all_data = get_multiple_stocks_and_save(tickers, "2025-01-01", "2025-12-31")