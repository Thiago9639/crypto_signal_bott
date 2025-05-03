from ta.momentum import RSIIndicator

def add_rsi(df, period=14):
    rsi = RSIIndicator(close=df["close"], window=period)
    df["rsi"] = rsi.rsi()
    return df