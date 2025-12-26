import requests
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# CONFIGURATION
# -----------------------------
API_KEY = os.getenv("PASTE_YOUR_OPENWEATHER_API_KEY_HERE")   # API key
CITY = "Delhi"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# -----------------------------
# FETCH DATA FROM API
# -----------------------------
response = requests.get(URL)
data = response.json()

# -----------------------------
# EXTRACT TEMPERATURE DATA
# -----------------------------
dates = []
temperatures = []

for item in data["list"]:
    dates.append(item["dt_txt"])
    temperatures.append(item["main"]["temp"])

# -----------------------------
# VISUALIZATION
# -----------------------------
sns.set(style="darkgrid")
plt.figure(figsize=(12, 6))
plt.plot(dates, temperatures, marker="o")
plt.xticks(rotation=45)
plt.title(f"5-Day Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()
