def generate_signal(df):
    last = df.iloc[-1]
    if last["rsi"] < 30 and last["macd"] > last["macd_signal"]:
        return "LONG"
    elif last["rsi"] > 70 and last["macd"] < last["macd_signal"]:
        return "SHORT"
    else:
        return "NEUTRO"