import yfinance as yf

def get_stock_data(ticker, start, end):
    """
    Fetch historical stock data for a given ticker symbol between start and end dates.

    Parameters:
    ticker (str): The stock ticker symbol.
    start (str): The start date in 'YYYY-MM-DD' format.
    end (str): The end date in 'YYYY-MM-DD' format.

    Returns:
    pandas.DataFrame: A DataFrame containing the historical stock data.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(start=start, end=end)
    return data

print(get_stock_data("AAPL", "2023-01-01", "2023-06-01"))