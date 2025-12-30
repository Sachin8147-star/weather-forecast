import requests
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# CONFIGURATION
# -----------------------------
API_KEY ="PUT_YOUR_OPENWEATHER_API_KEY_HERE"  # API key  "place your oprnweather api key here"

if API_KEY is None:
    raise ValueError("API key not found. set OPENWEATHER_API_KEY environmental variable.")
CITY = "Delhi"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

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

if "list" not in data:
    print("API Error: ",data)
    exit()

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
