import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

print("Starting data cleaning...\n")

# ====================================
# 1. CLEAN FARMERS
# ====================================
farmers = pd.read_csv(RAW_DIR / "farmers.csv")

farmers.columns = farmers.columns.str.lower().str.strip()
farmers.drop_duplicates(inplace=True)

farmers["farmer_id"] = farmers["farmer_id"].astype(int)
farmers["age"] = farmers["age"].astype(int)
farmers["registration_date"] = pd.to_datetime(farmers["registration_date"])

farmers.to_csv(PROCESSED_DIR / "farmers_clean.csv", index=False)
print("Farmers cleaned.")

# ====================================
# 2. CLEAN YIELDS
# ====================================
yields = pd.read_csv(RAW_DIR / "yields.csv")

yields.columns = yields.columns.str.lower().str.strip()
yields.drop_duplicates(inplace=True)

# Remove negative yields (defensive check)
yields = yields[yields["yield_kg"] >= 0]

# Ensure numeric types
yields["yield_kg"] = yields["yield_kg"].astype(float)
yields["area_hectares"] = yields["area_hectares"].astype(float)

# Derived metric
yields["yield_per_hectare"] = (
    yields["yield_kg"] / yields["area_hectares"]
)

yields.to_csv(PROCESSED_DIR / "yields_clean.csv", index=False)
print("Yields cleaned.")

# ====================================
# 3. CLEAN LOANS
# ====================================
loans = pd.read_csv(RAW_DIR / "loans.csv")

loans.columns = loans.columns.str.lower().str.strip()
loans.drop_duplicates(inplace=True)

loans["loan_amount"] = loans["loan_amount"].astype(float)
loans["repaid_amount"] = loans["repaid_amount"].astype(float)
loans["disbursed_date"] = pd.to_datetime(loans["disbursed_date"])

# Repayment rate
loans["repayment_rate"] = loans["repaid_amount"] / loans["loan_amount"]

# Default flag (if less than fully repaid)
loans["default_flag"] = (loans["repaid_amount"] < loans["loan_amount"]).astype(int)

loans.to_csv(PROCESSED_DIR / "loans_clean.csv", index=False)
print("Loans cleaned.")

# ====================================
# 4. CLEAN WEATHER
# ====================================
weather = pd.read_csv(RAW_DIR / "weather.csv")

weather.columns = weather.columns.str.lower().str.strip()
weather.drop_duplicates(inplace=True)

weather["date"] = pd.to_datetime(weather["date"])
weather["rainfall_mm"] = weather["rainfall_mm"].astype(float)
weather["temperature_c"] = weather["temperature_c"].astype(float)

weather.to_csv(PROCESSED_DIR / "weather_clean.csv", index=False)
print("Weather cleaned.")

print("\nData cleaning complete.")