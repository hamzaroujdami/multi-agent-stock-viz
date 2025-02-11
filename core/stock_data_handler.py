# core/stock_data_handler.py
import yfinance as yf
import matplotlib.pyplot as plt

def plot_stock_data(stock_symbols, metric='price'):
    plt.figure(figsize=(10, 5))
    for symbol in stock_symbols:
        stock = yf.Ticker(symbol)
        data = stock.history(period="YTD")
        if metric == 'price':
            plt.plot(data.index, data['Close'], label=f"{symbol} Price")
        elif metric == 'percent_change':
            pct_change = data['Close'].pct_change().cumsum()
            plt.plot(data.index, pct_change, label=f"{symbol} % Change")
    plt.legend()
    plt.title("Stock Performance YTD")
    plt.xlabel("Month")
    plt.ylabel("Price" if metric == 'price' else "% Change")
    plt.show()