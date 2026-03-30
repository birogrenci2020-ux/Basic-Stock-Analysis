!pip install yfinance
import yfinance as yf
import pandas as pd

def fetch_data(ticker, start="2024-01-01"):
    data = yf.download(ticker, start=start)
    return data  

def add_indicators(data):
    df = data.copy()
    df["Returns"] = df["Close"].pct_change()
    df["MA20"] = df["Close"].rolling(20).mean()
    return df 

def get_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return {  
        "Name": info.get("longName"),
        "Sector": info.get("sector"),
        "MarketCap": info.get("marketCap")
    }

def generate_signal(df):
    latest = df.iloc[-1]
    if latest["Close"].item() > latest["MA20"].item():  
        return "uptrend"
    else:
        return "downtrend"

def run_model(ticker):
    data = fetch_data(ticker)
    data = add_indicators(data)
    info = get_info(ticker)
    signal = generate_signal(data)
    print("Stock info:", info)  
    print("Signal:", signal)
    print("\nLatest data:")
    print(data.tail())

run_model("AGX") #just write the stock you ve been wanting to analyze
