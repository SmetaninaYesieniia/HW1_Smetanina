import requests
import pandas as pd

#тут я робила запит по своєму місту суми 
url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=50.9216&longitude=34.8003"
    "&hourly=temperature_2m,wind_speed_10m"
    "&forecast_days=7"
    "&timezone=auto"
)

response = requests.get(url)
data = response.json()

df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature": data["hourly"]["temperature_2m"],
    "wind_speed": data["hourly"]["wind_speed_10m"]
})

print("Мінімум:", df["temperature"].min())
print("Максимум:", df["temperature"].max())
print("Середня:", round(df["temperature"].mean(), 2))

wind_mean = df["wind_speed"].mean()
перевищує_середню = df[df["wind_speed"] > wind_mean].shape[0]
print(f"\nКількість годин, коли вітер > середнього ({round(wind_mean, 2)} м/с): {перевищує_середню}")
