import pandas as pd
import numpy as np
import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()

df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient="index")
df = df.rename(columns={
    "1. open": "open",
    "2. high": "high",
    "3. low": "low",
    "4. close": "close",
    "5. volume": "volume"
})
df.index = pd.to_datetime(df.index)
df = df.sort_index()
df["close"] = pd.to_numeric(df["close"])

short_window = 5
long_window = 25
df["sma_short"] = df["close"].rolling(window=short_window).mean() #сер знач
df["sma_long"] = df["close"].rolling(window=long_window).mean()
df["signal"] = np.where(df["sma_short"] > df["sma_long"], 1, 0) # якщо 1 то купляю, якщо 0 то нє
df["position"] = df["signal"].diff() #дивлюсь на змну

df["return"] = df["close"].pct_change() #на ск відс змінилася ціна
df["strategy"] = df["position"].shift(1) * df["return"] #типа обрахунок стратешії
df["strategy_cum"] = (1 + df["strategy"]).cumprod() #ск всього заробила
df["market_cum"] = (1 + df["return"]).cumprod() #ск б я мала якби просто зберігала

print("Останні сигнали та ефективність:   ")
print(df[["close", "sma_short", "sma_long", "signal", "position", "strategy_cum", "market_cum"]].tail(10))
