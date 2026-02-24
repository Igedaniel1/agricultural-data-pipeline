import pandas as pd
from faker import Faker
import random

fake = Faker()

# Farmers
farmers = []
for i in range(100):
    farmers.append({
        "farmer_id": i + 1,
        "name": fake.name(),
        "age": random.randint(18, 65),
        "gender": random.choice(["Male", "Female"]),
        "region": random.choice(["North", "South", "East", "West"]),
        "registration_date": fake.date_between(start_date="-3y", end_date="today")
    })

df_farmers = pd.DataFrame(farmers)
df_farmers.to_csv("data/raw/farmers.csv", index=False)

# Yields
yields = []
for i in range(200):
    yields.append({
        "yield_id": i + 1,
        "farmer_id": random.randint(1, 100),
        "crop": random.choice(["Maize", "Rice", "Soy", "Cassava"]),
        "season": random.choice(["2022", "2023", "2024"]),
        "yield_kg": random.randint(500, 5000),
        "area_hectares": round(random.uniform(0.5, 5.0), 2)
    })

df_yields = pd.DataFrame(yields)
df_yields.to_csv("data/raw/yields.csv", index=False)

# Loans
loans = []
for i in range(100):
    amount = random.randint(50000, 500000)
    repaid = random.randint(0, amount)
    loans.append({
        "loan_id": i + 1,
        "farmer_id": random.randint(1, 100),
        "loan_amount": amount,
        "disbursed_date": fake.date_between(start_date="-2y", end_date="today"),
        "repaid_amount": repaid,
        "status": "Repaid" if repaid >= amount else "Default"
    })

df_loans = pd.DataFrame(loans)
df_loans.to_csv("data/raw/loans.csv", index=False)

# Weather
weather = []
for i in range(365):
    weather.append({
        "weather_id": i + 1,
        "region": random.choice(["North", "South", "East", "West"]),
        "date": fake.date_between(start_date="-1y", end_date="today"),
        "rainfall_mm": round(random.uniform(0, 200), 2),
        "temperature_c": round(random.uniform(18, 35), 2)
    })

df_weather = pd.DataFrame(weather)
df_weather.to_csv("data/raw/weather.csv", index=False)

print("Data generated!")