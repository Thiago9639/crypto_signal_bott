from collectors.binance import get_ohlcv
from indicators.rsi import add_rsi
from indicators.macd import add_macd
from logic.signal_generator import generate_signal
from alerts.telegram import send_alert

df = get_ohlcv()
df = add_rsi(df)
df = add_macd(df)
signal = generate_signal(df)

print("SINAL:", signal)
send_alert(f"SINAL GERADO: {signal}")